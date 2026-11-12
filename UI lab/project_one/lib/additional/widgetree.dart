import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Widget Tree"),
        ),
        body: Center(
          child: Container(
            padding: EdgeInsets.all(20),
            color: Colors.blue,
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  "Hello Flutter!",
                  style: TextStyle(fontSize: 24),
                ),
                SizedBox(height: 20),
                ElevatedButton(
                  onPressed: () {},
                  child: Text("Click Me"),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}