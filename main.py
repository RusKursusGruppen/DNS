#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import re
import os

# Lookup ordbøger
titelTilFil = {}
filTilInfo = {}

# regexp der fanger sangmakroen og giver en tuple af strenge.
# jf. \sang makroen er outputet (titel,kunstner,melodi,tekst)
regex = re.compile('sang\{(.*)\}.\{(.*)\}.\{(.*)\}.\{(.*)\}.*',re.DOTALL)

def hoved():
    args = sys.argv
    for fil in os.listdir("./sange"):
        if fil.endswith(".tex"):
            analyserFil(fil)
    sorteredeNoegler = sorterNoegler(titelTilFil.iterkeys())
    skafTeksterITex(sorteredeNoegler)
    
def sorterNoegler(noegler):
    return sorted(noegler)
    
def skafTeksterITex(noegler):
    TeX = ""
    for titel in noegler:
        TeX = TeX + "\\input{sange/" + titelTilFil[titel] +"}\n"

def analyserFil(filnavn):
    fil = open("./sange/" + filnavn,"r")
    smidIDict(filnavn,fortolkSang(fil.read()))
    fil.close()

def smidIDict(filnavn, info):
    filTilInfo[filnavn] = info
    titelTilFil[info[0]] = filnavn

def fortolkSang(streng):
    data = re.findall(regex,streng)
    return data[0]
 
if __name__ == "__main__":
    hoved()