def strike(lines):
    split=lines.splitlines()
    for line in split:
        result="-"+line.strip()+"-"
        print(result)

def red(lines):
    split=lines.splitlines()
    for line in split:
        result="{color:#de350b}"+line.strip()+"{color}"
        print(result)

def green(lines):
    split=lines.splitlines()
    for line in split:
        result="{color:#00875a}"+line.strip()+"{color}"
        print(result)

# use three pairs for """
text=""""sdas is   0
dfsdfsdfsdfsdfsd
asdasd"""


strike(text) 
red (text)
green(text)