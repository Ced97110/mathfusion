import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
box(ax,2,30,38,12,'sujet',label=r'$5=2\times2+1$'); text(ax,21,26,'reste 1 : ligne 1','sujet','s')
box(ax,2,10,38,12,'autre',label=r'$5=1\times3+2$'); text(ax,21,6,'reste 2 : colonne 2','autre','s')
X=[54,65,76]; Y=[26,14]
for b in range(3): text(ax,X[b]+5,44,rf'$b={b}$','autre' if b==2 else 'fixe','s')
for a in range(2):
    text(ax,48,Y[a]+5,rf'$a={a}$','sujet' if a==1 else 'fixe','s')
    for b in range(3):
        hit=(a==1 and b==2)
        box(ax,X[b],Y[a],10,10,'resultat' if hit else 'fixe',label='5' if hit else None,size='m',lw=0.6,r=0.5)
text(ax,70,6,r'pas 5 : $(1,2)$','resultat','m')
save(fig,'45-186')
