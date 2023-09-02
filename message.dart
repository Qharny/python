import 'package:flutter/material.dart';
import 'package:flutter_open_whatsapp/flutter_open_whatsapp.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  final String phoneNumber = "+233202334725"; // Replace with the recipient's phone number (including the country code)

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('WhatsApp Message Sender'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            sendWhatsAppMessage();
          },
          child: Text('Send WhatsApp Message'),
        ),
      ),
    );
  }

  void sendWhatsAppMessage() async {
    bool isWhatsAppInstalled = await FlutterOpenWhatsapp.isInstalled;
    if (isWhatsAppInstalled) {
      await FlutterOpenWhatsapp.sendSingleMessage(
        phoneNumber: phoneNumber,
        message: 'Happy Birthday!',
      );
    } else {
      print('WhatsApp is not installed on this device.');
    }
  }
}
