public class RunJava {

    public static void main(String[] args) {

        // Initialize class
        myqueue queueClass = new myqueue();
            
        queueClass.add(1);
        queueClass.add(2);
        queueClass.add(3);
        queueClass.add(4);
        queueClass.add(5);
        queueClass.add(50);
        queueClass.add(51);

        queueClass.peek();
        queueClass.pop();
        queueClass.pop();
        queueClass.printQueue();
    }
}
