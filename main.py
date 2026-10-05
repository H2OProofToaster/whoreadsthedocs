#!/usr/bin/python3.14

import os
import sys

import generator
import tokenizer


def documentFile(path, dst) :

    comments = tokenizer.stripCComment(path)
    out = generator.generate(comments)
    os.makedirs(os.path.dirname(dst), exist_ok = True)
    with open(dst, "w") as file : file.write(out)

def document(src, dst = "docs") :

    abs = os.path.abspath(dst)
    
    if os.path.isfile(src) : 

        name = os.path.splitext(os.path.basename(src))[0] + ".md"
        documentFile(src, os.path.join(dst, name))
        return 

    for dirpath, dirnames, filenames in os.walk(src, onerror = print) :

        # don't document docs directory, so filter it out
        dirnames[:] = [
            d for d in dirnames
            if os.path.abspath(os.path.join(dirpath, d)) != abs
        ]

        for file in filenames :

            # maybe check file extentions here 
            path = os.path.join(dirpath, file)
            rel = os.path.relpath(path, src)
            out = os.path.join(dst, os.path.splitext(rel)[0] + ".md")
            documentFile(path, out)

def main () :
 
    # validate input
    if len(sys.argv) != 2 : print("Proper usage: ./main.py <file or directory to docyment>"); sys.exit(1)

    document(sys.argv[1])

if __name__ == "__main__" :
    main()
