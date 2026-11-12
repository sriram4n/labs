import 'package:flutter/material.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  Widget build(BuildContext context){
    return MaterialApp(
      home:Scaffold(
        backgroundColor: Colors.black,
        appBar: AppBar(title: Text("WELCOME TO CMR!!"), backgroundColor: Colors.amber[800]),
        body:Center(
          child: Column(children: [
            Text(
            "Think placements",
            style: TextStyle(
                color: Colors.amber,
                fontSize: 50,
                fontWeight: FontWeight.w700,
                wordSpacing: 6,
                letterSpacing: 6,
                // backgroundColor: Colors.grey[900],
                shadows: [
                  Shadow(color: Colors.amber, offset: Offset(2, 1), blurRadius: 15)
                ]
              ),
            ),
            Text(
            "Think cmr (i guess)",
            style: TextStyle(
                color: Colors.amber[100],
                fontSize: 20,
                fontWeight: FontWeight.w300,
                letterSpacing: 3,
                wordSpacing: 1,
              ),
            ),
          ],)
        ),
      ),
    );
  }
}