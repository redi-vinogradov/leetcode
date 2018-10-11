def twoSum(nums, target):
    """ For each element of list we check if remainder of target-current element
    exists in new dictionary. And if it's there - then we have our target sum.
    """
    ndict = {}
    for i, n in enumerate(nums):
        if target-n in ndict:
            print([ndict[target-n], i])
        ndict[n] = i

def main():
    nums = [2,7,11,15]
    target = 9
    twoSum(nums, target)

if __name__ == '__main__':
    main()
