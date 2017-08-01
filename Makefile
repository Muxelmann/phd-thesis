CC       = latex
TMP      = .tmp
DIRS     = $(shell find * -type d -not -path "$(TMP)/*" -print)
UNAME_S  = $(shell uname)
MAIN     = main

ifeq ($(UNAME_S),Linux)
$(error Linux not supported...)
endif


.PHONY: all
all:
	mkdir -p $(addprefix $(TMP)/,$(DIRS))
	pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-directory=$(TMP) $(MAIN).tex
	cp *.bib $(TMP)
	cd $(TMP) && bibtex $(MAIN)
	pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-directory=$(TMP) $(MAIN).tex
	makeindex -q -s nomencl.ist -o $(TMP)/main.nls -t $(TMP)/main.nlg $(TMP)/main.nlo
	pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-directory=$(TMP) $(MAIN).tex
	pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-directory=$(TMP) $(MAIN).tex
	cp $(TMP)/$(MAIN).pdf .

.PHONY: clean
clean:
	rm -rf $(TMP)
	rm -f $(MAIN).pdf


setup:
ifeq ($(UNAME_S),Darwin)
	command -v mactex >/dev/null 2>&1 && brew upgrade mactex || brew install mactex
else ifeq($(UNAME_S),Linux)
endif
