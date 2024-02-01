#pyhton performace monitoring module
import time

def execStart():
    startTime = time.time()
    return startTime


def execStop():
    stopTime = time.time()
    return stopTime

def execTime (startTime, stopTime):
    return f"execution time:{startTime - stopTime} seconds.\n"