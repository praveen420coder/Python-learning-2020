import java.awt.*;
import java.applet.*;
 
 
public class Move extends Applet implements Runnable {
     
     
    public void init() {
         
    }
     
    public void start() {
         
        Thread t = new Thread(this);
        t.start();
         
    }
     
    public void run() {
         
        Thread.currentThread().setPriority(Thread.MIN_PRIORITY);
        while (true){
             
            repaint();
            try {
                Thread.sleep(500);
            }
            catch (InterruptedException e) {
                //Do Nothing
            }
            Thread.currentThread().setPriority(Thread.MAX_PRIORITY); 
        }
         
    }
         
    public void paint(Graphics g) {
    g.drawOval(75,20,150,115);
    g.fillOval(90,25,20,20);
     
     
    }
 
}