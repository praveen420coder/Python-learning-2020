import java.util.Scanner;

public class Praveen1{

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter String : ");
	    String p = sc.nextLine();
		System.out.println("Enter Character : ");
		char c = sc.next().charAt(0);
		int count =0;
		for(int i=0;i<p.length();i++) {
			if(p.charAt(i)==c) {
				count++;
				int d=i;
			}
		}
		
		if(count==0) {
			System.out.println("character is not in the string");
		}
		else {
			System.out.println("At position:"+d);
			
		}

	}
}