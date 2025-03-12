import 'dart:math';

double _doubleInRange(Random source , num start, num end) => start + source.nextDouble() * (end - start);
final random = Random();
final coffees = List.generate(
  _names.length,
  (index) => Coffee(
    image: 'assets/coffee_concept/${index + 1}.png',
    name: _names[index],
    price: _doubleInRange(random, 3, 7),
  ),
);

class Coffee {
  Coffee({
    required this.image,
    required this.name,
    required this.price,
  });

  final String image;
  final String name;
  final double price;
}

final _names = [
  'Cappuccino',
  'Flat White',
  'Espresso',
  'Americano',
  'Cafe Latte',
  'Mocha',
];