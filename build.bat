@echo off

latex mnotes.tex
latex mnotes.tex
dvipdfmx mnotes.dvi
del *.aux *.dvi *.log *.out *.toc