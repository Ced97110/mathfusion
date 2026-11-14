import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,20,52,r'$3+3=6$','sujet','l'); text(ax,66,52,r'$A\cup A=A$','sujet','l')
for i in range(3):
    disc(ax,5+i*6,40,2.3,'sujet'); disc(ax,27+i*6,40,2.3,'varie')
text(ax,22,40,'+','encre','m')
brace(ax,2.7,29.3+6*0+12,34,'fixe')
text(ax,19,26,'6 objets comptés','fixe','s')
box(ax,48,34,14,12,'sujet',label='3'); text(ax,66,40,r'$\cup$','varie','l'); box(ax,70,34,14,12,'sujet',label='3')
arrow(ax,(66,32),(66,23),'resultat'); box(ax,59,10,14,12,'resultat',label='3'); text(ax,66,5,'un seul 3','resultat','s')
save(fig,'42-150')
