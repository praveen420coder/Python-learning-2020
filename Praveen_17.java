import java.io.*;
import java.util.Scanner;
class Praveen_17
{
	public static void main(String[] args)
	{
		try
		{	
			System.out.println("Enter what you want to store  in text file:");
			Scanner sc = new Scanner(System.in);
			String name = sc.nextLine();
			FileOutputStream ob = new FileOutputStream("typeout.txt");
			byte xy[]=name.getBytes();
			ob.write(xy);
			ob.close();
			
			System.out.println();
			System.out.println("Read the context from text file: ");
			int i=0;
			FileInputStream ib =new FileInputStream("typeout.txt");	
			while((i=ib.read())!=-1)
				{
				System.out.print((char)i);
				}
		}
		catch(Exception e){}		
	}
}