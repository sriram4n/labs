import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("My Portofoliolololo"),
          backgroundColor: Colors.indigoAccent,
        ),
        body: Center(
          child: Column(
            children: <Widget>[
              Image.asset('Profile.png'),
              Text(
                "I AM GREATTTTTT AND I LIKE ROBLOX AMONGUS SUSSYBAKA 420 69 67",
              ),
            ],
          ),
        ),
      ),
    );
  }
}
