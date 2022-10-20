# Cracking the Coding Interview - pp. 135 - q. 8.5

def multiply(a: int, b: int):

    """
    OBJECTIVE: Take 2 positive integers and multiply them without using the * operator

    Time Complexity: O(n) where n = the b input parameter. I set b as the smallest number whereever the function
                    is first called. After each recursive call, b decrements by 1 until it equals 1. 

    Space Complexity: O(n) where n = the b input parameter
    """

    # If b == 1, return a because anything times 1 equals itself
    if b == 1:
        return a

    # If == 0, immediately stop function by returning 0
    elif b == 0:
        return 0
    
    # Make a recursive call and reduce b by 1
    return a + multiply(a, b - 1)

a = 0
b = 33

print(multiply(max(a, b), min(a, b)))
