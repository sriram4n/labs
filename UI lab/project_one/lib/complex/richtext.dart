import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.blue,
          title: RichText(
            text: TextSpan(
              children: [
                TextSpan(
                  text: "Rich",
                  style: TextStyle(color: Colors.black, fontSize: 22),
                ),
                TextSpan(
                  text: "Text",
                  style: TextStyle(color: Colors.white, fontSize: 22),
                ),
              ],
            ),
          ),
        ),
        body: Center(
          child: RichText(
            text: TextSpan(
              children: [
                TextSpan(
                  text: "Hello",
                  style: TextStyle(color: Colors.black, fontSize: 24),
                ),
                TextSpan(
                  text: "World!",
                  style: TextStyle(color: Colors.blue, fontSize: 28),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
