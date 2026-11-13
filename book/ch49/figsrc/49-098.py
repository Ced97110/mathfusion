import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
x0,y0,c=14,18,4.5
for i in range(16):
    for j in range(4):
        box(ax,x0+i*c,y0+j*c,c,c,'varie' if (i,j)==(9,0) else 'fixe',lw=0.4,r=0.3)
    box(ax,x0+i*c,y0+4*c+0.8,c,c,'autre',lw=0.4,r=0.3)
for j in range(4): box(ax,x0-c-0.8,y0+j*c,c,c,'sujet',lw=0.4,r=0.3)
text(ax,x0+36,y0+4*c+c+5,'S : 16 colorations','autre','s')
text(ax,2,4,'G : 4 rotations','sujet','s',ha='left')
text(ax,86,4,'4 × 16 = 64 couples','resultat','s',ha='right')
text(ax,x0+9.5*c,11,'un couple (g, x)','varie','s')
arrow(ax,(x0+9.5*c,13.2),(x0+9.5*c,y0-0.3),'varie')
save(fig,'49-098')
