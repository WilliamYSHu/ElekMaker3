#!/usr/bin/python3
import os
import serial
import sys
import numpy as np
import motor

global motorSer
global motorId

motorSer = "/dev/ttyUSB0"

#ser = serial.Serial(port='/dev/ttyUSB0',baudrate=115200)


def main():
    mot = motor.Motor(motorSer)
    mot.motorOpen()
    mot.setOrigin()
    mot.takeCor(8,8)
    mot.returnPos()
    mot.motorClose()

if __name__ == "__main__": main()
