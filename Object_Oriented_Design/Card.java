import java.util.HashSet;

public class Card {

    // Create class variables
    String suit;
    String name;
    String color;
    int value;

    void setSuit(String suit) {

        // OBJECTIVE: Set card's suit based on "suit" variable

        // List suit types
        HashSet<String> suits = new HashSet<>();
        suits.add("Clubs");
        suits.add("Hearts");
        suits.add("Spades");
        suits.add("Diamonds");

        // If suit is in suits, update suit
        if (suits.contains(suit)) {this.suit = suit;}
    }

    void setName(String name) {

        // OBJECTIVE: Set card name based on "name" variable

        // List name options
        HashSet<String> names = new HashSet<>();
        names.add("Jack");
        names.add("Queen");
        names.add("King");
        names.add("Ace");

        // If name is part of set, update name variable
        if (names.contains(name)) {
            this.name = name;
        }
        
        // Check if name is numeric
        try {
            this.name = Integer.toString(Integer.parseInt(name));
        }
        catch (NumberFormatException err){
            ; // <= Similar to Python's "pass"
        }

        // If function is still going, then set card as invalid
        this.name = "INVALID CARD!";
    }

    void setColor() {

        // OBJECTIVE: Set card's color based on suit type

        if (this.suit == "Clubs" || this.suit == "Spades") {
            this.color = "Black";
        }
        else if (this.suit == "Hearts" || this.suit == "Diamonds") {
            this.color = "Red";
        }
    }

    void setValue(int value) {

        // OBJECTIVE: Set card's color based on card's name

        if (this.name == "Jack") {
            this.value = 11;
        }

        else if (this.name == "Queen") {
            this.value = 12;
        }

        else if (this.name == "King") {
            this.value = 13;
        }

        // If card's name is Ace, set value to either 1 or 11
        else if (this.name == "Ace") {
            this.value = value == 1 || value == 11 ? value : 1; 
        }

        else {

            try {

                // Convert string to an integer
                int tmpValue = Integer.valueOf(value);

                // Keep input if it's between 1-10
                if (tmpValue > 1 || tmpValue < 10) {
                    this.value = tmpValue;
                }
                else {
                    this.value = -1;
                }
            }
            catch (NumberFormatException err) {
                ;
            }
        }
    }

    Card(String suit, String name) {

        // OBJECTIVE: Construct class without given input value. If so, then this must be a face card

        setSuit(suit);
        setName(name);
        setColor();
        setValue(0);
    }

    Card(String suit, String name, int value) {

        // OBJECTIVE: Construct class with given input value. If so, this isn't a face card

        setSuit(suit);
        setName(name);
        setColor();
        setValue(value);
    }
}