import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
x0,y0,c=30,12,16
text(ax,x0+1.5*c,72,'image du 2e élément : 3 choix','varie','s')
text(ax,14,y0+1.5*c+8,'image du 1er\nélément :\n3 choix','sujet','s')
for i in range(3):
    for j in range(3):
        box(ax,x0+j*c,y0+i*c,c-1.5,c-1.5,'resultat',label='1',size='m')
        text(ax,x0+j*c+(c-1.5)/2,y0+i*c+2.2,'appl.','resultat','s')
text(ax,x0+1.5*c-0.7,5,r'$3\times3=9=3^2$ applications','resultat','m')
save(fig,'42-294')
