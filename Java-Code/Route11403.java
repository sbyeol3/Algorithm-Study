import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Route11403 {

	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int arr[][] = new int[N][N];
		int result[][] = new int[N][N];

		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				arr[i][j] = scan.nextInt();
			}
		}
    
		scan.close();
    
		for(int i = 0; i < N; i++){ // ---- 1
			Queue<Integer> queue = new LinkedList<>();
			boolean visited[] = new boolean[N];
			queue.add(i);
			while(!queue.isEmpty()){
				int point = queue.poll();
				for(int j = 0; j < N; j++){
					if(arr[point][j] == 1 && visited[j] != true){
						queue.add(j);
						visited[j] = true; // --- 2
						result[i][j] = 1; // --- 3
					}
				}
			}
		}

		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				System.out.print(result[i][j] + " ");
			}
			System.out.println();
		}
	}
	}