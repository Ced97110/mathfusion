import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,r'$\mathbb{O}$ : les parenthèses comptent','sujet','s')
bw=22;xs=[4,33,62]
A=[r'$(e_1e_2)e_3$',r'$e_4e_3$',r'$-e_6$']
B=[r'$e_1(e_2e_3)$',r'$e_1e_5$',r'$e_6$']
for i,x in enumerate(xs):
    box(ax,x,36,bw,10,'sujet',label=A[i])
    box(ax,x,10,bw,10,'autre',label=B[i])
    if i<2:
        arrow(ax,(x+bw+0.5,41),(xs[i+1]-0.5,41),'varie')
        arrow(ax,(x+bw+0.5,15),(xs[i+1]-0.5,15),'varie')
text(ax,73,28,r'$\neq$','limite','xl')
text(ax,20,28,'même produit, autre ordre','fixe','s')
save(fig,'78-177')
