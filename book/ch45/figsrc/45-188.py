import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
X=[22,48]; Y=[30,12]
for b in range(2): text(ax,X[b]+12,51,rf'$b={b}$','encre','m')
cells={(0,0):'0',(1,1):'1'}
for a in range(2):
    text(ax,14,Y[a]+8,rf'$a={a}$','encre','m')
    for b in range(2):
        if (a,b) in cells: box(ax,X[b],Y[a],24,16,'resultat',label=cells[(a,b)],size='l')
        else: box(ax,X[b],Y[a],24,16,'fixe',label='jamais',size='s',dash=True)
arrow(ax,(52,27),(43,32),'varie')
text(ax,44,8.5,r'2e pas : retour en $(0,0)$','varie','m')
text(ax,44,3.5,'seulement 2 cases sur 4','limite','m')
save(fig,'45-188')
