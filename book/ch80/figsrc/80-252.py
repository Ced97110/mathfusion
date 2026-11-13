import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
ws=[8,4,2,1]; u=76/15; x=6
rl=['sujet','autre','autre','autre']
leg=[r'8 = $f$ : par 2 seulement','4 : par 2 et 3 seulement','2 : par 2 et 5 seulement','1 : par 2, 3 et 5']
for i,w in enumerate(ws):
    box(ax,x,62,w*u,10,rl[i],label=str(w),size='s',r=0.5)
    box(ax,6,47-i*8,4,4,rl[i],r=0.3)
    text(ax,13,49-i*8,leg[i],rl[i],'s',ha='left')
    x+=w*u
brace(ax,6,82,74,'fixe',label=r'$g$ = 15 divisibles par 2',down=False)
text(ax,44,10,'8 + 4 + 2 + 1 = 15','resultat','m')
save(fig,'80-252')
