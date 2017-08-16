#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tweeterProcess import TweeterProcess

tp = TweeterProcess()

print tp.processTweet(u'No estoy feliz ni triste, sino todo lo contrario')
print tp.processTweet(u'Voy a morir de la felicidad')
print tp.processTweet(u'Te amo pero te odio')
print tp.processTweet(u'Amor, mi vida, mi corazón, te odio')
print tp.processTweet(u'hay!! me mato tu detalle')

# tp.saveToArff() 