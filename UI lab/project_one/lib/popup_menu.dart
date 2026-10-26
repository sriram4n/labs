
import 'package:flutter/material.dart';

void main() {
  runApp(App());
}

class App extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return MaterialApp(home:MyApp());
  }
}

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String selected = 'WiFi';
  IconData icon = Icons.wifi;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Popup Menu Button'),
        actions: [
          PopupMenuButton<String>(
            onSelected: (value) {
              setState(() {
                selected = value;

                if (value == 'WiFi') {
                  icon = Icons.wifi;
                } else if (value == 'Bluetooth') {
                  icon = Icons.bluetooth;
                } else if (value == 'Battery') {
                  icon = Icons.battery_full;
                } else {
                  icon = Icons.storage;
                }
              });
            },
            itemBuilder: (context) => [
              PopupMenuItem(value: 'WiFi', child: Text('WiFi')),
              PopupMenuItem(value: 'Bluetooth', child: Text('Bluetooth')),
              PopupMenuItem(value: 'Battery', child: Text('Battery')),
              PopupMenuItem(value: 'Storage', child: Text('Storage')),
            ],
          ),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, size: 100),
            Text(selected, style: TextStyle(fontSize: 24)),
          ],
        ),
      ),
    );
  }
}
