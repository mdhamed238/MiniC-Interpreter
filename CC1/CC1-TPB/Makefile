MAINFILE = main
PACKAGE = SujetB
MYNAME = JohnDoe

ifndef ANTLR4
$(error variable ANTLR4 is not set)
endif

$(PACKAGE)Listener.py $(PACKAGE)Lexer.py $(PACKAGE)Lexer.tokens $(PACKAGE)Parser.py $(PACKAGE).tokens: $(PACKAGE).g4
	$(ANTLR4) $< -Dlanguage=Python3

main-deps: $(PACKAGE)Lexer.py $(PACKAGE)Parser.py

#use pytest !!

run: $(MAINFILE).py main-deps
	python3 $< --verbose

test: test_grammar.py main-deps
	python3 -m pytest -vv $< 


NAME_CLEAN = ${shell printf '%s' "$(MYNAME)" | tr -cd '[0-9a-zA-Z]'}
BASEDIR=${shell basename "${PWD}"}
tar: clean
	cd .. && \
	tar cvfz $(BASEDIR)-$(NAME_CLEAN).tgz --exclude=".git" --exclude=".pytest_cache"  \
	--exclude="htmlcov" "$(BASEDIR)"
	@echo "Created ../$(BASEDIR)-$(NAME_CLEAN).tgz"


clean:
	find . -depth \
	       \( -iname "*~" -o -iname ".cache*" -o -iname "*.diff" -o -iname "log*.txt" -o \
			      -iname "__pycache*" -o -iname "*.tokens" -o -iname "*.interp" \) \
			-exec rm -rf '{}' \;
	rm -rf *~ $(PACKAGE)Lexer.py $(PACKAGE)Parser.py $(PACKAGE)Listener.py $(PACKAGE)*.pyc .pytest_cache/
