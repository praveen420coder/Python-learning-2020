import java.util.*;
class Teacher extends Person
{   Scanner s= new Scanner(System.in);
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