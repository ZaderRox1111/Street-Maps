import sys
from random import *
import math

#create global constants
MIN_BLOCK_LOC = 0
MAX_BLOCK_LOC = 100
MIN_LENGTH = 1
MAX_LENGTH = 100
DIR_CHANCE = 0.9

def main():
    #name of file to create, amount of lines of data to generate
    write_file = sys.argv[1]
    amount_of_entries = int(sys.argv[2])

    #generate the data and store into lines of data
    data = create_data(amount_of_entries)

    #write those lines into a file
    with open(write_file, 'w') as writing:
        writing.writelines(data)

def create_data(amount):
    #empty data list, and counter to help make data easier to work with
    data = []
    counter = 0

    #create lines of data one by one using the for loop
    for index in range(amount):
        #creating the x, y, and length randomly
        x_start = float(randint(MIN_BLOCK_LOC, MAX_BLOCK_LOC))
        y_start = float(randint(MIN_BLOCK_LOC, MAX_BLOCK_LOC))
        length = float(randint(MIN_LENGTH, MAX_LENGTH))
        
        #creating direction with a weighted bias
        if (random() < DIR_CHANCE):
            #splitting between up and right 50%
            if (random() < 0.5):
                direction = 0.
            else:
                direction = 5.
        
        else:
            #every other direction between 0-9 (0-18 here)
            direction = randint(0, 18)

        #put direction between 0-9
        direction = direction / 2.

        #update the counter
        counter += 1

        #format the line of data
        line = f"{x_start} {y_start} {length} {direction} {counter}\n"

        #add the line to the list of data
        data.append(line)

    #return the list of data
    return data

if __name__ == "__main__":
    main()
