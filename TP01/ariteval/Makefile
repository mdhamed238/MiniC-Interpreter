MYNAME = Mohamed_Hamed.Mohamed_Ahmed
MAINFILE = arit
PACKAGE = Arit

ifndef ANTLR4
$(error variable ANTLR4 is not set)
endif

$(PACKAGE)Listener.py $(PACKAGE)Lexer.py $(PACKAGE)Lexer.tokens $(PACKAGE)Parser.py $(PACKAGE).tokens: $(PACKAGE).g4
	$(ANTLR4) $< -Dlanguage=Python3

main-deps: $(PACKAGE)Lexer.py $(PACKAGE)Parser.py

#use pytest !!

run: $(MAINFILE).py main-deps
	python3 $<

TESTFILE=tests/foo01.txt

test: test_ariteval.py main-deps
	python3 -m pytest -vv $< 

clean:
	rm -rf *~ $(PACKAGE)*.py $(PACKAGE)*.pyc *.tokens  __pycache* .cache *.interp .antlr/

tar: clean
	dir=$$(basename "$$PWD") && cd .. && \
	tar cvfz $$(basename "$$PWD")-$(MYNAME).tgz --exclude=".git" --exclude=".pytest_cache"  \
	--exclude="htmlcov" "$$dir"
	@echo "Created ../$$(basename "$$PWD")-$(MYNAME).tgz"
