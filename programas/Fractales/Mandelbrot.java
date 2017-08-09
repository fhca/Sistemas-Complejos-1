// This example is from the book _Java AWT Reference_ by John Zukowski.
// Written by John Zukowski.  Copyright (c) 1997 O'Reilly & Associates.
// You may study, use, modify, and distribute this example for any purpose.
// This example is provided WITHOUT WARRANTY either expressed or
import java.awt.*;
import java.awt.image.*;
import java.applet.*;

public class Mandelbrot extends Applet implements Runnable {
    Thread animator;
    Image im1, im2, im3, im4;
    public void start() {
        animator = new Thread(this);
        animator.start();
    }
    public synchronized void stop() {
        animator = null;
    }
    public void paint(Graphics g) {
        if (im1 != null)
            g.drawImage(im1, 0, 0, null);
        if (im2 != null)
            g.drawImage(im2, 0, getSize().height / 2, null);
        if (im3 != null)
            g.drawImage(im3, getSize().width / 2, 0, null);
        if (im4 != null)
            g.drawImage(im4, getSize().width / 2, getSize().height / 2, null);
    }
    public void update (Graphics g) {
        paint (g);
    }
    public synchronized void run() {
        Thread.currentThread().setPriority(Thread.MIN_PRIORITY);
        int width = getSize().width / 2;
        int height = getSize().height / 2;
        byte[] pixels = new byte[width * height];
        int index = 0;
        int iteration=0;
        double a, b, p, q, psq, qsq, pnew, qnew;
        byte[] colorMap = {(byte)255, (byte)255, (byte)255, // white
                           (byte)0, (byte)0, (byte)0};      // black
        MemoryImageSource mis = new MemoryImageSource(
            width, height, 
            new IndexColorModel (8, 2, colorMap, 0, false, -1),
            pixels, 0, width);
        mis.setAnimated(true);
        im1 = createImage(mis);
        im2 = createImage(mis);
        im3 = createImage(mis);
        im4 = createImage(mis);
        // Generate Mandelbrot
        final int ITERATIONS = 16;
        for (int y=0; y<height; y++) {
            b = ((double)(y-64))/32;
            for (int x=0; x<width; x++) {
                a = ((double)(x-64))/32;
                p=q=0;
                iteration = 0;
                while (iteration < ITERATIONS) {
                    psq = p*p;
                    qsq = q*q;
                    if ((psq + qsq) >= 4.0)
                        break;
                    pnew = psq - qsq + a;
                    qnew = 2*p*q+b;
                    p = pnew;
                    q = qnew;
                    iteration++;
                }
                if (iteration == ITERATIONS) {
                    pixels[index] = 1;
                    mis.newPixels(x, y, 1, 1);
                    repaint();
                }
                index++;
            }
        }
    }
}