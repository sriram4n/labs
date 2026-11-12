import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(home: MyApp()));
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Multiple Widgets"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Text(
              "Hello Flutter!",
              style: TextStyle(fontSize: 25),
            ),

            Icon(Icons.favorite, color: Colors.red, size: 50),

            Container(
              height: 80,
              width: 200,
              color: Colors.blue,
              child: Center(
                child: Text(
                  "Container Widget",
                  style: TextStyle(color: Colors.white),
                ),
              ),
            ),


            TextField(
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                hintText: "Enter your name",
              ),
            ),

            ElevatedButton(
              onPressed: () {},
              child: Text("Submit"),
            ),
          ],
        ),
      ),
    );
  }
}