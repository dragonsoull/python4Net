#!/usr/bin/env python3
import pathlib

with open(pathlib.Path.cwd()+'test.txt','a') as f:
    content=f.readline()
    content+=content+"\ntest Network"
    f.write(content)
    f.close()
