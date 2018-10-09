def moveZeroes(nums):
    """ The trick is very simple: check if value is equal to zero and if it is
    than remove that value from the list and add it to the end.
    """
    zeroes = []
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(i)

    print(nums)


def main():
    nums = [0,1,0,3,12]
    moveZeroes(nums)

if __name__ == '__main__':
    main()
