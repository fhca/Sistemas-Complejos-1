# encoding: latin-1

from Tkinter import *
import math

def mitad(a,b,p=2./3.):
    """ Devuelve el punto a*p+b*(1-p). """
    return (a[0]*p+b[0]*(1-p),a[1]*p+b[1]*(1-p))

def carp(e):
    """ Devuelve arreglo de vértices luego de una iteración de Carp. """
    r=[]
    while e:
        (a,b,c,d)=e[:4]
        abb=mitad(a,b)
        aab=mitad(b,a)
        add=mitad(a,d)
        aad=mitad(d,a)
        aa=(abb[0],add[1])
        bb=(aab[0],add[1])
        cc=(aab[0],aad[1])
        dd=(abb[0],aad[1])
        bcc=(b[0],bb[1])
        bbc=(b[0],cc[1])
        ccd=(dd[0],d[1])
        cdd=(cc[0],d[1])
        r.extend([a,abb,aa,add])  # NO
        r.extend([abb,aab,bb,aa]) # N
        r.extend([aab,b,bcc,bb])  # NE
        r.extend([bb,bcc,bbc,cc]) # E
        r.extend([cc,bbc,c,cdd]) # SE
        r.extend([dd,cc,cdd,ccd]) # S
        r.extend([aad,dd,ccd,d])  # SO
        r.extend([add,aa,dd,aad]) # O
        del e[:4]
    return r


def pinta(e):
    canvas = Canvas(width=550, height=550, bg='white')  
    canvas.pack(expand=YES, fill=BOTH)                  
    while e:
        canvas.create_polygon(*e[:4],fill="blue",  outline="blue")
        del e[:4]
    mainloop()

def main():
    e=[(10,10),(500,10),(500,500),(10,500)]
    for i in xrange(4):
        e=carp(e)
    pinta(e)

if __name__=="__main__":
    main()
