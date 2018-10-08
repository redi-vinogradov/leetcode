def containsDuplicate(nums):
    """ The trick here is that set() returns unique list of values so the
    easiest solution would be to compare original list with it's unique copy
    """

    return False if len(set(nums)) == len(nums) else True

def main():
    nums = [1,2,3,1]
    if containsDuplicate(nums):
        print("true")
    else:
        print("false")

if __name__ == '__main__':
    main()
