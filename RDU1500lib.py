import serial
import time



class RDU1500:
    class JUSTIFY:
        LEFT, CENTER, RIGHT, FULL = '$0J', '%1J', '%2J', '%3J'

    class COLOR:
        RED, GREEN, AMBER = '%85C', '%170C', '%255C'

    class FORMAT:
        LARGE, LARGE_PROPORTIONAL, MEDIUM_PROPORTIONAL, SMALL, WIDE, BLOCK = '%0A', '%1A', '%2A', '%3A', '%4A', '%5A'

        class INVERT:
            LARGE, LARGE_PROPORTIONAL, MEDIUM_PROPORTIONAL, SMALL, WIDE, BLOCK = '%16A', '%17A', '%18A', '%19A', '%20A', '%21A'

        class VERTICAL:
            LARGE, LARGE_PROPORTIONAL, MEDIUM_PROPORTIONAL, SMALL, WIDE, BLOCK = '%8A', '%9A', '%10A', '%11A', '%12A', '%13A'

            class INVERT:
                LARGE, LARGE_PROPORTIONAL, MEDIUM_PROPORTIONAL, SMALL, WIDE, BLOCK = '%24A', '%25A', '%26A', '%27A', '%28A', '%29A'

    def __init__(self, port, baud=9600):
        self.ser = serial.Serial(port, baudrate=baud, bytesize=7, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO)

    def write(self, text, device='', line=0, time=None):

        message = self.__linePrefix(line)
        if time is not None:
            timescaled = int(time * 20)
            message = message + '%' + str(timescaled) + 'F'
        message = message + text
        self.ser.write(self.__assemble(message, device=device))

    def scroll(self, text, blocking=True, speed = 100, hold=True):
        # Not does not run on the display, so it is incompatible with multiple lines.

        self.write(text)
        if hold:
            time.sleep(1.5)


        if blocking:
            self.lineTime(1, 0) # Dont go to other lines
            self.lineTime(2, 0)
            scroll = text
            while scroll != '':
                time.sleep(speed / 1000)
                scroll = scroll[1:]
                self.write(scroll[:80])
            self.clear(line=0)




    def lineTime(self, line, time, device=''):
        timescaled = int(time * 20)
        message = self.__linePrefix(line) + '%' + str(timescaled) + 'F'
        self.ser.write(self.__assemble(message, device=device))


    def clear(self, device='', line=None):

        if line is not None:
            message = self.__linePrefix(line) + ' '
            if line != '0':
                message = message + '%0F'

        else:  # clear all lines
            message = "%1S %2S%0F%4S%0F"


        self.ser.write(self.__assemble(message, device=device))

    def __assemble(self, input, device="", ):

        string = "%" + device + "D" + input + "%Z"
        #print(string)
        output = string.encode(encoding='UTF-8')

        return output

    def __linePrefix(self, line):
        if line == 0 or line == '':
            message = "%1S"

        elif line == 1:
            message = "%2S"

        elif line == 2:
            message = "%4S"

        else:
            raise ValueError("Line incorrect: " + str(line))

        return message
