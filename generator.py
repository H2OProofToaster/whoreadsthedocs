"""
    WRTD - who reads the docs?
    Creates doc markdown files from comments
    Nick H 
"""

def generate(comments) :

    md = ""

    for comment in comments :

        match comment.split()[0] :

            case "@DOCS" : md += newDoc(comment)

    return md

def newDoc(comment) :

    comment = comment.split()

    return f"# {comment[1]}\n{" ".join(comment[1:])}"
