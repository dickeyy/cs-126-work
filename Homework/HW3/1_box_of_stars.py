def box_of_stars(width, height):
    print("*" * width, sep="")
    for i in range(0, (height - 2)):
        print('*', " " * (width - 2), "*", sep="")
    print("*" * width, sep="")

box_of_stars(8,5)