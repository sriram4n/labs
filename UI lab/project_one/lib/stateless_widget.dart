import 'package:flutter/material.dart';

void main() {
  runApp(MyClass());
}

void clicked() {
  print("Click!");
}

class MyClass extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
            child: Container(
              height: 300,
              width: 300,
              color: Colors.deepPurple,
              child: Center(
                child: ElevatedButton(onPressed: clicked, child: Text("press me bbg")),
              ),
            ),
          ),
        ),
      );
  }
}
