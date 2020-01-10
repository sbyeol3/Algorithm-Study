import java.util.Scanner;

public class Stack10828 {
	 private int top;
	 private int maxSize;
	 private int[] stackArray;

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		
		for(int i=0;i<N;i++) {
			String str = s.next();
		}
	}
	
	void push(int X) {
		top = X;
		stackArray[maxSize] = X;
		maxSize++;
	}
	
	int pop() {
		if(maxSize==0)
			return -1;
		else {
			int tmp = stackArray[maxSize-1];
			stackArray[maxSize-1] = -1;
			top = stackArray[maxSize-2];
			maxSize--;
			return tmp;
		}
	}
}
