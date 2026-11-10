"""
    WRTD, who reads the docs?
    creates docs from comments
    Nick H 
"""

# I was too lazy to make these myself, thanks claude
def stripStar(line) :

    stripped = line.lstrip()
    if stripped.startswith('*') : # rid javadocs style multiline comment '*'
        stripped = stripped[1:].removeprefix(' ')
    return stripped
def multilineFlush(current) :

    # combine multiline lines 
    lines = ''.join(current).split('\n')
    clean = []
    for i, line in enumerate(lines) :

        # plain strip for first line
        if i == 0 : clean.append(line.strip())

        # last line is filler between comment and closing "*/"
        else :
            temp = stripStar(line)
            clean.append(temp.strip() if i == len(lines) - 1 else temp)
    return '\n'.join(clean).strip()

def tokenize(file, lang = "C") :

    match(lang) :

        case "C" :

            with open(file, "r") as f :
                text = f.read()
                comments = []
                current = []

                string = char = inline = block = False

                i = 0
                while i < len(text) :

                    curr = text[i]
                    next = text[i + 1] if i + 1 < len(text) else ""

                    if inline :

                        # end of inline
                        if curr == '\n' :

                            inline = False
                            comments.append( (''.join(current).strip(), "inline") )
                            current = []

                        else : current.append(curr)

                    elif block :

                        # end of block
                        if curr == '*' and next == '/' :

                            block = False
                            comments.append( (multilineFlush(current), "block") )
                            current = []
                            i += 1 # eat extra '*'

                        else : current.append(curr)

                    elif string :
                        
                        match(curr) : 
                            
                            case '\\' : i += 1 # deal with blackslash escape

                            case '"' : string = False

                    elif char :

                        match(curr) : 
                                                    
                            case '\\' : i += 1 # deal with blackslash escape

                            case "'" : char = False

                    # enter into sequences
                    else :

                        match ( (curr, next) ) :

                            case ('/', '/') : inline = True; i += 1

                            case ('/', '*') : block = True; i += 1

                            case ('"', _) : string = True

                            case ("'", _) : char = True

                    i += 1

            return comments
