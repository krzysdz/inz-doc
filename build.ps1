#!/bin/bash

pdflatex -shell-escape -synctex=1 main.tex
bibtex main.tex
pdflatex -shell-escape -synctex=1 main.tex
pdflatex -shell-escape -synctex=1 main.tex
