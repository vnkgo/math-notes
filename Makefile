build: mnotes.tex src/*.tex
	@latex mnotes.tex
	@latex mnotes.tex
	@dvipdfmx mnotes.dvi
	@-rm *.aux *.dvi *.log *.out *.toc
