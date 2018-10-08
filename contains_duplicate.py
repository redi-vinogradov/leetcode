def containsDuplicate(nums):
    return False if len(set(nums)) == len(nums) else True

def main():
    nums = [1,2,3,1]
    if containsDuplicate(nums):
        print("true")
    else:
        print("false")

if __name__ == '__main__':
    main()
