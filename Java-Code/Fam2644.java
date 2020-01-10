import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Fam2644 {
	static int graph[][];
	static int cnt=-1;
	static Queue<Integer> queue = new LinkedList<>();
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		int n=s.nextInt();
		int a=s.nextInt();
		int b=s.nextInt();
		int m=s.nextInt();
		
		graph = new int[m][m];
		Arrays.fill(graph, 0);
		
		for(int i=0;i<m;i++) {
			int x=s.nextInt();
			int y=s.nextInt();
			graph[x][y] = graph[y][x] = 1;
		}
		
		if(graph[a][b]==1)
			cnt=1;
		else {
			for(int i = 1; i < n+1; i++){
				
			}
		}
	}

}
