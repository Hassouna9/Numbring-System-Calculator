#Ahmed Hassouna
import math
conditionYes = 0


def checkD(UserInput):
    z = 0
    global conditionYes
    for i in UserInput:
        if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            z += 1
    if z > 0:
        return "Not a Decimal number"
    else:
        conditionYes = 1
        return "it is a Decimal number "


def checkB(UserInput):
    z = 0
    global conditionYes
    for i in UserInput:
        if i not in ["0", "1", "."]:
            z += 1
    if z > 0:
        return "Not a Binary number"
    else:
        conditionYes = 1
        return "it is a Binary number"


def checkO(UserInput):
    z = 0
    global conditionYes
    for i in UserInput:
        if i not in ["1", "2", "3", "4", "5", "6", "7", "8", "."]:
            z += 1
    if z > 0:
        return "not a Octal number"
    else:
        conditionYes = 1
        return "it is a Octal number"


def checkH(UserInput):
    z = 0
    global conditionYes
    for i in UserInput:
        if i not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "A", "B", "C", "D", "E", "F"]:
            z += 1
    if z > 0:
        return "not a Hex_decimal number"
    else:
        conditionYes = 1
        return "it is a Hex_decimal number"


def Hex2D(word):
    if word == "A" or "a":
        word = 10
    elif word == "B" or "b":
        word = 11
    elif word == "C" or "c":
        word = 12
    elif word == "D" or "d":
        word = 13
    elif word == "E" or "e":
        word = 14
    elif word == "F" or "f":
        word = 15
    return word


def D2Hex(word):
    if word == 10:
        word = "A"
    elif word == 11:
        word = "B"
    elif word == 12:
        word = "C"
    elif word == 13:
        word = "D"
    elif word == 14:
        word = "E"
    elif word == 15:
        word = "F"
    return word


def Any2D(UserIn, Base):
    New = UserIn.split(".")
    FirstPart = 0
    SecondPart = 0
    condition = 0
    if len(New) == 1:
        FirstPart = New[0]
    elif len(New) == 2:
        FirstPart = New[0]
        SecondPart = New[1]
        condition = 1
    total1 = 0
    total2 = 0
    start = len(FirstPart)
    startD = 0
    if condition == 1:
        for i in SecondPart:
            if not i.isalpha():
                number = int(i)
            else:
                number = Hex2D(i)
            startD = startD - 1
            one = number * Base ** startD
            total2 = total2 + one
    for i in FirstPart:
        if not i.isalpha():
            number = int(i)
        else:
            number = Hex2D(i)
        start = start - 1
        one = number * Base ** start
        total1 = total1 + one
    return str(total1 + total2)


def D2Any(UserIn, Base):
    New = UserIn.split(".")
    FirstPart = 0
    SecondPart = 0
    condition = 0
    string1, string2 = "", ""
    # Fraction Condition
    if len(New) == 1:
        FirstPart = New[0]
    elif len(New) == 2:
        FirstPart = New[0]
        SecondPart = "0." + New[1]
        condition = 1
    # First Part
    Reminder1 = int(FirstPart) % Base
    output = int(FirstPart) // Base
    if Reminder1 > 9:
        Reminder1 = D2Hex(Reminder1)
    string1 = string1 + str(Reminder1)
    while output != 0:
        Reminder1 = output % Base
        output = output // Base
        Reminder1 = D2Hex(Reminder1)
        string1 = string1 + str(Reminder1)
    # Second Part
    if condition == 1:
        Reminder2 = math.floor(float(SecondPart) * Base)
        output2 = (float(SecondPart) * Base) - math.floor(float(SecondPart) * Base)
        if Reminder2 > 9:
            Reminder2 = D2Hex(Reminder2)
        string2 = string2 + str(Reminder2)
        while output2 != 0:
            Reminder2 = math.floor(output2 * Base)
            output2 = (float(output2) * Base) - math.floor(float(output2) * Base)
            Reminder2 = D2Hex(Reminder2)
            string2 = string2 + str(Reminder2)
    if condition == 1:
        return string1[::-1] + "." + string2
    else:
        return str(string1[::-1])

UserInput = input("Enter The Number: ").upper()
InputType = input("Enter The Type of the number: ")

conditionType = ''
converstionType = ''
# Input is decimal
if InputType in ["D", 'd', "Decimal", 'decimal', '10', 10]:
    conditionType = "D"
if conditionType == "D":
    print(checkD(UserInput))

if conditionYes ==1 and conditionType == "D":
    ToBase = input("Enter The Type or Base you want to Convert to: ")
    if ToBase in ["b",'B',"binary","Binary",2,"2"]:
        print(D2Any(UserInput, 2))
    if ToBase in ["O", 'o', "Octa", "octa", "8", 8]:
        print(D2Any(UserInput, 8))
    if ToBase in ["H", 'h', "Hex", "hex", "16", 16]:
        print(D2Any(UserInput, 16))

# Input is binary

if InputType in ["b",'B',"binary","Binary",2,"2"]:
    conditionType = "B"
if conditionType == "B":
    print(checkB(UserInput))

if conditionYes ==1 and conditionType == "B":
    ToBase = input("Enter The Type or Base you want to Convert to: ")
    if ToBase in ["D", 'd', "Decimal", 'decimal', '10', 10]:
        print(Any2D(UserInput, 2))
    if ToBase in ["O", 'o', "Octa", "octa", "8", 8]:
        print(D2Any(Any2D(UserInput,2),8))
    if ToBase in ["H", 'h', "Hex", "hex", "16", 16]:
        print(D2Any(Any2D(UserInput,2),16))

# Input is octa

if InputType in ["O", 'o', "Octal", "octal", "8", 8]:
    conditionType = "O"
if conditionType == "O":
    print(checkO(UserInput))

if conditionYes ==1 and conditionType == "O":
    ToBase = input("Enter The Type or Base you want to Convert to: ")
    if ToBase in ["D", 'd', "Decimal", 'decimal', '10', 10]:
        print(Any2D(UserInput, 8))
    if ToBase in ["b",'B',"binary","Binary",2,"2"]:
        print(D2Any(Any2D(UserInput,8),2))
    if ToBase in ["H", 'h', "Hex", "hex", "16", 16]:
        print(D2Any(Any2D(UserInput,8),16))

# Input is Hex

if InputType in ["H", 'h', "Hex", "hex", "16", 16]:
    conditionType = "H"

if conditionType == "H":
    print(checkH(UserInput))

if conditionYes ==1 and conditionType == "H":
    ToBase = input("Enter The Type or Base you want to Convert to: ")
    if ToBase in ["D", 'd', "Decimal", 'decimal', '10', 10]:
        print(Any2D(UserInput, 16))
    if ToBase in ["b",'B',"binary","Binary",2,"2"]:
        print(D2Any(Any2D(UserInput,16),2))
    if ToBase in ["O", 'o', "Octal", "octal", "8", 8]:
        print(D2Any(Any2D(UserInput,16),8))


Stop = input("Press any to continue: ")