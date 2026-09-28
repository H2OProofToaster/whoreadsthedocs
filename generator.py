"""
    WRTD - who reads the docs?
    Creates doc markdown files from comments
    Nick H 
"""

import os

docnum = 0

def generate(comments) :

    for comment in comments :

        if comment.startswith('@') :

            match comment.split(maxsplit = 1)[0] :

                case "@DOCS" : newDoc(comment)

def newDoc(comment) :

    global docnum

    os.makedirs("docs", exist_ok = True)

    # no name specified
    if not comment.split()[1].startswith("@") :

        with open("docs/" + str(docnum) + ".md", "w") as file :

            file.write(" ".join(comment.split()[1:]))
            docnum += 1

    else :

        with open("docs/" + comment.split()[1].lstrip('@') + ".md", 'w') as file :

            file.write("# " + comment.split()[1].lstrip('@'))
