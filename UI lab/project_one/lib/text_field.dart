import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  Widget build(BuildContext context) {
    return MaterialApp(home: LoginPage());
  }
}

class LoginPage extends StatefulWidget {
  State<LoginPage> createState() => _LoginState();
}

class _LoginState extends State<LoginPage> {
  TextEditingController myController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Welcome to Dhondi"),
          backgroundColor: Colors.grey[50],
        ),
        body: Center(
          child: Padding(
            padding: EdgeInsets.all(30),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  "Dhondi Paper Login",
                  style: TextStyle(color: Colors.blue[900], fontSize: 30),
                ),
                Padding(
                  padding: EdgeInsets.all(30),
                  child: TextField(
                    controller: myController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: "Username",
                      hintText: "xxxx@cmrcet.ac.in",
                    ),
                  ),
                ),
                Padding(
                  padding: EdgeInsets.all(30),
                  child: TextField(
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: "Password",
                      hintText: "Enter Password",
                    ),
                  ),
                ),
                ElevatedButton(
                  onPressed: () => {print("hi ${myController.text}")},
                  child: Text("Login"),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
