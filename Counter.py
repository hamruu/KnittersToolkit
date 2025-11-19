
import sys

def main(startnumber):
    rowcount = 0

    if startnumber % 2 == 1: #If the starting number is odd, reduce it by one to make it even.
        startnumber -= 1
        rowcount += 1
    
    while startnumber > 2: #Then reduce by two and make (n/2)-2 rows per reduction.
        prev = startnumber
        betweens = (startnumber / 2) - 2
        rowcount += (betweens) + 1
        startnumber -= 2
        print(f'Reduction from {prev} to {startnumber}')

    return rowcount

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 Rowcount.py <startnumber>")
        sys.exit(1)

    start = int(sys.argv[1])
    print(main(start))





