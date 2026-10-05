"""
    WRTD, who reads the docs?
    creates docs from comments
    Nick H 
"""

def stripCComment(file) :

    with open(file, "r") as f :
        text = f.read()
        comments = []
        current = []
        i = 0
        string = char = inline = multiline = False

        def stripStar(line) :

            stripped = line.lstrip()
            if stripped.startswith('*') : # rid javadocs style multiline comment '*'
                stripped = stripped[1:].removeprefix(' ')
            return stripped

        def multilineFlush() :

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

        while i < len(text) :
            
            curr = text[i]
            next = text[i + 1] if i + 1 < len(text) else ''

            if inline :

                if curr == '\n': # end inline comment
                    
                    inline = False
                    comments.append(''.join(current).strip())
                    current = []
                
                else : current.append(curr)

            elif multiline :

                if curr == '*' and next == '/' : # end multiline comment
                    
                    multiline = False
                    comments.append(multilineFlush())
                    current = []
                    i += 1

                else : current.append(curr)

            elif string : # track if in string, because comment-like syntax in strings aren't real comments

                if curr == '\\' : i += 1
                elif curr == '"' : string = False

            elif char : # same logic as for strings

                if curr == '\\' : i += 1
                elif curr == "'" : char = False

            else : # enter into comments/literals

                if curr == '/' and next == '/' : inline = True ; i += 1

                elif curr == '/' and next == '*' : multiline = True ; i += 1

                elif curr == '"' : string = True

                elif curr == "'" : char = True

            i += 1

        # cleanup unterminated comments
        if current : comments.append(multilineFlush() if multiline else ''.join(current).strip())

        return comments
