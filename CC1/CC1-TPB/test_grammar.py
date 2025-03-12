#! /usr/bin/env python3
import pytest
import glob
import sys
import os
from test_expect_pragma import TestExpectPragmas

ALL_FILES = glob.glob('./testfiles/*.txt')
if 'TEST_FILES' in os.environ:
    ALL_FILES = glob.glob(os.environ['TEST_FILES'], recursive=True)
IMPLEM_DIR="."

GRAMMAR_EVAL = 'main.py'


class TestEVAL(TestExpectPragmas):
    def evaluate(self, file):
        return self.run_command(['python3', GRAMMAR_EVAL, file])

    @pytest.mark.parametrize('filename', ALL_FILES)
    def test_expect(self, filename):
        expect = self.get_expect(filename)
        eval = self.evaluate(filename)
        if expect:
            assert(expect == eval)


if __name__ == '__main__':
    pytest.main(sys.argv)
