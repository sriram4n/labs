import 'package:flutter/material.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  Widget build(BuildContext context){
    return MaterialApp(home: HelloWorld());
  }
}

class HelloWorld extends StatefulWidget{
  State<HelloWorld> createState() => _HomePageState();
}

class _HomePageState extends State<HelloWorld>{
  String message = "Hello World";
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home:Scaffold(
        body:Center(
          child:Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(message),
              ElevatedButton(onPressed: (){
                setState((){
                  message = message == "Hello World" ? "This is Flutter" : "Hello World";
                });
              },
              child: Text("Change text"),
              ),
            ],
          ),
        ),
      ),
    );    
  }
  
}
