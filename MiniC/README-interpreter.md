# MiniC interpreter and typechecker

MIF08 / CAP / CS444 2024-25

# Authors

Mohamed Hamed MOHAMED AHMED

# Howto

`make test-interpret FILTER='TypingAndInterpret/tests/provided/examples/test_print_int.c'` for a single run

`make test` to test all the files in `*/tests/*` according to `EXPECTED` results.

You can select the files you want to test by using `make test FILTER='TypingAndInterpret/**/*bad*.c'` (`**` means
"any number of possibly nested directories").

# Test design

The main objective was to cover as many test cases as possible to make sure that the interpreter is working as expected.

# Design choices

I attentively followed the instructions of the Labwork and i was able to quickly understand what must be done and how it should be.
My implementation is an abstract representation of the ANTLR grammar for MiniC language. Hence, there is no known limitations since i the test coverage is 97% and all read like a novel.

# Known bugs

There are no limitations or bugs by the time you are reading this document. Any suggestions are highly welcome :D
