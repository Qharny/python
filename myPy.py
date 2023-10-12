# A python code to print your name in style

# get user name
name = input("Enter your name: ")

for x in name:
    x = x.upper()
    if x == "A":
        print('''

               #
              # #
             #   #
            # ### #
           #       #
          #         #

''')
    elif x == "B":
        print('''

            #####
            #    #
            #####
            #    #
            #####

''')
    elif x == "C":
        print('''

             ####
            #
            #
            #
             ####

''')
    elif x == "D":
        print('''

            ####
            #   #
            #    #
            #   #
            ####

''')
    elif x == "E":
        print('''

            ######
            #
            ######
            #
            ######

''')
    elif x == "F":
        print('''

            ######
            #
            ######
            #
            #

''')
    elif x == "G":
        print('''

             #####
            #
            #  ###
            #    #
             #####

''')
    elif x == "H":
        print('''

            #   #
            #   #
            #####
            #   #
            #   #

''')
    elif x == "I":
        print('''

             #
             #
             #
             #
             #

''')
    elif x == "J":
        print('''

                #
                #
                #
            #   #
             ###

''')
    elif x == "K":
        print('''

            #   #
            #  #
            ##
            #  #
            #   #

''')
    elif x == "L":
        print('''

            #
            #
            #
            #
            ######

''')
    elif x == "M":
        print('''

            #     #
            ##   ##
            # # # #
            #  #  #
            #     #

''')
    elif x == "N":
        print('''

            #    #
            ##   #
            # #  #
            #  # #
            #    #

''')
    elif x == "O":
        print('''

             ###
            #   #
            #   #
            #   #
             ###

''')
    elif x == "P":
        print('''

            #####
            #   #
            #####
            #
            #

''')
    elif x == "Q":
        print('''

             ###
            #   #
            #   #
            #  ##
             ###

''')
    elif x == "R":
        print('''

            #####
            #   #
            #####
            #  #
            #   #

''')
    elif x == "S":
        print('''

             #####
            #
             ####
                #
            #####

''')
    elif x == "T":
        print('''

            ######
               #
               #
               #
               #

''')
    elif x == "U":
        print('''

            #   #
            #   #
            #   #
            #   #
             ###

''')
    elif x == "V":
        print('''

            #     #
             #   #
              # #
               #

''')
    elif x == "W":
        print('''

            #     #
            #  #  #
            # # # #
            ## ##
            #     #

''')
    elif x == "X":
        print('''

            #   #
             # #
              #
             # #
            #   #

''')
    elif x == "Y":
        print('''

            #   #
             # #
              #
              #
              #

''')
    elif x == "Z":
        print('''

            ######
               #
              #
            #
            ######

''')
    else:
        print("Pattern not available for the letter: " + x)
