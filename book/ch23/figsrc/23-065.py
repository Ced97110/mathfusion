import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,44,80,'12 équations','encre','m')
for i in range(12): box(ax,9+i*6,70,4,4,'fixe',True)
arrow(ax,(44,68),(44,60.8),'fixe')
box(ax,26,50,36,10,'sujet',True,r'$D=b^2-4ac$')
heads=[(r'$D>0$','deux solutions'),(r'$D=0$','une solution'),(r'$D<0$','aucune solution')]
for i,(h,c) in enumerate(heads):
    x=2+i*29
    box(ax,x,22,26,14,'resultat',True)
    text(ax,x+13,31,h,'resultat','m'); text(ax,x+13,26,c,'resultat','s')
    arrow(ax,(44,50),(x+13,36.8),'varie')
text(ax,44,14,'« discriminare » : séparer','sujet','m')
text(ax,44,7,'D sépare en trois groupes','encre','s')
save(fig,'23-065')
