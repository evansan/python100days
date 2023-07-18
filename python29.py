def yellow(text):
        return "\033[33m" + text
def purple(text):
        return "\033[35m" + text
def green(text):
        return "\033[32m" + text
def default(text):
         return "\033[0m" + text


print("Super Subroutine")

print("With my ", yellow("new program"), default("I can just call green('and') "), green("and"), "\n", 
     default("that word will appear in the color I set it to. "),
    "\n" "With no ", purple("weird gaps"), default("."), sep="" )


