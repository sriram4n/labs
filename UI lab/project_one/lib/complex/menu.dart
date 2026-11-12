import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  State<MyApp> createState() => _MyState();
}

class _MyState extends State<MyApp> {
  Color color = Colors.white;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text("Menu Page"), backgroundColor: color),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              MenuAnchor(
                menuChildren: [
                  MenuItemButton(
                    onPressed: () {
                      setState(() {
                        color = Colors.blue;
                      });
                    },
                    child: Text("Blue"),
                  ),
                  MenuItemButton(
                    onPressed: () {
                      setState(() {
                        color = Colors.red;
                      });
                    },
                    child: Text("Red"),
                  ),
                  MenuItemButton(
                    onPressed: () {
                      setState(() {
                        color = Colors.pink;
                      });
                    },
                    child: Text("Pink"),
                  ),
                ],
                builder: (context, controller, child) {
                  return ElevatedButton(
                    onPressed: () {
                      controller.isOpen
                          ? controller.close()
                          : controller.open();
                    },
                    child: Text("Choose color"),
                  );
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}
