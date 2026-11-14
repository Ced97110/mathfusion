import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,24,64,40,12,'sujet',label='D₄ : 8 gestes',size='m')
# set 1: 4 vertices of a square
box(ax,10,14,22,22,'autre',fill=False)
for dx in (0,22):
    for dy in (0,22):
        disc(ax,10+dx,14+dy,2.2,'autre')
text(ax,21,6,'4 sommets','autre','s')
# set 2: 16 colourings
for i in range(4):
    for j in range(4):
        box(ax,52+i*8,16+j*8,6,6,'resultat',r=0.5,lw=0.6)
text(ax,68,8,'16 colorations','resultat','s',)
arrow(ax,(34,64),(21,41),'varie'); arrow(ax,(54,64),(68,52),'varie')
text(ax,20,54,'agit sur','varie','s'); text(ax,74,60,'agit sur','varie','s')
save(fig,'49-092')
