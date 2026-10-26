import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.blue[200],
        appBar: AppBar(
          title: Text("Row Widget Demo"),
          backgroundColor: Colors.blue[300],
        ),
        body: Center(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Container(
                padding: EdgeInsets.all(30),
                color: Colors.blueGrey[900],
                child: Text("Flutter", style: TextStyle(color: Colors.white)),
              ),
              Container(
                padding: EdgeInsets.all(30),
                color: Colors.blueGrey[900],
                child: Text("Shlutter", style: TextStyle(color: Colors.white)),
              ),
              Container(
                padding: EdgeInsets.all(30),
                color: Colors.blueGrey[900],
                child: Text("Tlutter", style: TextStyle(color: Colors.white)),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
