import java.util.*;
class Students extends Person
{
    char standerd;
    public Students()
    {
        System.out.println("Standerd of Student - ");
        standerd= s.next().charAt(0);
    }
    void display()
    {
            super.display();
                System.out.println("Standerd of Student - "+ standerd);
    }
}