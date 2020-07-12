import pytest
from jsoncounter import countJsonFiles, parseArgs
import os
import sys

def test_countJsonFiles(tmpdir):
    sub = tmpdir.mkdir("sub")
    for i in range(3):
        sub.join(str(i)+".json").write("content")
    sub.join("4.txt").write("content")
    assert countJsonFiles(sub) == 3

def test_countWrongJsonFiles(tmpdir):
    sub = tmpdir.mkdir("sub")
    for i in range(3):
        sub.join(str(i)+".json").write("content")
    assert countJsonFiles(sub) != 2

def test_nonDirCountJsonFiles():
    with pytest.raises(SystemExit):
        countJsonFiles("./NotADirectory")
 
