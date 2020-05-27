import java.util.*;
class Person 
{   Scanner s= new Scanner(System.in);
    String name;
    int age;
    Person()
    {
          System.out.println("Enter Name:");
          name=s.next();
          System.out.println("Enter Age:");
          age=s.nextInt();
    }
    void display()
    {
        System.out.println( "Name:"+ name);
        System.out.println("Age:"+ age);
    }  
}

class Students extends Person
{   //Scanner s= new Scanner(System.in);
    char standerd;
    public Students()
    {
        System.out.println("Standerd of Student:");
        standerd= s.next().charAt(0);
    }
    void display()
    {
            super.display();
                System.out.println("Standerd of Student:"+ standerd);
    }
}
class Teacher extends Person
{  //Scanner s= new Scanner(System.in);
    String post;
    public Teacher()
    {   
        System.out.println("Post of Teacher:");
        post= s.next();
    }
    void display()
    {           super.display();
                System.out.println("Post of Teacher:"+ post);
    }
}
class Praveen_Q13
{
    public static void main(String[] args)
    {
     System.out.println("Teacher Information");
     Teacher t = new Teacher();
     t.display();
     System.out.println("Student Information");
     Students x= new Students();
     x.display();
    }
}    
