import 'package:flutter/material.dart';
void main() {
  runApp(App());
}
class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: MyApp());
  }
}
class MyApp extends StatefulWidget {
  State<MyApp> createState() => _CounterState();
}

class _CounterState extends State<MyApp> {
  int _count = 0;
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Click count"),
          backgroundColor: Colors.amber,
        ),
        body: Center(
          child:Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("You have clicked this many times: "),
              Text(_count.toString()),
          ],),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () => {
            setState(() {
              _count++;
            }),
          },
          backgroundColor: Colors.amber,
          foregroundColor: Colors.amber[100],
          child: Icon(Icons.plus_one),
        ),
      ),
    );
  }
}
