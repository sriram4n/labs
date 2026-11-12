import 'package:flutter/material.dart';

void main() {
  runApp(Counter());
}

class Counter extends StatefulWidget {
  State<Counter> createState() => CounterState();
}

class CounterState extends State<Counter> {
  int _count = 0;
  void _increment() {
    setState(() => _count++);
  }

  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: Column(
            children: [
              Text("You have clicked this many times: "),
              Text(_count.toString()),
              ElevatedButton(onPressed: _increment, child: Text("Click me")),
            ],
          ),
        ),
      ),
    );
  }
}
