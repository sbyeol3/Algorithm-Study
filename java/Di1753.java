import java.util.Arrays;
import java.util.Scanner;

public class Di1753 {
	static final int MAX = 10000;
	int count=0;
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int V = s.nextInt();
		int E = s.nextInt();
		int W[][] = new int[V+1][V+1];
		Arrays.fill(W[V], MAX);
		
		for(int i=1;i<(V+1);i++)
			W[i][i]=0;
		
		for(int i=0;i<E;i++) {
			int u = s.nextInt();
			int v = s.nextInt();
			int w = s.nextInt();
			W[u][v] = w;
		}
		int length[] = new int[V+1];
		length = dijkstra(V, W);
		
		for(int i=1;i<=V;i++)
			System.out.println(length[i]);

	}
	static int[] dijkstra (int n, int W[][]) {
		int i,j, vnear=0;
		int min;
		Edge e = new Edge();
		int touch[] = new int[n+1];
		int length[] = new int[n+1];
		
		for(i=2;i<=n;i++) { //ÃÊ±âÈ­
			touch[i]=1;
			touch[i]=W[1][i];
		}
		
		e.start=touch[vnear];
		e.end = vnear;
		
		for(i=1;i<n;i++) {
			min=MAX;
			for(j=2;j<=n;j++) 
				if(0<=length[j] && length[j]<min) {
					min=length[j];
					vnear=i;
				}
			
			for(j=2;j<=n;j++) {
				if(length[vnear]+W[vnear][j] < length[j] && W[min][i]>=0) {
					length[j] = length[vnear]+W[vnear][i];
				}
			}
			
			length[vnear]=-1;
		}
		return length;
	}
}

class Edge{
	int start;
    int end;
    int value;
    
    Edge(){
    	
    }

    Edge(int start, int end, int value) {
    	this.start = start;
        this.end = end;
        this.value = value;
    }
}