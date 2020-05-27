import java.util.Scanner;

class Airthmatic extends Numbers
{
    private float c;
    Scanner x=new Scanner(System.in);
    public void operation()
    {
        System.out.println("Which operation YOu want to perform (select the Number):");
        System.out.println("1.Addition\n" +
                "2.subtraction\n" + "3.Multiplication\n"+"4.Division");
        float d = x.nextInt();
        if(d ==1)
        {
            c=a+b;
        }
        if(d ==2)
        {
            c=a-b;
        }
        if(d ==3)
        {
            c=a*b;
        }
        if(d ==4)
        {
            c=a/b;
        }

    }
    public float getresult()
    {
        return c;
    }

    public static void main(String[] args)
    {
        Airthmatic obj;
        obj = new Airthmatic();
        obj.setnumber();
        obj.displayNumber();
        obj.operation();
        System.out.println("The result is:"+obj.getresult());


    }

}
