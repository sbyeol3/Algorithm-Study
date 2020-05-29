import java.util.Scanner;

public class Melody2920 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int melody[] = new int[8];
		boolean mix = false;
		boolean asc = true;
		
		for(int i=0;i<8;i++) {
			melody[i]=s.nextInt();
			if(i==0) {
				if(melody[i]!=1 && melody[i]!=8) {
					mix = true;
					break;
				}
				else if(melody[i]==1)
					asc = true;
				else
					asc = false;
				
				continue;
			}
			
			if(asc == true) {
				if(melody[i]!=melody[i-1]+1) {
					mix = true;
					break;
				}
			}
			else{
				if(melody[i]!=melody[i-1]-1) {
					mix = true;
					break;
				}
			}
				
		}
		
		s.close();
		if(mix == true)
			System.out.println("mixed");
		else {
			if(asc==true)
				System.out.println("ascending");
			else
				System.out.println("descending");
		}
	}

}
