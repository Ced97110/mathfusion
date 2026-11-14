import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
w=19
text(ax,4,65,'avec des fractions','fixe','s',ha='left')
box(ax,4,50,w,10,'sujet',label='5/8 %')
arrow(ax,(23.5,54),(65.5,54),'varie'); text(ax,44,58,'× 1/100','varie','s')
box(ax,35,50,w,10,'fixe',label='5/8 × 1/100',size='s') if False else None
box(ax,66,50,w,10,'resultat',label='5/800')
box(ax,4,24,w,10,'sujet',label='0,625')
arrow(ax,(23.5,28),(65.5,28),'varie'); text(ax,44,32,'× 0,01','varie','s')
text(ax,4,39,'avec des décimaux','fixe','s',ha='left') if False else None
box(ax,66,24,w,10,'resultat',label='0,00625')
arrow(ax,(75.5,49),(75.5,35),'resultat',both=True); text(ax,73,42,'égaux','resultat','s',ha='right')
arrow(ax,(13.5,49),(13.5,35),'fixe',both=True); text(ax,16,42,'5/8 = 0,625','fixe','s',ha='left')
arrow(ax,(23.5,54),(65.5,54),'varie') if False else None
text(ax,4,19,'avec des décimaux','fixe','s',ha='left')
save(fig,'09-082')
