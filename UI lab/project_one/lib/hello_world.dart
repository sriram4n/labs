import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text(
            "Hello World Program",
            style: TextStyle(color: Colors.white),
          ),
          backgroundColor: Colors.deepPurple,
        ),
        backgroundColor: Colors.deepPurple[200],
        body: Center(
          child: Text("Hello World", style: TextStyle(fontSize: 30)),
        ),
      ),
    );
  }
}
