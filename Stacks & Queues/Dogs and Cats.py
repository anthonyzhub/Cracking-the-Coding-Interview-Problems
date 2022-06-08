# Cracking the Coding Interview - pp. 98 - q 3.6

from random import choice, randint

class Animal:

    def __init__(self, specie, timeAtShelter) -> None:
        self.specie = specie
        self.timeAtShelter = timeAtShelter

class DogsAndCats:
    
    def __init__(self) -> None:

        # Create a queue for both animals
        self.dogQueue = list()
        self.catQueue = list()

    def reviewAnimals(self):

        # OBJECTIVE: Print animal type and age from both queues

        ans = ""
        for animal in sorted(self.dogQueue + self.catQueue, key= lambda animal: animal.timeAtShelter, reverse=True):
            ans += "{} - {} minutes, ".format(animal.specie, animal.timeAtShelter)

        print(ans)

    def enqueue(self, animalType, timeAtShelter):

        # OBJECTIVE: Add new animal to appropriate queue and sort it afterwards

        # Create a new animal class
        newAnimal = Animal(animalType, timeAtShelter)

        # If newAnimal is a cat, add it to catQueue. If it's a dog, add it to dogQueue
        if newAnimal.specie == "Cat":
            self.catQueue.append(newAnimal)
            self.catQueue.sort(key= lambda animal: animal.timeAtShelter, reverse=True)

        elif newAnimal.specie == "Dog":
            self.dogQueue.append(newAnimal)
            self.dogQueue.sort(key= lambda animal: animal.timeAtShelter, reverse=True)

        else:
            return

    def dequeue(self, animalType=None):

        # OBJECTIVE: Remove oldest animal from either queue. If animalType is specified, remove oldest animal from appropriate queue

        # If both queues are empty, exit function
        if len(self.catQueue) == 0 and len(self.dogQueue) == 0:
            return

        # If a specie wasn't specified, look for oldest animal
        if animalType is None:

            # If either queue is empty, return oldest animal from non-empty queue
            if len(self.dogQueue) == 0 and len(self.catQueue) > 0:
                return self.catQueue.pop(0)
            elif len(self.dogQueue) > 0 and len(self.catQueue) == 0:
                return self.dogQueue.pop(0)
            
            # Get next dog and cat
            nextCat = self.catQueue[0]
            nextDog = self.dogQueue[0]

            # Pop and return oldest animal
            if nextCat.timeAtShelter >= nextDog.timeAtShelter:
                return self.catQueue.pop(0)
            else:
                return self.dogQueue.pop(0)

        # Check if animal type is a cat and that there are cats to adopt
        elif animalType == "Cat" and len(self.catQueue) > 0:
            return self.catQueue.pop(0)

        # Check if animal type is a dog and that there are dogs to adopt
        elif animalType == "Dog" and len(self.dogQueue) > 0:
            return self.dogQueue.pop(0)

        else:
            return

def main():

    # Initialize class
    shelter = DogsAndCats()

    # Populate shelter
    for _ in range(5):
        shelter.enqueue(choice(["Dog", "Cat"]), randint(1, 100))
    shelter.reviewAnimals()

    # Adopt cat and dog
    shelter.dequeue("Dog")
    shelter.reviewAnimals()
    shelter.dequeue("Cat")
    shelter.reviewAnimals()

main()