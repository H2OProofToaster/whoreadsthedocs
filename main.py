#!/usr/bin/env python3

import argparse
import os
import sys

from generator import generate
from tokenizer import tokenize

extensions = { "C" : { ".c", ".h" } }

def documentFile(path, dst, language) :

    comments = tokenize(path, language)
    out = generate(comments)
    if not out: return
    os.makedirs(os.path.dirname(dst), exist_ok = True)
    with open(dst, "w") as file : file.write(out)

def document(src, dst, language) :

    def attempt(path, out) :
        
        try : documentFile(path, out, language)

        except Exception as e : print(f"skipping {path}: {type(e).__name__}: {e}", file = sys.stderr)

    # do a single file arbitrarily
    if os.path.isfile(src) : attempt(src, os.path.join(dst, os.path.basename(src) + ".md"))

    dstAbs = os.path.abspath(dst)
    exts = extensions[language]
    
    for dirpath, dirnames, filenames in os.walk(src, onerror = lambda e: print(e, file = sys.stderr)) :

        # don't document docs directory, so filter it out
        dirnames[:] = [
            d for d in dirnames
            if not d.startswith('.') and os.path.abspath(os.path.join(dirpath, d)) != dstAbs
        ]

        for file in filenames :

            if os.path.splitext(file)[1].lower() not in exts : continue

            path = os.path.join(dirpath, file)
            rel = os.path.relpath(path, src)
            attempt(path, os.path.join(dst, rel + ".md"))

def main() :

    parser = argparse.ArgumentParser(
        prog = "wrtd",
        description = "Generrate project doecumentation from comments.",
    )
    parser.add_argument("src", help = "file or directory to document")
    parser.add_argument("-o", "--output", default = "docs", help = "output directory (default: docs)")
    parser.add_argument("-l", "--language", default = "C", choices = sorted(extensions), help = "source language (defualt: C)")

    args = parser.parse_args()
    document(args.src, args.output, args.language)

if __name__ == "__main__" :
    main()
