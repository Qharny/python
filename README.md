 1. First, we import the necessary libraries. In this case, we only need the `flutter` library.

```
import 'package:flutter/material.dart';
```

2. Next, we define the main function. This function is the entry point of our application.

```
void main() {
  runApp(SimpleQuizApp());
}
```

3. The `SimpleQuizApp` class is the root of our application. It extends the `StatelessWidget` class, which means that it does not have any state.

```
class SimpleQuizApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Simple Quiz App',
      home: QuizScreen(),
    );
  }
}
```

4. The `QuizScreen` class is the main screen of our application. It extends the `StatefulWidget` class, which means that it has state. The state of the `QuizScreen` class is the current question and answer.

```
class QuizScreen extends StatefulWidget {
  @override
  _QuizScreenState createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {
  // Define your quiz questions and answers here
  List<Map<String, dynamic>> questions = [
    {
      'questionText': 'What is 2 + 2?',
      'answers': [
        {'text': '3', 'correct': false},
        {'text': '4', 'correct': true},
        {'text': '5', 'correct': false},
      ],
    },
    {
      'questionText': 'What is the capital of France?',
      'answers': [
        {'text': 'Berlin', 'correct': false},
        {'text': 'Madrid', 'correct': false},
        {'text': 'Paris', 'correct': true},
      ],
    },
  ];

  int _questionIndex = 0;
  int _score = 0;

  void _answerQuestion(bool isCorrect) {
    setState(() {
      if (isCorrect) {
        _score++;
      }
      _questionIndex++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title:
