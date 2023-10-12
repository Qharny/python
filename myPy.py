# A python code to print your name in style

# get user name
name = input("Enter your name: ")
print(f"Hello {name}")
print("This is the pattern of your name.")
print("\n\n ※⁜※⁜※⁜※⁜※⁜※⁜※⁜※⁜※⁜※⁜※⁜※⁜※⁜※⁜※⁜※ \n\n")

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
    if x == "B":
        print('''

            #####
            #    #
            #####
            #    #
            #####

''')
    if x == "C":
        print('''

             ####
            #
            #
            #
             ####

''')
    if x == "D":
        print('''

            ####
            #   #
            #    #
            #   #
            ####

''')
    if x == "E":
        print('''

            ######
            #
            ######
            #
            ######

''')
    if x == "F":
        print('''

            ######
            #
            ######
            #
            #

''')
    if x == "G":
        print('''

             #####
            #
            #  ###
            #    #
             #####

''')
    if x == "H":
        print('''

            #   #
            #   #
            #####
            #   #
            #   #

''')
    if x == "I":
        print('''

             #
             #
             #
             #
             #

''')
    if x == "J":
        print('''

                #
                #
                #
            #   #
             ###

''')
    if x == "K":
        print('''

            #   #
            #  #
            ##
            #  #
            #   #

''')
    if x == "L":
        print('''

            #
            #
            #
            #
            ######

''')
    if x == "M":
        print('''

            #     #
            ##   ##
            # # # #
            #  #  #
            #     #

''')
    if x == "N":
        print('''

            #    #
            ##   #
            # #  #
            #  # #
            #    #

''')
    if x == "O":
        print('''

             ###
            #   #
            #   #
            #   #
             ###

''')
    if x == "P":
        print('''

            #####
            #   #
            #####
            #
            #

''')
    if x == "Q":
        print('''

             ###
            #   #
            #   #
            #  ##
             ###

''')
    if x == "R":
        print('''

            #####
            #   #
            #####
            #  #
            #   #

''')
    if x == "S":
        print('''

             #####
            #
             ####
                #
            #####

''')
    if x == "T":
        print('''

            ######
               #
               #
               #
               #

''')
    if x == "U":
        print('''

            #   #
            #   #
            #   #
            #   #
             ###

''')
    if x == "V":
        print('''

            #     #
             #   #
              # #
               #

''')
    if x == "W":
        print('''

            #     #
            #  #  #
            # # # #
            ## ##
            #     #

''')
    if x == "X":
        print('''

            #   #
             # #
              #
             # #
            #   #

''')
    if x == "Y":
        print('''

            #   #
             # #
              #
              #
              #

''')
    if x == "Z":
        print('''

            ######
               #
              #
            #
            ######

''')
    # else:
    #     print("Pattern not available for the letter: " + x)

pattern = []
pattern.append(x)
print(pattern)