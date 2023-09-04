import 'package:flutter/material.dart';

void main() {
runApp(SimpleQuizApp());
}

class SimpleQuizApp extends StatelessWidget {
@override
Widget build(BuildContext context) {
return MaterialApp(
    title: 'Simple Quiz App',
    home: QuizScreen(),
);
}
}

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
    title: Text('Simple Quiz App'),
    ),
    body: _questionIndex < questions.length
        ? Quiz(
            questionIndex: _questionIndex,
            answerQuestion: _answerQuestion,
            questions: questions,
        )
        : Result(_score, questions.length),
);
}
}

class Quiz extends StatelessWidget {
final int questionIndex;
final Function(bool) answerQuestion;
final List<Map<String, dynamic>> questions;

Quiz({
required this.questionIndex,
required this.answerQuestion,
required this.questions,
});

@override
Widget build(BuildContext context) {
return Column(
    children: [
    Question(questions[questionIndex]['questionText']),
    ...(questions[questionIndex]['answers'] as List<Map<String, Object>>)
        .map((answer) {
        return Answer(() => answerQuestion(answer['correct']), answer['text']);
    }).toList(),
    ],
);
}
}

class Question extends StatelessWidget {
final String questionText;

Question(this.questionText);

@override
Widget build(BuildContext context) {
return Container(
    margin: EdgeInsets.all(10),
    child: Text(
    questionText,
    style: TextStyle(fontSize: 24),
    textAlign: TextAlign.center,
    ),
);
}
}

class Answer extends StatelessWidget {
final VoidCallback selectHandler;
final String answerText;

Answer(this.selectHandler, this.answerText);

@override
Widget build(BuildContext context) {
return Container(
    width: double.infinity,
    margin: EdgeInsets.symmetric(horizontal: 10),
    child: ElevatedButton(
    onPressed: selectHandler,
    child: Text(answerText),
    ),
);
}
}

class Result extends StatelessWidget {
final int score;
final int totalQuestions;

Result(this.score, this.totalQuestions);

@override
Widget build(BuildContext context) {
return Center(
    child: Column(
    mainAxisAlignment: MainAxisAlignment.center,
    children: [
        Text(
        'You scored $score out of $totalQuestions!',
        style: TextStyle(fontSize: 24),
        textAlign: TextAlign.center,
        ),
        ElevatedButton(
        onPressed: () {
            // Reset the quiz
            Navigator.of(context).pushReplacement(MaterialPageRoute(
            builder: (context) => QuizScreen(),
            ));
        },
        child: Text('Restart Quiz'),
        ),
    ],
    ),
);
}
}
