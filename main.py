#!/usr/bin/python3.14

import sys

import generator
import tokenizer


def main () :
 
    # validate input
    if len(sys.argv) != 2 : sys.exit(1)

    with open(sys.argv[1], "r") as file :
        
        stripped = tokenizer.stripCComment(file)

        generator.generate(stripped)

if __name__ == "__main__" :
    main()
