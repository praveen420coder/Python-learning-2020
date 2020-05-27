import java.util.Scanner;
 class Praveen_16
{

 public  static void string()
 {
   String input="covid19";
   String s;
   Scanner sc = new Scanner(System.in); 
   System.out.println("Enter a string");
   s=sc.nextLine();
   
   try{
    if(s.length() < input.length())
      throw new NumberFormatException ("negative than string size");
    else if(s.length() > input.length())
      throw new NumberFormatException ("Greater than string size");
    else
     System.out.println(" String is " + s);
    }
    
   catch( NumberFormatException e)
     {
        System.out.println("Exception " + e.getMessage());
      }
  }
 public static void main(String args[])
  { 
    string();
    System.out.println("program continue");

  }
}