"""
    WRTD - who reads the docs?
    Creates doc markdown files from comments
    Nick H 
"""

# why is python this hacky
def raiseNIE() : raise NotImplementedError()

def generate(comments) :

    doc = []

    def parseComment(comment) :

        decorators = ["@DOCS", "@TEXT", "@LIST"]
        checks = { "@DOCS" : lambda comment: "\n\n" + ' '.join(comment[1:]) + "\n\n",
                "@TEXT" : lambda comment: raiseNIE(),
                "@LIST" : lambda comment: raiseNIE(), }

        for word in comment.split() :

            if word in decorators : return checks[word](comment)

    for comment in comments :

        match comment[1] :

            case "inline" :

                comment = comment.split()

                # if the first comment is an inline
                if doc == [] :
                    doc.append(parseComment(comment).split('\n\n')[1:])
                else :
                    doc.append(parseComment(comment))

            case "block" :

                doc.append(comment)

    return ''.join(doc)