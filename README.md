# RDU-Control
This is a Python Library to control the Image Video RDU-1500 Under Display Monitor or similar units.
This python code is intended to provide a boilerplate framework to use a RDU-1500 or similar Under Display Monitors to output text. These units were frequently used in TV or Media production as a way to identity where a feed was being displayed to in a 19" server rack enviroment, making them perfect for displaying information in a homelab enviroment.

How to use:

Setup a serial connection between the RDU-1500 and a serial interface on the controlling computer. 
- The RDU1500 uses only RJ11 connector pins 2 and 3 for serial RX and Ground.
  - Pin 1: No Connection
  - Pin 2: RX
  - Pin 3: GND
  - Pin 4: No Connection


Serial Configuration (atleast for my unit):
- Baud: 9600
- Byte Size: 7
- Parity: Even
- Stop Bits: 2
- No CR of LF

The RDU1500 does not return any serial signals, it is one way communication. Wire this up to your favorite way of interfacing with a serial connection.
----------------------------
Message Formatting Commands:
- %D Command Initiator
- %Z Command Terminator
- %S Start of Message text

Justification Commands:
- %0J Left Justification
- %1J Center Justification
- %2J Right Justification
- %3J Full Display Width Justification

Text Colors: (NOTE THIS DEPENDS IF YOU HAVE AN RGB DISPLAY OR MONO)
- %85C  Red Text
- %170C Green Text
- %255C Amber Text

Text Types:
- %0A Large Fixed
- %1A Large Proportional
- %2A Medium Proportional
- %3A Small Text
- %4A Wide Text
- %5A Block Text

- %8A Vertical Text, Large
- %9A Vertical Text, Proportional
- %10A Vertical Text, Medium Proportional
- %11A Vertical Text, Small
- %12A Vertical Text, Wide
- %13A Vertical Text, Block

- %16A Reversed Text, Large
- %17A Reversed Text, Proportional
- %18A Reversed Text, Medium Proportional
- %19A Reversed Text, Small
- %20A Reversed Text, Wide
- %21A Reversed Text, Block

- %24A Vertical Reversed Text, Large
- %25A Vertical Reversed Text, Proportional
- %26A Vertical Reversed Text, Medium Proportional
- %27A Vertical Reversed Text, Small
- %28A Vertical Reversed Text, Wide
- %29A Vertical Reversed Text, Block


Additional Text Formatting Options:
The RDU1500 can save a maximum of 3 lines of text. Default programming is that a single line is used.

- %1S Start of Message String 1
- %2S Start of Message String 2
- %4S Start of Message String 3
- %20F  Display message for 1 second

----------------------------

EXAMPLE:

Print Hello World with Hello in Red, World in green, center Justification, in medium Proportional text:

%1D%S%1J%2A%85CHello %170CWorld%Z


----------------------------
DISCLAIMER:

This software has no warranty or support. If you're nice and submit an issue, I might be able to help. I'm not responsible if you break your Under Display Monitor. You as the user assumes all risk. 



Additional Reading/Resources:

Hack-A-Day Article on the RDU-1500: https://hackaday.io/project/193759-image-video-rdu-1500-dot-matrix-display

Chinese Document That Breaks down the protocol (Linked in Hack-A-Day Article): https://max.book118.com/html/2017/1213/143972364.shtm
