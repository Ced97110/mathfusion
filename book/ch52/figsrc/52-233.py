import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
V=[[0,4,2],[3,1,5]]
text(ax,56,57,'reste par 3','varie','s'); text(ax,8,28,'reste\npar 2','sujet','s')
for c in range(3): text(ax,35+c*15,47,str(c),'varie','m')
for r in range(2):
    text(ax,22,34-r*12+5,str(r),'sujet','m')
    for c in range(3):
        role='resultat' if (r==1 and c==2) else 'sujet' if r==1 else 'varie' if c==2 else 'fixe'
        box(ax,28+c*15,34-r*12,14,10,role,label=str(V[r][c]))
text(ax,44,10,r'lu : $5$, donc $n=5+6q$','resultat','s')
save(fig,'52-233')
