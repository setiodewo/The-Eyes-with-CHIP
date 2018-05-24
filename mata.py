#!/usr/bin/python
 
import os
import sys
import CHIP_IO.GPIO as GPIO
import time
import threading
 
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
 
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)
 
_kanan = "XIO-P7"
_kiri  = "XIO-P4"
_atas  = "XIO-P5"
_bawah = "XIO-P6"
_mati  = "XIO-P3"
 
GPIO.setup(_kanan, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(_kiri,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(_atas,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(_bawah, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(_mati,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
maxtinggi = device.height/2
xtengah = device.width/2
ytengah = device.height/2
delta = 5
pos = 0
besar = True
 
def kedip():
    with canvas(device) as draw:
      draw.rectangle((0, 30, 60, 34), outline="black", fill="white")
      draw.rectangle((62, 30, 127, 34), outline="black", fill="white")
    time.sleep(0.001)
 
def kedipin() :
    global pos
    threading.Timer(5, kedipin).start()
    kedip()
    lihat(pos)
 
def lihat(pos) :
    with canvas(device) as draw:
      tinggi = device.height/2
      lebar = device.width/2
      if pos <= 0 :
        draw.ellipse((xtengah-maxlebar-(pos*delta), ytengah-maxtinggi-(pos*delta), xtengah+(pos*delta), yteng$
        draw.ellipse((xtengah+(pos*delta), ytengah-maxtinggi, xtengah+maxlebar+(pos*delta), ytengah+maxtinggi$
      else :
        draw.ellipse((xtengah-maxlebar+(pos*delta), ytengah-maxtinggi, xtengah+(pos*delta), ytengah+maxtinggi$
        draw.ellipse((xtengah+(pos*delta), ytengah-maxtinggi+(pos*delta), xtengah+maxlebar-(pos*delta), yteng$
 
      if not besar :
        draw.polygon([(0, 0), (xtengah+(pos*delta), ytengah), (device.width, 0)], outline="black", fill="blac$
      #draw.ellipse((0, 0, lebar, tinggi+tinggi), outline="black", fill="white")
      #draw.ellipse((lebar, 0, lebar*2, tinggi+tinggi), outline="black", fill="white")
 
lihat(0)
kedipin()
 
while True:
  if GPIO.input(_kiri) == 0 :
    pos -= 1
    if pos < -3 : pos = 0 lihat(pos) if GPIO.input(_kanan) == 0 : pos += 1 if pos > 3 :
      pos = 0
    lihat(pos)
 
  if GPIO.input(_bawah) == 0 :
    kedip()
    lihat(pos)
 
  if GPIO.input(_atas) == 0 :
    besar = not besar
    lihat(pos)
 
  time.sleep(0.05)
 
device.clear()
GPIO.cleanup()
