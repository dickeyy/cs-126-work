# Write a function named get_file_name that repeatedly prompts the user for a file name until the user types the name of a file that exists on the system. Once you get a good file name, return that file name as a string. Here is a sample dialogue from one call to your function, assuming that the file good.txt does exist and the others do not:

# Type a file name: bad.txt
# Type a file name: not_here.txt
# Type a file name: good.txt

# Write your function here
def get_file_name():
    while True:
        filename = input("Type a file name: ")
        if os.path.exists(filename):
            return filename
        print("File not found. Try again.")
        