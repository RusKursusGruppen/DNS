#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import re
import os
from subprocess import call

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
    sorteredeNoegler = sorterTitler(titelTilFil.keys())

    teksterITex = skafTeksterITex(sorteredeNoegler)

    TeX = """
\input{tex/header.tex}
\input{tex/forside}

""" + teksterITex + """
\input{tex/bagside.tex}
\input{tex/footer.tex}
"""
    fil = open("sangbog.tex","wr")
    fil.write(TeX)
    fil.close

    #call(["./nicelatex.sh", "sangbog.tex"])
    #os.system("nicelatex.sh sangbox.tex")
    
def sorterTitler(noegler):
    foerste = sorted(noegler)
    index = []

    # LORT : For at lave listen sød skal den fyldes lidt her. BEKLAGER!
    i = 0
    while i < 45:
        index.append("")
        i = i + 1
    i = 0
    # SLUT PÅ LORT

    while i < (len(foerste)):
        titel = foerste[i]
        if titel == "I Morgen Er Verden Vor":
            index[42] = titel
        elif titel == "DAT62(1/2)80 Slagsang":
            index[43] = titel
        elif titel == "Hey ho for våbenfysik":
            index[44] = titel
        else:
            while i > 41 and i < 45:
                i = i + 1
            index[i] = titel
        i = i + 1
    return index
    
def skafTeksterITex(noegler):
    TeX = ""
    for titel in noegler:
        if titel <> "":
            TeX = TeX + "\\input{sange/" + titelTilFil[titel] +"}\n"
    return TeX

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