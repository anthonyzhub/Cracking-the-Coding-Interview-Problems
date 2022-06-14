// Cracking the Coding Interview - pp. 98 - q 3.6

import java.util.*;

public class DogsAndCats {

    public class Animal implements Comparable<Animal> {

        // OBJECTIVE: Create a class within class that will hold animal type and time at shelter
    
        String specie;
        int timeAtShelter;
    
        Animal(String specie, int timeAtShelter) {
            this.specie = specie;
            this.timeAtShelter = timeAtShelter;
        }

        int getTime() {return timeAtShelter;}
    
        @Override
        public int compareTo(Animal otherAnimal) {
    
            // OBJECTIVE: Compare time at shelter between this class's age against otherAnimal's

            if (this.timeAtShelter > otherAnimal.timeAtShelter) {
                return 1;
            }
            else if (this.timeAtShelter < otherAnimal.timeAtShelter) {
                return -1;
            }
            return 0;
        }
    }

    // Create 2 queues for each animal
    ArrayList<Animal> dogQueue;
    ArrayList<Animal> catQueue;

    DogsAndCats() {
        dogQueue = new ArrayList<Animal>();
        catQueue = new ArrayList<Animal>();
    }

    void reviewAnimals() {

        // OBJECTIVE: Print all animals inside of queues
        /*
        ArrayList<Animal> tmp = new ArrayList<Animal>();
        tmp.addAll(dogQueue);
        tmp.addAll(catQueue);
        Collections.sort(tmp);
        for (Animal curAnimal: tmp) {
            System.out.printf("%s - %d, ", curAnimal.specie, curAnimal.timeAtShelter);
        }
        */

        System.out.println("Dog");
        for (Animal dog: dogQueue) {System.out.print(dog.timeAtShelter + " ");}
        System.out.println();

        System.out.println("Cat");
        for (Animal cat: catQueue) {System.out.print(cat.timeAtShelter + " ");}
        System.out.println();

        // Create a dog and cat pointer
        int dogIT = 0;
        int catIT = 0;

        // Iterate both queues at the same time
        while (dogIT < dogQueue.size() && catIT < catQueue.size()) {

            // Get both animals
            Animal curDog = dogQueue.get(dogIT);
            Animal curCat = catQueue.get(catIT);

            // Print oldest animal first, then update index pointer
            if (curCat.timeAtShelter >= curDog.timeAtShelter) {
                System.out.printf("Cat - %d, ", curCat.timeAtShelter);
                catIT++;
            }
            else {
                System.out.printf("Dog - %d, ", curDog.timeAtShelter);
                dogIT++;
            }
        }

        // Iterate remaining part of catQueue
        while (catIT < catQueue.size()) {
            System.out.printf("Cat - %d, ", catQueue.get(catIT).timeAtShelter);
            catIT++;
        }

        // Iterate remaining part of dogQueue
        while (dogIT < dogQueue.size()) {
            System.out.printf("Dog - %d, ", dogQueue.get(dogIT).timeAtShelter);
            dogIT++;
        }
        
    }

    void enqueue(String animalType, int timeAtShelter) {

        // OBJECTIVE: Add new animal to appropriate queue

        // Create a new instance of animal class
        Animal newAnimal = new Animal(animalType, timeAtShelter);

        // If animal type is a dog, add it to dog queue. If it's a cat, add it to cat queue
        if (newAnimal.specie == "Cat") {
            catQueue.add(newAnimal);
            Collections.sort(catQueue);
        }
        else if (newAnimal.specie == "Dog") {
            dogQueue.add(newAnimal);
            Collections.sort(dogQueue);
        }
        else {
            return;
        }
    }

    Animal dequeue(String animalType) {

        // OBJECTIVE: Return oldest animalType. If animalType is null, then return oldest animal from the shelter

        // If both queues are empty, exit function
        if (catQueue.isEmpty() && dogQueue.isEmpty()) {return null;}

        // If animalType is null, return oldest animal from the shelter
        if (animalType == null) {

            // If either queue is empty, return oldest animal from non-empty queue
            if (!catQueue.isEmpty() && dogQueue.isEmpty()) {
                return catQueue.remove(0);
            }
            else if (catQueue.isEmpty() && !dogQueue.isEmpty()) {
                return dogQueue.remove(0);
            }

            // Get oldest animal from both queues
            Animal oldestCat = catQueue.get(0);
            Animal oldestDog = dogQueue.get(0);

            // Pop and return oldest animal
            if (oldestCat.timeAtShelter >= oldestDog.timeAtShelter) {
                return catQueue.remove(0);
            }
            return dogQueue.remove(0);
        }

        // If preferred animal is a cat and there's a cat available, return oldest cat
        else if (animalType == "Cat" && !catQueue.isEmpty()) {
            return catQueue.remove(0);
        }

        // If preferred animal is a dog and there's a dog available, return oldest dog
        else if (animalType == "Dog" && !dogQueue.isEmpty()) {
            return dogQueue.remove(0);
        }
        return null;
    }
}