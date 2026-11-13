import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
s=3
def grille(x0,y0,cols,rows,role='sujet'):
    for c in range(cols):
        for r in range(rows): box(ax,x0+s*c,y0+s*r,s,s,role,r=0.3,lw=0.5)
text(ax,44,77,'12 carreaux à chaque ligne','encre','s')
def etiq(y,d,q,role='resultat',x=None,ha='left'):
    text(ax,7,y,f'd = {d}','varie','s')
    text(ax,x,y,q,role,'s',ha=ha)
grille(13,61,3,4); etiq(67,3,'q = 4',x=25)
grille(13,47,4,3); etiq(51.5,4,'q = 3',x=28)
grille(13,33,5,2); grille(13,39,2,1,'limite'); etiq(37.5,5,'q = 2, reste 2','limite',x=31)
grille(13,22,6,2); etiq(25,6,'q = 2',x=34)
grille(13,14,12,1); etiq(15.5,12,'q = 1',x=52)
for c in range(24):
    box(ax,13+s*c,6,s,1.5,'limite',r=0.3,lw=0.5)
text(ax,7,6.75,'d = 24','varie','s')
text(ax,49,10.5,'q = ½ rangée','limite','s')
arrow(ax,(82,72),(82,22),'varie')
text(ax,79,47,'d grandit','varie','s',rot=90)
save(fig,'03-117')
