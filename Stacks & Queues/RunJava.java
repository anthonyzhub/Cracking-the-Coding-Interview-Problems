public class RunJava {

    public static void main(String[] args) {

        // Initialize class
        SortStack sortedStack = new SortStack();
            
        sortedStack.push(1);
        sortedStack.push(2);
        sortedStack.push(3);
        sortedStack.push(4);
        sortedStack.push(5);
        sortedStack.push(50);
        sortedStack.push(51);

        sortedStack.peek();
        sortedStack.pop();
        sortedStack.pop();
        sortedStack.printStack();
    }
}
