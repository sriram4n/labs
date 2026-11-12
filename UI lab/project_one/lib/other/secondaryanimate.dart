import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(home: MyApp()));
}

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => MyAppState();
}

class MyAppState extends State<MyApp> {
  double size = 100;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Animation")),
      body: Center(
        child: AnimatedContainer(
          duration: Duration(seconds: 1),
          width: size,
          height: size, 
          color: Colors.blue,
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            size = size == 100 ? 200 : 100; //if size 100, make it 200 
          });
        },
        child: Icon(Icons.play_arrow),
      ),
    );
  }
}