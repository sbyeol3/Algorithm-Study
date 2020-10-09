package prev;

import java.util.Scanner;
import java.util.ArrayList;
class ProdNode {
	public int time;
	public ArrayList<ProdNode> afterNodes = new ArrayList<ProdNode>();
	
	public ProdNode(int time) {
		this.time = time;
	}
}
public class J201810 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int R = sc.nextInt();
		ProdNode[] nodeList = new ProdNode[N];
		int head = 0;
		
		for (int i=0;i<N;i++) {
			int time = sc.nextInt();
			ProdNode node = new ProdNode(time);
			nodeList[i] = node;
		}
		
		for (int i=0;i<R;i++) {
			int pre = sc.nextInt();
			int after = sc.nextInt();
			nodeList[pre-1].afterNodes.add(nodeList[after-1]);
		}
		int goal = sc.nextInt();
		ProdNode current = nodeList[0];
		int total = current.time;
		while (current.afterNodes.size() > 0) {
			if (current.afterNodes.size() == 1) {
				current = current.afterNodes.get(0);
			} else {
				int max = 0, maxIdx = -1;
				int length = current.afterNodes.size();
				for (int i=0;i<length;i++) {
					ProdNode temp = current.afterNodes.get(i);
					if (temp.time > max) {
						max = temp.time;
						maxIdx = i;
					}
				}
				current = current.afterNodes.get(maxIdx);
			}
			total += current.time;
		}
		
		System.out.println(total);
		sc.close();
	}

}
