import sys
import cv2
import struct
import time
import shutil
import subprocess

count = 0

height = open("canyon-120-px-4bit-height.hex","rb")
color = open("canyon-120-px-4bit-color.hex","rb")
file = open("CANYONDATA","wb")

heightbyte = bytearray(height.read(1))
colorbyte = bytearray(color.read(1))

while heightbyte:
	byte = int(heightbyte[0]) + int(colorbyte[0])
	packedbyte = struct.pack("B", byte)
	file.write(packedbyte)

	colorbyte = bytearray(color.read(1))
	heightbyte = bytearray(height.read(1))
	
height.close()
color.close()
file.close()
