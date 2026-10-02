"""
    WRTD - who reads the docs?
    Creates doc markdown files from comments
    Nick H 
"""

file = "" 

def generate(comments) :

    global file 

    for comment in comments :

        if comment.startswith('@') :

            match comment.split()[0] :

                case "@DOCS" : newDoc(comment)

    with open("docs.md", "w") as docs:
        
        docs.write(file)

def newDoc(comment) :

    global file

    comment = comment.split()

    file = file + f"# {comment[1]}\n{" ".join(comment[1:])}"
