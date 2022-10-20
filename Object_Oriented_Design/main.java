public class main {
    static void main(String[] args) {

        Card one = new Card("Clubs", "King");
        Card two = new Card("Hearts", "Jack");
        Card three = new Card("Spades", "Queen");
        Card four = new Card("Diamonds", "Ace");
        Card five = new Card("Hearts", "1");

        one.info();
        two.info();
        three.info();
        four.info();
        five.info();
    }   
}
