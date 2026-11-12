import 'package:flutter/material.dart';

// least likely question
void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              ButtonBar(
                children: [
                  ElevatedButton(onPressed: () {}, child: Text("hi")),
                  ElevatedButton(onPressed: () {}, child: Text("hello")),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
