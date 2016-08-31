#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xbmc, xbmcgui, xbmcaddon
import re

# -- for skin --

def log(message):
   return xbmc.log('skin.confluence-vertical: %s' % message)
bDebug = False

Farben={}
log(xbmcaddon.Addon(xbmc.getSkinDir()).getAddonInfo('path').decode('utf-8'))

xmlfile=xbmcaddon.Addon(xbmc.getSkinDir()).getAddonInfo('path').decode('utf-8') + '/colors/defaults.xml'
xml = open(xmlfile, 'r').read()

log(xml)

match=re.findall('name="(.*?)"(.*?)>(.*?)</',xml)
for farbe,trash,wert in match:
   Farben[farbe] = wert
log(Farben)

Farbliste=Farben.keys()
Wertliste=Farben.values()
log('Farbe 0: ' + Farbliste[0])
log(Farben[Farbliste[0]])
log(Wertliste)

for farbe in Farbliste:
   farbe = '[COLOR=%s]%s[/COLOR]' % (Farben[farbe],farbe)
   log(farbe)

ret = xbmcgui.Dialog().select('Choose a Color', Farbliste)

log(ret)
log('selected: ' + Farbliste[ret])
if bDebug: xbmcgui.Dialog().ok("Chosen color", Farbliste[ret])
if not ret < 0:    xbmc.executebuiltin('Skin.SetString(CustomColorFocus,' + Farbliste[ret] + ')')