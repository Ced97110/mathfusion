import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for i,(n,role,lab,y) in enumerate([(3,'sujet','H : 3 éléments',56),(2,'autre','N : 2 éléments',42),(1,'resultat','H ∩ N : 1 élément',28)]):
    for j in range(n): disc(ax,7+8*j,y,3,role)
    text(ax,32,y,lab,role,'s',ha='left')
for r in range(3):
    for c in range(2): box(ax,65+9.5*c,48-9.5*r+ 8,8,8,'resultat')
text(ax,74,29,'H + N : 6 éléments','resultat','s')
box(ax,16,4,56,12,'fixe'); text(ax,44,10,r'$3\times 2\div 1=6$','encre','l')
save(fig,'48-160')
