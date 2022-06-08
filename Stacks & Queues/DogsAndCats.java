// Cracking the Coding Interview - pp. 98 - q 3.6

import java.util.*;

public class DogsAndCats {

    class Animal {

        // OBJECTIVE: Create a class within class that will hold animal type and time at shelter

        String specie;
        int timeAtShelter;
    
        Animal(String specie, int timeAtShelter) {
            this.specie = specie;
            this.timeAtShelter = timeAtShelter;
        }
    }

    // Create 2 queues for each animal
    Queue<Animal> dogQueue;
    Queue<Animal> catQueue;

    DogsAndCats() {
        dogQueue = new Queue<Animal>();
        catQueue = new Queue<Animal>();
    }


}
