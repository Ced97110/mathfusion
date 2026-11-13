import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
X=[12,36,66]
for x,a,b in zip(X,['3','4','7'],['6','8','14']):
    box(ax,x-6,44,12,9,'sujet' if x<60 else 'resultat',label=a)
    box(ax,x-6,10,12,9,'autre' if x<60 else 'resultat',label=b)
    arrow(ax,(x,43),(x,20.5),'varie'); text(ax,x+8,31.5,r'$\times 2$','varie','s')
text(ax,24,48.5,'+','sujet','l'); text(ax,51,48.5,'=','sujet','l')
text(ax,24,14.5,'+','autre','l'); text(ax,51,14.5,'=','autre','l')
text(ax,44,60,'les sommes se correspondent','resultat','s')
save(fig,'42-302')
