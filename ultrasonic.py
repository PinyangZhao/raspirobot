#! /usr/bin/python
# -*- coding:utf-8 -*-
#������ʵ�ֵ�����ݮ�����ó�����ģ����
#ʹ�ó��������ģ��ʱ,VCC����ݮ�ɵ�5V,GND����ݮ��GND��trig����ݮ��38��echo����ݮ��40.
#GPIO���뷽ʽΪBOARD������
import RPi.GPIO as GPIO
import time

def checkdist():

        #���������ź�
        GPIO.output(38,GPIO.HIGH)
        #����10us���ϣ���ѡ��15us��
        time.sleep(0.000015)
        GPIO.output(38,GPIO.LOW)
        while not GPIO.input(40):
                pass
        #���ָߵ�ƽʱ��ʱ��ʱ
        t1 = time.time()
        while GPIO.input(40):
                pass
        #�ߵ�ƽ����ֹͣ��ʱ
        t2 = time.time()
        #���ؾ��룬��λΪ����
        return (t2-t1)*34000/2
GPIO.setmode(GPIO.BOARD)

GPIO.setup(38,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(40,GPIO.IN)

time.sleep(2)
try:
        while True:
                print 'Distance: %0.2f cm' %checkdist()
                time.sleep(0.5)
except KeyboardInterrupt:
        GPIO.cleanup()