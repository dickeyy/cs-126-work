def touch(elbow, ear):
    print("touch your", elbow, "to your", ear)

def main():
    head = "shoulders"
    knees = "toes"
    elbow = "head"
    eye = "eyes and ears"
    ear = "eye"

    touch(ear, elbow)
    touch(elbow, ear)
    touch(head, "elbow")
    touch(eye, eye)
    touch(knees, "Toes")
    touch(head, "knees " + knees)

main()