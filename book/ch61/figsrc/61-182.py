import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
text(ax,4,83,'degré du corps','encre','s',ha='left')
ys=[66,47,28,9]; deg=[1,2,4,8]
roles=['sujet','varie','varie','resultat']
for y,d,r in zip(ys,deg,roles):
    box(ax,4,y,10*d,10,r,label=str(d),size='l')
for i in range(3):
    arrow(ax,(9,ys[i]),(9,ys[i+1]+10),'fixe')
    text(ax,14,ys[i]-4.5,'tracé %d : × 2 au plus'%(i+1),'fixe','s',ha='left')
text(ax,44,3.5,r'$2\times2\times2=8$ au plus','resultat','s')
save(fig,'61-182')
