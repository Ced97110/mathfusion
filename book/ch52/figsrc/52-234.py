import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
text(ax,44,43,'restes 2 par 3, dans l’ordre','sujet','s')
vals=[2,5,8,11]; roles=['limite','resultat','fixe','fixe']
for i,(v,r) in enumerate(zip(vals,roles)):
    x=3.75+i*21.5
    box(ax,x,20,16,11,r,label=str(v),dash=(i>1))
    if i: arrow(ax,(x-5.3,25.5),(x-0.2,25.5),'varie'); text(ax,x-2.75,35,'+ 3','varie','s')
text(ax,11.75,14,'pair','limite','s'); text(ax,33.25,14,'impair','resultat','s')
text(ax,33.25,7,'on s’arrête','resultat','s')
save(fig,'52-234')
