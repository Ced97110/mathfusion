import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
vals=[[0,4,2],[3,1,5]]
X=[14,38,62]; Y=[26,8]
for b in range(3): text(ax,X[b]+11,46,rf'$b={b}$','encre','m')
for a in range(2):
    text(ax,7,Y[a]+8,rf'$a={a}$','encre','m')
    for b in range(3):
        box(ax,X[b],Y[a],22,16,'sujet' if vals[a][b]==0 else 'resultat',label=str(vals[a][b]),size='l')
text(ax,44,3,r'$k$ = nombre de pas jusqu’à la case','encre','s')
save(fig,'45-183')
