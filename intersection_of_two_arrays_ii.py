def intersect(nums1, nums2):
    """ One-line solution is complicated
    Second solution trick is to fill up new list with each element quantity
    and increase this quantity is it not unique or keep it equal to 1 if 
    unique. After that for each element in second list decrease the value of
    each element if it exists and greater than 0
    """
    #res = [nums1.remove(x)==None and x for x in nums2 if x in nums1]
    #print(res)

    vals = {}
    result = []
    for n1 in nums1:
        if n1 in vals:
            vals[n1] += 1
        else:
            vals[n1] = 1

    for n2 in nums2:
        if n2 in vals and vals[n2] > 0:
            vals[n2] -= 1
            result.append(n2)
    print(result)

def main():
    nums1 = [1,2,2,1,2,2]
    nums2 = [2,2]
    intersect(nums1, nums2)

if __name__ == '__main__':
    main()
