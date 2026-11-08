# Who Reads The Docs?
A tool that pulls comments from a project into a separate docs directory

## How do I use it?
wrtd makes the distinction between using block and inline comments. For now,
if you use block comments they will be the only ones processed into a docs file.
If you wish to explicitly include the content from an inline comment,
you must use the @DOCS decorator. For block comments (`/*` and `*/` in c-like languages)
the continuous string of characters contained within will be automatically parsed as markdown.
This stream of markdown is then generated per-file and placed in a duplicate subdirectory of the 
current working directory, `cwd/docs`. To instead output a plain .txt file, use the @TEXT decorator
at some point in the file.

## What languages are supported?
Currently, only C-Style comments using `/*` and `*/`,
but more language support in the future is something I hope for.

## What decorators are there?
### Available
> more to come soon
### Planned
- @DOCS
- @TEXT
- @LIST

## Examples

### @DOCS
For the following code snippet:
```c
/* # Add function */
/* This function adds two numbers */
int add(int a, int b) { // Don't include me in docs
  return a + b; // @DOCS Include me in docs
}
```
the following markdown file would be created
```md
# Add function
This function adds two numbers
Include me in docs
```

### @TEXT
This outputs .txt files rather than .md files \
(Not supported yet)

### @LIST
This will be intended to make working lists of things.
Todos, count things, classify functions, etc... If a block comment starts with @TEXT,
then the following comment will not appear in file's corresponding doc file, but instead
be put in a separate directory `docs/lists`. Project-wide, lists will end up here, still
formatted in markdown. The @TEXT decorator will have no effect on lists \
(Not supported yet)

## Why did I make this?
Well, I did very little research confirming that a similar tool doesn't exist,
but I wanted something that would document my work without having to keep tabs
on separate documents and/or duplicating existing comments into wikis and documentation.
That and, someone had told me I need to comment my code better.
