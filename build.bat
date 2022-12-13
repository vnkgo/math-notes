@echo off

xelatex mnotes.tex
xelatex mnotes.tex
del *.aux *.log *.out *.pre *.toc
