
import java.util.Scanner;


abstract class Shape {
    float area;
    float radius;
    float side1;
    float side2;
    abstract void area();
}

class Square extends Shape{

    @Override
    void area() {

        Scanner k=new Scanner(System.in);

        System.out.println("Enter the size of the side:");
        side1=k.nextInt();
        area=side1*side1;
        System.out.println("The area is:"+area);
    }
}
class Rectangle extends Shape {

    @Override
    void area() {

        Scanner k=new Scanner(System.in);

        System.out.println("Enter the size of the side1:\n"+"Enter the size of side2:");
        side1=k.nextInt();
        side2=k.nextInt();
        area=side1*side2;
        System.out.println("The area is:"+area);

    }
}
class Circle extends Shape {

    @Override
    void area() {
        Scanner k=new Scanner(System.in);

        System.out.println("Enter the size of the side1:\n"+"Enter the size of side2:");
        radius=k.nextInt();
        area= (float) (3.14*radius*radius);
        System.out.println("The area is:"+area);
    }
}
public class Praveen_Q14 {

    public static void main(String[] args) {
        int d;
        Scanner k=new Scanner(System.in);

            System.out.println("Choose Shape From Below which area You Want:\n" +
                    "1.Square\n" + "2.Rectangle\n" + "3.Circle\n" + "4.Exit");
            d = k.nextInt();
            Square s = new Square();
            Rectangle r = new Rectangle();
            Circle c = new Circle();

            if (d == 1) {
                s.area();
            }
            if (d == 2) {
                r.area();
            }
            if (d == 3) {
                c.area();
            }




    }
}
