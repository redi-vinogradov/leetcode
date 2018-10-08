def rotate(nums, k):
    """ The trick is that we are moving not just each value but slice of array
    to it's new position by calculating value of modulus remainder
    """
    k = k % len(nums)
    if k == 0:
        return
    nums[:k], nums[k:] = nums[-k:], nums[:-k]
    print(nums)

def main():
    nums = [1,2,3,4,5,6,7]
    k = 3
    rotate(nums, k)

if __name__ == '__main__':
    main()
