def rotate(nums, k):
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
