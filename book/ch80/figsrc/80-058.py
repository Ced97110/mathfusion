import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
items=[('espace entier V','resultat'),('plans par l’origine','sujet'),('droites par l’origine','sujet'),('origine seule','fixe')]
for i,(t,r) in enumerate(items):
    y=62-i*18
    box(ax,4,y,50,12,r,label=t,size='s')
line(ax,[(58,74),(61,74),(61,8),(58,8)],'varie',lw=1.2)
text(ax,74,41,r'$L(V)$','varie','xl',weight='bold')
text(ax,74,30,'tous les','varie','s'); text(ax,74,25,'sous-espaces','varie','s'); text(ax,74,20,'de V','varie','s')
save(fig,'80-058')
