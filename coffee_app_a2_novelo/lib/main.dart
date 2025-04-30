import 'package:coffee_app_a2_novelo/coffee_concept_home.dart';

import 'package:flutter/material.dart';

void main() => runApp(MainCoffeeConceptApp());
class MainCoffeeConceptApp extends StatelessWidget {
  const MainCoffeeConceptApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.dark(),
      home: CoffeeConceptHome(),
    );
  }
}
