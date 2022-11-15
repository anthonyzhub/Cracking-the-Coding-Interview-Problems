# Cracking the Coding Interview - pp. 135 - q. 8.6

class Tower:

    def __init__(self, index) -> None:
        
        # Create a stack and an index pointer
        self.stack = list()
        self.idx = index
    
    def getIndex(self):
        # OBJECTIVE: Return current index value
        return self.idx
    
    def add(self, newDisk):

        # OBJECTIVE: Add a new disk to stack

        # If stack isn't empty, but top element is smaller than new disk, exit function
        if len(self.stack) > 0 and self.stack[0] <= newDisk:
            print("Unable to add disk")
        
        else:
            self.stack.insert(0, newDisk)

    def moveTopTo(self, newTower):

        # OBJECTIVE: Move top element from current tower to a different tower

        topElem = self.stack.pop(0)
        newTower.add(topElem)

    def moveDisks(self, n, destination, buffer):

        # OBJECTIVE: Move disk from current tower to buffer, then move last disk to destination

        # If disk is empty, exit function
        if n <= 0:
            return
        
        # Move n - 1 disk from origin to buffer, using destination as a buffer
        self.moveDisks(n - 1, buffer, destination)

        # Move top disk from origin to destination
        self.moveTopTo(destination)

        # Move top n - 1 disks from buffer to destination, using origin as a buffer
        buffer.moveDisks(n - 1, destination, self)

    def print(self):

        # OBJECTIVE: Print tower from bottom to top

        for disk in self.stack[::-1]:
            print(disk, end=" ")

def main():

    """
    OBJECTIVE: Given 3 towers with tower 1 filled with n disc. The disc are sorted in ascending order and a big disk
                can't sit on top of a smaller disk. Move all discs from tower 1 to tower 3
    
    Time Complexity: O(1) because this algorithm just pops and inserts a new element. Since this is a stack, each
                    stack operation takes O(1) time.

    Space Complexity: O(n) where n = number of disks. The purpose of the function is to move all discs from tower 1 to
                    tower 3. moveDisks() will be making plenty of recursive calls.
    """

    # Define number of disks
    numOfDisks = 3

    # Create 3 towers
    towers = list()
    for i in range(numOfDisks):
        towers.append(Tower(i))

    # Populate origin tower with disks
    for disk in range(numOfDisks, 0, -1):
        towers[0].add(disk)

    # Move disks from origin to destination
    # NOTE: Any tower can be the buffer and destination. The problem just sets the last tower to be the destination
    towers[0].moveDisks(numOfDisks, towers[2], towers[1])
    towers[2].print()

main()