import java.util.Random;

public class RunJava {

    public static void main(String[] args) {

        // Initialize class
        DogsAndCats shelter = new DogsAndCats();
        
        String[] options = {"Cat", "Dog"};
        for (int i=0; i<5; i++) {

            // Select a random animal
            String randAnimal = options[new Random().nextInt(options.length)];

            // Add animal to queue
            shelter.enqueue(randAnimal, new Random().nextInt(100));
        }

        // Adopt cat and dog
        shelter.dequeue("Dog");
        // shelter.reviewAnimals();
        shelter.dequeue("Cat");
        shelter.reviewAnimals();
    }
}
