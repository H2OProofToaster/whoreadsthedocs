# Who Reads The Docs?
A tool that pulls comments from a project into a separate docs directory

## How do I use it?
Decorate your comments with @DOCS and wrtd will pull them into markdown files
for you to view. Write your comments in markdown for your docs to have a little
more pzazz.

## What languages are supported?
Currently, only C-Style comments using `/*`, `*/`, and `//`,
but more language support in the future is something I hope for.

## What decorators are there?
### Available
- @DOCS
### Planned
- @TXT
- @FUNC

## Examples

### @DOCS decorator
For this code snippet from 'add.c',
```c
/* @DOCS
 * # Add
 * This function takes two numbers and adds them
 */
int add (int a, int b);
```
This file would be generated 'docs/add.md' at the project root,
```md
# Add
This function takes two numbers and adds them
```

### @TXT decorator
This outputs .txt files rather than .md files \
(Not supported yet)

### @FUNC decorator
This pulls and documents function information when placed above a signature \
(Not supported yet)

## Why did I make this?
Well, I did very little research confirming that a similar tool doesn't exist,
but I wanted something that would document my work without having to keep tabs
on separate documents and/or duplicating existing comments into wikis and documentation.
