import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,62,r'divisé par 3, sans reste 0','encre','s')
cx=[16,44,72]
for i,x in enumerate(cx): box(ax,x-12,46,24,8,'sujet',label=f'étape {i+1}',size='s')
bx=[30,58]
for i,x in enumerate(bx): box(ax,x-12,22,24,8,'fixe',label=f'reste {i+1}',size='s')
arrow(ax,(cx[0],45.5),(bx[0]-3,30.5),'varie'); arrow(ax,(cx[1],45.5),(bx[0]+3,30.5),'varie')
arrow(ax,(cx[2],45.5),(bx[1]+3,30.5),'sujet')
text(ax,14,36,'même reste','varie','s')
box(ax,4,4,80,10,'resultat',label='deux restes égaux : ça boucle',size='s')
text(ax,44,17.5,'(reste 0 avant : arrêt)','resultat','s')
save(fig,'08-080')
