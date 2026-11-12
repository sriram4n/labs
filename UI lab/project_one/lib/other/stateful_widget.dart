import 'package:flutter/material.dart';

void main() {
  runApp(Counter());
}

class Counter extends StatefulWidget {
  @override
  State<Counter> createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  int _count = 0;

  void _increment() {
    setState(() => _count++);
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("You clicked the button this many times:"),
              Text(_count.toString()),
              ElevatedButton(
                onPressed: _increment,
                child: Text("Increment"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
