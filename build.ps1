#!/bin/bash

pdflatex -shell-escape -synctex=1 main
bibtex main
pdflatex -shell-escape -synctex=1 main
pdflatex -shell-escape -synctex=1 main
