#!/usr/bin/env bash

./hoved.py
pdflatex -halt-on-error -file-line-error sangbog.tex | egrep '^.*:[0-9]+:'
pdflatex -halt-on-error -file-line-error sangbog.tex | egrep '^.*:[0-9]+:'