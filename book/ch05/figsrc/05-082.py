import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
# ligne 1 : petits nombres
text(ax,2,60,'PGCD de 12 et 18','encre','m',ha='left',weight='bold')
box(ax,2,46,20,9,'resultat',label='factoriser',size='s')
box(ax,24,46,20,9,'sujet',label='comparer',size='s')
text(ax,48,50.5,'immédiat','resultat','s',ha='left')
# ligne 2 : deux nombres de 300 chiffres
text(ax,2,36,'deux nombres de 300 chiffres','encre','m',ha='left',weight='bold')
box(ax,2,22,60,9,'limite',label='factoriser : très long',size='s')
box(ax,64,22,20,9,'sujet',label='comparer',size='s')
# axe du temps
arrow(ax,(2,10),(84,10),'fixe')
text(ax,2,4.5,'temps de calcul','fixe','s',ha='left')
save(fig,'05-082')
