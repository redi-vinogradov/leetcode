def singleNumber(nums):
    """ O(n) would be just place every unique value to new list (or set) and
    then print it using pop() (returns last item in the list)
    """
    new_nums = set()
    for i in nums:
        if i in new_nums:
            new_nums.remove(i)
        else:
            new_nums.add(i)
    print(new_nums.pop())

def main():
    nums = [2,2,1]
    singleNumber(nums)

if __name__ == '__main__':
    main()
