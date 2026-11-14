import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
for y,r,c,t in [(50,'resultat','2 + 3 = 5','énoncé : vrai'),(36,'limite','2 + 3 = 6','énoncé : faux'),(22,'fixe','2 + 3','expression : désigne 5'),(8,'fixe','combien font 2 + 3 ?','question : n’affirme rien')]:
    box(ax,3,y,34,10,r,label=c,size='l' if len(c)<10 else 's')
    arrow(ax,(38,y+5),(46,y+5),'fixe')
    text(ax,48,y+5,t,r,'s',ha='left')
save(fig,'42-064')
