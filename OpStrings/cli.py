from OpStrings import *

import click

@click.command()
@click.option("-m", '--func', help='function', required=True)
@click.option("-s1", '--str1', help='string1', required=True)
@click.option("-s2", '--str2', help='string2', required=True)

def main(func, str1, str2):
    if func=="maior":
        maxLen(str1, str2)
    elif func=="menor":
        minString(str1, str2)
    elif func=="media":
        meanString(str1,str2)
    else:
        print("Introduza 'maior', 'menor', ou 'media'.")

if __name__ == '__main__':
    main()