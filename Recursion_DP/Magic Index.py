# Cracking the Coding Interview - pp. 135 - q. 8.3

def binarySearch(magic: list[int], leftPtr: int, rightPtr: int) -> int:

    if leftPtr <= rightPtr:

        # Create a midpoint pointer
        midPtr =(leftPtr + rightPtr) // 2

        # If element at midPtr equals to midPtr, return index
        if magic[midPtr] == midPtr:
            return midPtr
        
        # If element at midPtr is greater than midPtr, search left half of list
        elif magic[midPtr] > midPtr:
            return binarySearch(magic, leftPtr, midPtr - 1)
        
        # If element at midPtr is smaller than midPtr, search right half of list
        else:
            return binarySearch(magic, midPtr + 1, rightPtr)

    return -1

def magicIndex(magic: list[int]) -> int:

    # If list is empty, return -1
    if len(magic) == 0:
        return -1
    
    return binarySearch(magic, 0, len(magic) - 1)

# magic = [0, 5, 4, 1, 2, 3]
# magic = [4, 1, 0, 3, 5, 2]
magic = [0, 1, 2, 3, 4, 5]
print(magicIndex(magic))