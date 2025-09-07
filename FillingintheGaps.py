#Filling in the Gaps
#C:\Users\Dan\Downloads\Python codes\Text files

import os, re
from pathlib import Path
import pyinputplus as pyip

prefix = 'spam'

searched_folder = pyip.inputStr(prompt = \
                                'Enter absolute path of searched folder\n')

lastnum = 0

for filename in os.listdir(Path(searched_folder)):
    if filename.startswith(prefix):
        index = ''
        try:
            for char in filename[len(prefix): len(filename)]:
                if type(int(char)) is not int:
                    break
                else:
                    index += char
        except:
            pass
        if index != '':
            num = int(index)
            if num - lastnum > 1:
                for i in range(num - lastnum - 1):
                    print('Gap at position: ' + str(lastnum + i + 1))
            lastnum = num
        else:
            print(filename + ' is not from the series')
