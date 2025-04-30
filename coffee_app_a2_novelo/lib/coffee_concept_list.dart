import 'package:coffee_app_a2_novelo/coffee.dart';
import 'package:coffee_app_a2_novelo/coffee_concept_details.dart';
import 'package:flutter/material.dart';

const _duration = Duration(milliseconds: 300);
const _initialPage = 8.0;

class CoffeeConceptList extends StatefulWidget {
  @override
  _CoffeeConceptListState createState() => _CoffeeConceptListState();
}

class _CoffeeConceptListState extends State<CoffeeConceptList> {
  final _pageCoffeeController = PageController(
    viewportFraction: 0.35,
    initialPage: _initialPage.toInt(),
  ); 
  final _pageTextController = PageController(initialPage: _initialPage.toInt());
  double _currentPage = _initialPage;
  double _textPage = _initialPage;


  void _coffeeScrollListner() {
    setState(() {
      _currentPage = _pageCoffeeController.page!;

    });
  }

  void _textScrollListener(){
    _textPage = _currentPage;

  }

  @override
  void initState() {
    _pageCoffeeController.addListener(_coffeeScrollListner);
    _pageTextController.addListener(_textScrollListener);
    super.initState();
  }

  @override
  void dispose() {
    _pageCoffeeController.removeListener(_coffeeScrollListner);
    _pageTextController.removeListener(_textScrollListener);
    _pageCoffeeController.dispose();
    _pageTextController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: BackButton(
          color: Colors.black,
        ),
      ),
      body: Stack(
        children: [
          Positioned(
            left: 20,
            right: 20,
            bottom: -size.height*0.22,
            height: size.height*0.3,
            child: DecoratedBox(
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                boxShadow: [
                  BoxShadow(
                    color: Colors.brown,
                    blurRadius: 90,
                    spreadRadius: 45,
                  )
                ],
              ),
            ),
          ),
          Transform.scale(
            scale: 1.6,
            alignment: Alignment.bottomCenter,
            child: PageView.builder(
              controller: _pageCoffeeController,
              scrollDirection: Axis.vertical,
              itemCount: coffees.length + 1,
              onPageChanged: (value){
                if (value < coffees.length) {
                  _pageTextController.animateToPage(
                    value,
                    duration: _duration,
                    curve: Curves.easeOut,
                  );
                }
              },
              itemBuilder: (context, index){
                if (index == 0) {
                return const SizedBox.shrink();}
                final coffee = coffees[index-1];
                final result = _currentPage - index + 1;
                final value = -0.4 * result + 1; 
                final opacity = value.clamp(0.0, 1.0);
              
                return GestureDetector(
                  onTap: () {
                    Navigator.of(context).push(
                      PageRouteBuilder(
                        transitionDuration: Duration(milliseconds: 650),
                        pageBuilder: (context, animation, _) {
                          return FadeTransition(
                            opacity: animation,
                            child: CoffeeConceptDetails(coffee: coffee),
                        );
                      }),
                    );
                  },
                  child: Padding(
                    padding: const EdgeInsets.only(bottom: 20),
                    child: Transform(
                      alignment: Alignment.bottomCenter,
                      transform: Matrix4.identity()
                        ..setEntry(3, 2, 0.001)
                        ..translate(0.0, size.height/2.6 *(1-value).abs(),) 
                        ..scale(value),
                      child: Opacity(
                        opacity: opacity, 
                        child: Hero(
                          tag: coffee.name,
                          child: Image.asset(
                          coffee.image,
                          fit: BoxFit.fitHeight,
                      ),
                    )),
                  ),
                                ),
                );  
            },
          ),
        ),
      Positioned(
            left: 0,
            top: 0,
            right: 0,
            height: 100,
            child: Column(
              children: [
                Expanded (
                  child: PageView.builder(
                    itemCount: coffees.length,
                    controller: _pageTextController,
                    physics: const NeverScrollableScrollPhysics(),
                    itemBuilder: (context, index) {
                      final opacity = (1-(index - _textPage).abs()).clamp(0.0, 1.0);
                      return Opacity(
                        opacity: opacity,
                        child: Padding(
                        padding: EdgeInsets.symmetric(horizontal: size.width* 0.2),
                        child: Hero(
                          tag:"text_${coffees[index].name}",
                          child:Material(
                            child: Text(
                              coffees[index].name,
                              maxLines: 2,
                              textAlign: TextAlign.center,
                              style: TextStyle(
                                fontSize: 25,
                                fontWeight: FontWeight.w800,
                                ),
                              ),
                            ),  
                          ),
                        ),
                      );
                    }),
                ),
                SizedBox(height: 15,),
                AnimatedSwitcher(
                  duration: _duration,
                  child: Text(
                    '\$${coffees[_currentPage.toInt()].price.toStringAsFixed(2)}',
                    style: TextStyle(
                      fontSize: 24,
                    ),
                    key: Key(coffees[_currentPage.toInt()].name),
                  ),
                ),
              ],
            ),    
          ),
        ],
      ),
    );
  }
}
