import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,23,57,'s’arrêtent','resultat','l',weight='bold')
text(ax,65,57,'ne s’arrêtent pas','limite','l',weight='bold')
L=['3/4 = 0,75','1/5 = 0,2','1/8 = 0,125']; R=['1/3 = 0,333…','1/6 = 0,1666…','2/11 = 0,1818…']
for i in range(3):
    y=38-i*16
    box(ax,3,y,40,11,'resultat',label=L[i])
    box(ax,45,y,40,11,'limite',label=R[i])
save(fig,'08-082')
