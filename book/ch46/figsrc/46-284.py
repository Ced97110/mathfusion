import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,r'$\varphi(12)=4$ : exposant 4','sujet','m')
for i in range(4):
    box(ax,6+i*14,38,10,9,'sujet',label='5')
    if i<3: text(ax,6+i*14+12,42.5,r'$\times$','varie','m')
arrow(ax,(62,42.5),(68,42.5),'varie')
box(ax,69,37,16,11,'fixe',label='625')
text(ax,44,28,r'$625 = 52 \times 12 + 1$','encre','m')
box(ax,6,8,56,11,'fixe',label=r'$52 \times 12$')
box(ax,64,8,14,11,'resultat',label='1')
text(ax,71,3.5,'reste','resultat','s')
save(fig,'46-284')
