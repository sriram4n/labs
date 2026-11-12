import 'package:flutter/material.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  Widget build(BuildContext context){
    return MaterialApp(
      home:Scaffold(
        appBar: AppBar(title: 
          RichText(
            text: TextSpan(
              children:[
                TextSpan(text: "Rich", style:TextStyle(fontSize: 22)),
                TextSpan(text: "Text", style:TextStyle(fontSize: 26, color: Colors.blue)),
              ],
            ),
          ),
          backgroundColor: Colors.grey,
        ),

        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              RichText(
                text: TextSpan(
                  children: [
                    TextSpan(
                      text: "Hello",
                      style: TextStyle(fontSize: 30, fontWeight: FontWeight(100))
                    ),
                    TextSpan(
                      text: " World", 
                      style: TextStyle(fontSize: 38, fontWeight: FontWeight(800), color: Colors.blue),
                    )
                  ],
                ),
              )
          ],),
        ),
      ),
    );
  }
}