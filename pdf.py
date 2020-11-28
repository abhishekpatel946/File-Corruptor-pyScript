'''
author: Abhishek Patel
version: 3.8.5
encode: UTF-8
EOL: CRLF
'''

# import lib
import re, sys

# don't active it's dangourres
def active():
    # read and replace with *
    with open('test.txt', 'r') as file:
        newLines = []
        for line in file.readlines():
            for chars in p.findall(line):
                newLines.append(line.replace(chars, '*'))

            # trying to consider an edge-case
            if len(newLines) > 0:
                newLines = newLines[0]
            else:
                print('file curruption completion...!')
                sys.exit()
        # close the file
        file.close()

    # write on file 
    with open('test.txt', 'w') as file:
        for line in newLines:
            file.write(line)
        # close the file
        file.close()

if __name__ == "__main__":
    # make a regular exprssion
    p = re.compile('[a-zA-Z0-9_,.]')

    # try to until each char are available in file
    with open('test.txt', 'r') as file:
        all_char = file.read()
        print('Currupting Data in progress...')
        while p.findall(all_char):
            active()
        # close the file
        file.close()
    print('file curruption completion...!')