import 'dart:math';

double _doubleInRange(Random source , num start, num end) => start + source.nextDouble() * (end - start);
final random = Random();
final coffees = List.generate(
  _names.length,
  (index) => Coffee(
    image: 'assets/images/${index + 1}.png',
    name: _names[index],
    price: _doubleInRange(random, 3, 7),
  ),
);

class Coffee {

  final String image;
  final String name;
  final double price;

  Coffee({
    required this.image,
    required this.name,
    required this.price,
  });
}

final _names = [
  'Caramel Cold Drink',
  'Iced Coffee Mocha',
  'Caramelized Pecan Latte',
  'Toffee Nut Latte',
  'Capuchino',
  'Toffee Nut Iced Latte',
  'Americano',
  'Vietnamese-Style Iced',
  'Caramel Macchiato',
  'Black Tea Latte',
  'Classic Irish Coffee',
  'Toffee Nut Crunch Latte',
];