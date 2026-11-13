import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,44,77,r'$(x,\ y) \mapsto (x + b\,y,\ y)$','sujet','xl')
text(ax,44,69,r'ici $b$ = 1/2 et point (4, 6)','fixe','s')
rows=[('fixe',r'd’abord : lire $y$ = 6'),('sujet','ensuite : 1/2 × 6 = 3'),('varie','puis : 4 + 3 = 7'),('fixe',r'enfin : $y$ reste 6')]
for i,(r,l) in enumerate(rows):
    y=52-i*11
    box(ax,12,y,64,8,r,label=l)
    if i<3: arrow(ax,(44,y-0.2),(44,y-2.8),'fixe',lw=0.8)
box(ax,12,4,64,10,'resultat',label=r'$(4,\ 6) \mapsto (7,\ 6)$',size='l')
save(fig,'73-012')
