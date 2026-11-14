import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,45,54,'multiple de 3','varie','s'); text(ax,76,54,'élément de (7)','fixe','s')
def plus(x,y):
    line(ax,[(x-1.3,y),(x+1.3,y)],'fixe'); line(ax,[(x,y-1.3),(x,y+1.3)],'fixe')
def eq(x,y):
    line(ax,[(x-1.3,y+0.8),(x+1.3,y+0.8)],'fixe'); line(ax,[(x-1.3,y-0.8),(x+1.3,y-0.8)],'fixe')
for y,n,m,k,r in ((40,'19','3 × 4','7','sujet'),(26,'17','3 × 1','14','sujet'),(8,'19 − 17 = 2','3 × 3','−7','resultat')):
    box(ax,3,y,24,9,r,label=n,size='s')
    eq(31,y+4.5)
    box(ax,35,y,21,9,'varie',label=m,size='s')
    plus(60,y+4.5)
    box(ax,64,y,22,9,'fixe',label=k,size='s')
line(ax,[(3,21),(86,21)],'fixe',dash=True)
save(fig,'52-111')
