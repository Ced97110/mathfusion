import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,11,45,r'$\circ$','encre','l')
cw,ch,gp=15,11,1.2; xs=[19.2,19.2+cw+gp]; ys=[27.8,27.8-ch-gp]
names=[r'$1_S$',r'$\alpha$']
for j in range(2): box(ax,xs[j],40,cw,10,'fixe',label=names[j])
for i in range(2):
    box(ax,4,ys[i],14,ch,'fixe',label=names[i])
    for j in range(2):
        r='sujet' if i==j else 'varie'
        box(ax,xs[j],ys[i],cw,ch,r,label=names[0] if i==j else names[1])
arrow(ax,(39,30),(30.5,24.5),'resultat',both=True)
text(ax,70,31,'les deux ordres','resultat','s'); text(ax,70,26,r'donnent $\alpha$','resultat','s')
text(ax,44,6,r'$2!=2$ éléments : $1_S$ et $\alpha$','encre','s')
save(fig,'44-265')
