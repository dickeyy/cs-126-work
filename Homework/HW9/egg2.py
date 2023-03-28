def main():
    egg_without_middle()
    egg_middle()
    egg_without_middle()
    egg_middle()
    bottom_half()
    whole_egg()

def egg_without_middle():
    print("  _______")
    print(" /       \\")
    print("/         \\")
    print("\\         /")
    print(" \\_______/")

def egg_middle():
    print("-\"-'-\"-'-\"-")

def bottom_half():
    print("\\         /")
    print(" \\_______/")

def whole_egg():
    print("  _______")
    print(" /       \\")
    print("/         \\")
    print("-\"-'-\"-'-\"-")
    print("\\         /")
    print(" \\_______/")

main()