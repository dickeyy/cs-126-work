# Write a complete console program that implements a Caesar cipher or rotation cipher, which is a crude system of encoding strings by shifting every letter forward by a given number. Your program should prompt the user to type a message and an encoding "key" (number of places to shift each character) and display the shifted message. For example, if the shift amount is 3, then the letter A becomes D, and B becomes E, and so on. Letters near the end of the alphabet wrap around for a shift of 3, X becomes A, and Y becomes B, and Z becomes C. Here are two example dialogues:

# Your message? Attack zerg at dawn
# Encoding key? 3
# DWWDFN CHUJ DW GDZQ
# Your message? DWWDFN CHUJ DW GDZQ
# Encoding key? -3
# ATTACK ZERG AT DAWN

# Write code below
message = input("Your message? ")
key = int(input("Encoding key? "))
for c in message:
    if c.isupper():
        print(chr((ord(c) - ord('A') + key) % 26 + ord('A')).capitalize(), end="")
    elif c.islower():
        print(chr((ord(c) - ord('a') + key) % 26 + ord('a')).capitalize(), end="")
    else:
        print(c, end="")
print()

