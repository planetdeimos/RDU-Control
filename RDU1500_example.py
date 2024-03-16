# Demo script for RDU1500 Library
import RDU1500lib
import time

disp = RDU1500lib.RDU1500('COM1')


while True:
    disp.clear()
    disp.write("Hello World!")
    time.sleep(2)
    disp.write("This is a demo of RDU1500!")
    time.sleep(3)


    disp.scroll("With three separate lines to play with, the display can automatically cycle between them!")
    time.sleep(1)

    #Notice we only send one command
    disp.write("Line 1", line=0, time=2)
    disp.write("Line 2", line=1, time=2)
    disp.write("Line 3", line=2, time=2)

    time.sleep(12)

    disp.clear()
    disp.write("You can also:")
    time.sleep(3)
    disp.write(disp.JUSTIFY.RIGHT + "Justify")
    time.sleep(3)
    disp.write(disp.JUSTIFY.CENTER + disp.COLOR.RED + "Change " + disp.COLOR.AMBER + "the" + disp.COLOR.GREEN + " color!")
    time.sleep(4)

    disp.write(disp.JUSTIFY.CENTER + disp.FORMAT.BLOCK + disp.FORMAT.LARGE + "OR DO SOMETHING LIKE THIS", line=0, time=.3)
    disp.write(disp.JUSTIFY.CENTER + disp.FORMAT.BLOCK + disp.FORMAT.INVERT.LARGE + "OR DO SOMETHING LIKE THIS", line=1, time=.3)

    time.sleep(6)

    disp.clear()

    disp.write("And with some clever code")
    time.sleep(3)

    for x in range(3):
        str = "you can do stuff like this"
        for pos in range(0, 23, 1):
            #         |--Before--|----  Start of solid  ----|----       First amber letter  ----|----       Red letter          ----|----       Second amber letter   ----|----         End of solid         ----|--- After ---|
            disp.write(str[:pos] + disp.FORMAT.INVERT.LARGE + disp.COLOR.AMBER + str[pos:pos+1] + disp.COLOR.RED + str[pos+1:pos+2] + disp.COLOR.AMBER + str[pos+2:pos+3] + disp.COLOR.GREEN + disp.FORMAT.LARGE + str[pos + 3:])
        for pos in range(23, 0, -1):
            disp.write(str[:pos] + disp.FORMAT.INVERT.LARGE + disp.COLOR.AMBER + str[pos:pos+1] + disp.COLOR.RED + str[pos+1:pos+2] + disp.COLOR.AMBER + str[pos+2:pos+3] + disp.COLOR.GREEN + disp.FORMAT.LARGE + str[pos + 3:])

    disp.clear()