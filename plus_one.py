def plusOne(digits):
    """ First of all we need to convert original list to a string (done with 
    map() and then convert it back to int to add 1 (so we can get 124 from
    [1,2,3]). Next with list comprehension we are returning list of int values
    converted from a string.
    """
    s = int(''.join(map(str, digits))) + 1
    print([int(s) for s in str(s)])

def main():
    digits = [1,2,3]
    plusOne(digits)

if __name__ == '__main__':
    main()
