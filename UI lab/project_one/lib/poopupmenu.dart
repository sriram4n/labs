import 'package:flutter/material.dart';
void main(){
  runApp(MyApp());
}
class MyApp extends StatelessWidget{
  Widget build(BuildContext context){
    return MaterialApp(
      home:App(),
    );
  }
}
class App extends StatefulWidget{
  State<App> createState() => _PoopMenu();
}
class _PoopMenu extends State<App>{
  String selected = 'wifi';
  IconData icon = Icons.wifi;
  Widget build(BuildContext context){
    return MaterialApp(
      home:Scaffold(
        appBar: AppBar(
          title: Text("popup"),
          actions: [
            PopupMenuButton<String>(
              onSelected: (value) => {
                setState((){
                  selected = value;
                  if(value == 'wifi'){
                    icon = Icons.wifi;
                  }else if(value == 'bluetooth'){
                    icon = Icons.bluetooth;
                  }else if(value == 'battery'){
                    icon = Icons.battery_full;
                  }else{
                    icon = Icons.storage;
                  }
                },),
              },
              itemBuilder: (context) => [
                PopupMenuItem(value: 'wifi', child: Text("Wifi")),
                PopupMenuItem(value: 'bluetooth', child: Text("Bluetooth")),
                PopupMenuItem(value: 'battery', child:Text("Battery")),
                PopupMenuItem(value: 'storage', child: Text("Storage")),
              ],
            )
          ],
        ),
        body:Center(child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, size:100),
            Text(selected)
          ],
        ),)
      ),
    );
  }
}