def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    result = False
    for n in nums:
        if n == 7:
            result = True
    
    return result



print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

