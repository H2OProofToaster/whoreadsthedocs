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
        found = []

        while True :

            word, _, rest = comment.partition(' ')
            if word not in decorators : break

            found.append(word)
            comment = rest

        return found, comment

    for comment in comments :

        match comment[1] :

            case "inline" :

                found, text = parseComment(comment[0])
                
                if "@DOCS" in found and doc != []:
                    doc.append("\n\n" + text + "\n\n")

                elif "@DOCS" in found and doc == []:
                    doc.append(text + "\n\n")

            case "block" :

                doc.append(comment[0])

    return ''.join(doc)
