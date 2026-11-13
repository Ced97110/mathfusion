import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
rows=[(70,r'$4x+1-3x=-8$','sujet','départ'),(50,r'$x+1=-8$','varie','regrouper'),(32,r'$x=-9$','resultat','retirer 1 des deux côtés')]
for y,s,r,l in rows:
    box(ax,8,y-5,44,10,r,label=s,size='l'); text(ax,56,y,l,r,'s',ha='left')
arrow(ax,(30,64),(30,56),'varie'); arrow(ax,(30,44),(30,38),'varie')
text(ax,44,12,r'$4\times(-9)+1-3\times(-9)=-8$','resultat','m')
text(ax,44,5,'vérification','resultat','s')
arrow(ax,(30,26),(30,18),'resultat')
save(fig,'16-082')
