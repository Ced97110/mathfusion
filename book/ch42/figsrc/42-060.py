import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
for cx,sep,nm in [(22,'∣','barre'),(66,':','deux-points')]:
    text(ax,cx-1.8,40,r'{$x$','sujet','l',ha='right'); text(ax,cx,40,sep,'varie','xl',weight='bold'); text(ax,cx+1.8,40,r'$x$ pair}','sujet','l',ha='left')
    text(ax,cx,33.5,nm,'varie','s')
    arrow(ax,(cx+(8 if cx<40 else -8),30),(44,18),'fixe')
text(ax,44,40,'=','encre','xl')
box(ax,32,6,24,11,'resultat',label='{2, 4, 6}',size='l')
text(ax,60,11.5,r'pour $x$ de 1 à 6','fixe','s',ha='left')
save(fig,'42-060')
