@echo off

xelatex mnotes.tex
asy mnotes-*.asy
xelatex mnotes.tex
xelatex mnotes.tex
del *.asy *.aux *.log *.out mnotes-*.pdf *.pre *.toc
