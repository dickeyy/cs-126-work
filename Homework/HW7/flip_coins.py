def flip_coins(input_file_name):
    
    with open(input_file_name) as input_file:
        for line in input_file:
            line = line.strip().upper().split()

            # calculate the number of heads and tails
            heads = line.count('H')
            tails = line.count('T')

            # calculate the percentage of heads and tails
            heads_percentage = int(round((heads / (heads + tails)) * 100, 0))
            tails_percentage = int(round((tails / (heads + tails)) * 100, 0))

            # print the results
            print(f"{heads} heads ({heads_percentage}%)")

            if heads_percentage > 50:
                print("There were more heads!\n")
            else:
                print()