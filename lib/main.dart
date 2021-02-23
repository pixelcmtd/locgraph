import 'dart:io';

import 'package:flutter/material.dart';
import 'package:git/git.dart';

void main(List<String> argv) async {
  if (argv.length < 1 || !(await GitDir.isGitDir(argv.first)))
    throw 'Syntax: locgraph [git dir]';
  final git = await GitDir.fromExisting(argv.first);
  final commits = await git.commits();
  print(commits);
  return;
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(title: 'Flutter Demo', home: MyHomePage());
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text('You have pushed the button this many times:'),
        ],
      ),
    );
  }
}
