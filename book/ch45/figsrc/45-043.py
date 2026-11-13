import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
xs=[12,28,44,60,76]
top=['$-1$','$0$','$1$','$2$','$3$']; bot=['1/2','1','2','4','8']
for i,(x,a,b) in enumerate(zip(xs,top,bot)):
    hl = i in (0,4)
    disc(ax,x,64,5.5,'varie' if hl else 'sujet',label=a)
    box(ax,x-6,28,12,10,'varie' if hl else 'resultat',label=b,size='m')
    arrow(ax,(x,58),(x,39.5),'fixe')
text(ax,44,72,r'$n\mapsto 2^n$','fixe','m') if False else None
text(ax,44,16,r'$3+(-1)=2\ \mapsto\ 4$','varie','s')
text(ax,44,8,r'$8\times 1/2=4$','varie','s')
save(fig,'45-043')
