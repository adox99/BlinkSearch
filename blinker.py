# basic way to make blink device
# search for something
# made by ado

# WHAT THIS PROGRAM IS DOING
#
# This program will convert 3 given inputs
# from a human, and convert these into different
# letters, numbers and perform various tasks
# For sake of example, this program is taking the
# three inputs as follows:
#
# left eye blink
# right eye blink
# both eyes blinking in sync
#
# This program is also assuming that the 3 inputs
# each time are accurate with 100% confidence,
# meaning there will be no implementation of 'undo'
# also, as the brain is difficult to read, the three inputs
# will be optimized to find letters/numbers as quickly as possible
#
# Later in this programs development, the use of a users history,
# or user's common trends/themes, will help the program become
# more efficient, given as there are only 3 inputs, efficiency is
# very important.
#
# EXTRA
# This program will really always be based on the number of
# unique inputs that can be sent and recognized (WITH 100% CONFIDENCE)
# through the brain waves that are being monitored.
#
# The rest of the comments below are notes for development


# most common items to think about
# A-Z, 0-9
# 36 characters total
# left eye + right eye + both eyes
# only give input, not output
#   both  = b
#   left  = l
#   right = r

# start for letters   =    b l b
#   'e t a o i | n s r h l | d c u m f | p g w y b | v k x j q z'
#        0           1           2           3           4           [ l translation ]
#    0 1 2 3 4   0 1 2 3 4   0 1 2 3 4   0 1 2 3 4   0 1 2 3 4 5     [ r translation ]
#
# confirm with b

# start for numbers   =    b r b
#   '0 1 2 | 3 4 5 | 6 7 8 9'
#      0       1       2         [ l translation ]
#    0 1 2   0 1 2   0 1 2 3     [ r translation ]
#
# confirm with b

# reset for "NONE"    =    b b b

commonLettersList = 'e t a o i n s r h l d c u m f p g w y b v k x j q z'
commonNumbersList = '0 1 2 3 4 5 6 7 8 9'

commonLetters = [
    [
        'e', 't', 'a', 'o', 'i'
    ],
    [
        'n', 's', 'r', 'h', 'l'
    ],
    [
        'd', 'c', 'u', 'm', 'f'
    ],
    [
        'p', 'g', 'w', 'y', 'b'
    ],
    [
        'v', 'k', 'x', 'j', 'q', 'z'
    ]
]

commonNumbers = [
    [
        '0', '1', '2'
    ],
    [
        '3', '4', '5'
    ],
    [
        '6', '7', '8', '9'
    ]
]

class Blinker():
    def __init__(self):
        self.commandlist = '' # used for general "menu-like" commands
        self.commandstr  = '' # used for building words/numbers together
        self.usingLetters = False
        self.usingNumbers = False
         # index:0, l | index:1, r
        self.letterIndex = [-1, -1]
        self.numberIndex = [-1, -1]
    def getIndexShift(self, letter):
        if letter == 'l':
            return 0
        elif letter == 'r':
            return 1
    def fire(self):
        # will run the command given
        
        self.commandstr  = ''
        self.commandlist = ''
        pass
    def update(self, newLetter):
        indexShift = self.getIndexShift(newLetter)

        # 3 basic functionalities
        # switching between letters, numbers, and reseting commandlist
        if self.commandlist == 'bbb': # 3 normally, 4 if already in category
            if self.usingLetters:
                print('exiting letters')
            if self.usingNumbers:
                print('exiting numbers')
            self.usingLetters = False
            self.usingNumbers = False
            self.commandlist  = '' 
        if not self.usingLetters and not self.usingNumbers:
            if self.commandlist == 'blb':
                print('now using letters')
                self.usingLetters = True
                self.usingNumbers = not self.usingLetters
                self.commandlist = ''
            elif self.commandlist == 'brb':
                print('now using numbers')
                self.usingNumbers = True
                self.usingLetters = not self.usingNumbers
                self.commandlist = ''
            #elif self.commandlist == 'bbb':
            #    print('cleared command list')
            #    self.commandlist = ''
        else: # either letters or numbers are active
            # check for confirmation (use a single b to confirm)
            if newLetter == 'b':
                if self.usingLetters:
                    if self.letterIndex[0] > -1 and self.letterIndex[1] > -1:
                        foundLetter = commonLetters[self.letterIndex[0]][self.letterIndex[1]]
                        print(f'{self.commandstr} -> {self.commandstr + foundLetter}')
                        self.commandstr += foundLetter
                        # reset the letters
                        self.letterIndex[0] = -1
                        self.letterIndex[1] = -1
                    else: # tried to confirm nothing (so add to commandlist)
                        self.commandlist += 'b'
                elif self.usingNumbers:
                    pass
            else: # changing indexes
                if self.usingLetters:
                    print(f'{self.letterIndex[indexShift]} -> {self.letterIndex[indexShift] + 1}')
                    self.letterIndex[indexShift] += 1
                elif self.usingNumbers:
                    print(f'{self.numberIndex[indexShift]} -> {self.numberIndex[indexShift] + 1}')
                    self.numberIndex[indexShift] += 1

    def run(self):
        while True:
            # would be some sort of blink input
            # for now will fill with just simple
            # input() statement
            blinkLetter = input('Letter: ')
            # blink letter will always be either
            # l, r or b
            if blinkLetter == 'b' or blinkLetter == 'r' or blinkLetter == 'l':
                if not self.usingLetters and not self.usingNumbers:
                    self.commandlist += blinkLetter
                else: # modifying commandstr (not commandlist)
                    pass
                self.update(blinkLetter)
            elif blinkLetter == 'exit':
                return 1
            else:
                print('bad command')

def main():
    b = Blinker()

    # accepting input for the command
    b.run()

    


if __name__ == "__main__":
    main()