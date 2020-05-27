import java.util.Scanner;

public class Numbers {
     float a;
     float b;
    Scanner k=new Scanner(System.in);
    public void setnumber()
    {
       System.out.println("Enter the first Number:");
        a=k.nextInt();
        System.out.println("Enter the second Number:");
        b=k.nextInt();
    }
   public void displayNumber()
   {
       System.out.println("The first number is:"+a);
       System.out.println("The second number is:"+b);
   }
}