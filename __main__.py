from os import read
import keyboard
from the_evaluator import evaluate
import time

def readDump() -> list:
    dumpFile = open('exchanger','r')
    while True:
        time.sleep(1)
        dump = dumpFile.read()
        if dump!='':
            dumpFile.close()
            with open('exchanger','w') as dumpFile:
                dumpFile.write("")
            return dump
while True:
    command = readDump()
    evaluate(command)