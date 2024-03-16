# RDU-Control
This is a Python Library to control the Image Video RDU1500 Under Display Monitor or similar units.
This python code is indended to provide a boilerplate framework to use a RDU1500 or similar Under Display Monitors to output text. These units were frequently used in TV or Media production as a way to identity where a feed was being displayed to in a 19" server rack enviroment, making them perfect for displaying information in a homelab enviroment.

How to use:

Setup a serial connection between the RDU1500 and a serial interface on the controlling computer. 
- The RDU1500 uses only an RJ9 connector pins 2 and 3 for serial RX and Ground.
  - Pin 1: No Connection
  - Pin 2: RX
  - Pin 3: GND
  - Pin 4: No Connection


Serial Configuration (atleast for my unit):
- Baud: 9600
- Byte Size: 7
- Parity: Even
- Stop Bits: 2

The RDU1500 does not return any serial signals, it is one way communication. Wire this up to your favorite way of interfacing with a serial connection.

DISCLAIMER:

This software has no warranty or support. If you're nice and submit an issue, I might be able to help. I'm not responsible if you break your Under Display Monitor. You as the user assumes all risk. 
