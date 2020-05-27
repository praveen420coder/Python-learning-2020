import java.util.Scanner;

interface Drawable {
    Scanner k=new Scanner(System.in);
    final int RED=1;
    final int GREEN=2;
    final int BLUE=3;
   default void draw(int a){}

}
class Circle implements Drawable{
    Scanner k=new Scanner(System.in);
    private float x,y,r;
    public Circle()
    {
        System.out.println("Enter the Radius:");
        r=k.nextInt();
        System.out.println("Enter the Centre Coordinate:(x,y):");
        x=k.nextInt();
        y=k.nextInt();}
    @Override
    public void draw(int color) {

      int a=color;
        System.out.println("Circle drawn at center ("+x+","+y+") with radius "+r+" And color"+color);

    }

}
class Rectangle implements Drawable{
    Scanner k=new Scanner(System.in);

     private float x,y;
     public Rectangle(){

        System.out.println("Enter the sides(length,width):");
        x=k.nextInt();
        y=k.nextInt();

    }

    @Override
    public void draw(int color) {

        System.out.println("Rectangle drawn at with length"+x+"And width"+y+"with color"+color);
    }
}
class Praveen_15 {
    public static void main(String[] args) {
        int q;
        Scanner k=new Scanner(System.in);


        System.out.println("What You want to draw:\n1.Circle\n2.Rectangle");
        q=k.nextInt();
        if(q==1){
            int d;
            Circle cir = new Circle();
            System.out.println("Enter The Color:(RED=1,GREEN=2,BLUE=3):");
            d=k.nextInt();
            cir.draw(d);

        }
        if(q==2){
            int t;
            Rectangle rec = new Rectangle();
            System.out.println("Enter The Color:(RED=1,GREEN=2,BLUE=3):");
            t=k.nextInt();
            rec.draw(t);

        }
    }
}
