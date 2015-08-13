# Turing's Machine

if __name__ == "__main__":
    # The following parallel arrays will describe transition rules
    trState = []
    trIfChar = []
    trWrite = []
    trDir = []
    trNewState = []

    # Read Turing's Machine description from a file
    lines = []
    with open("Tests.txt", "r") as f:
        lines = f.readlines()
    
    if len(lines) < 5:
        print("Cannot read description of Turing Machine from file")
        sys.exit(-1)

    # The folowing variables and array will describe the current state of machine:
    stripe = lines[0].strip()   # Strip is on the 1st line of file
    stripeList = list(stripe)   # We'll need it as a list to modify characters
    pos = int(lines[1])     # Initial position on strip is on the 2nd line
    state = int(lines[2])   # Starting state is on the 3rd line
    finstate = int(lines[3])# Halting state is on the 4th line

    # It's important to ensure that strip starts and ends with a blank ('-')
    if stripeList[0] != '-':
        print("WARNING : Original file doesn't contain blank character '-' at the "
                + "beginning of stripe, so it will be prepanded and initial position"
                + " adjusted appropriately.")
        stripeList = ['-'] + stripeList
        stripe = "".join(stripeList)
        pos += 1
    if stripeList[len(stripeList)-1] != '-':
        print("WARNING : Original file doesn't contain blank character '-' at the "
                + "end of stripe, so it will be appended.")
        stripeList.append('-')
        stripe = "".join(stripeList)


    # Now read in transition rules:
    for i in range(0,(len(lines)-4)):
        transition = lines[i+4].split()
        if len(transition) != 5:
            print("Bad format of input file.")
            sys.exit(-2)
        trState.append(int(transition[0]))
        trIfChar.append(transition[1])
        trWrite.append(transition[2])
        trDir.append(int(transition[3]))
        trNewState.append(int(transition[4]))

    # Release resource:
    f.close()


    # Output initial state
    print("-------------------------------------------")
    print("Initial state of Turing Machine:")
    print(stripe)
    print("pos   = " + str(pos))
    print("state = " + str(state))
    print("-------------------------------------------")


    # Now allow the Turing Machine to process the strip
    while state != finstate:
        # Find the matching rule
        i = 0
        while i < len(trState):
            if trState[i] == state:
                if trIfChar[i] == '*' or trIfChar[i] == stripeList[pos]:
                    break   # If state and character matched rule then stop search
            i += 1  # Else go to next rule
        if i < len(trState):    # If appropriate rule matched
            # Print info about the rule
            print("Matching rule:")
            print("state(" + str(trState[i]) + "), char(" + trIfChar[i] + ")  ->  "
                    + "new state(" + str(trNewState[i]) + "), write(" + trWrite[i]
                    + "), dir(" + str(trDir[i]) + ")")
            # Then apply the rule
            if trWrite[i] != '*':   # Write character only if not wild card
                stripeList[pos] = trWrite[i]
                stripe = "".join(stripeList)
            pos += trDir[i]
            state = trNewState[i]
        else:   # Else the machine can't continue its work
            print("Can not find appropriate rule.")
            print("Turing Machine will terminate immediately.")
            sys.exit(-3)

        # Print out the new state of Turing Machine:
        print("Current state of Turing Machine:")
        print(stripe)
        print("pos   = " + str(pos))
        print("state = " + str(state))
        # In case of situation when head is positioned at the end of strip
        # we must append a blank to right
        if pos == len(stripeList):
            stripeList.append('-')
            stripe = "".join(stripeList)
            print("WARNING : Head is positioned outside writable stripe, so extra "
                    + "blank character '-' will be added at the end.")
        if pos < 0:
            stripeList = ['-'] + stripeList
            stripe = "".join(stripeList)
            pos += 1
            print("WARNING : Head is positioned outside writable stripe, so extra "
                    + "blank character '-' will be added at the beginning.")
            print("          Position of head will be adjusted")
            print("pos   = " + str(pos) + " (adjusted)")
        print("-------------------------------------------")


    # When finished, print out the final state of machine to emphasize it
    print("Final state of Turnig Machine reached:")
    print(stripe)

