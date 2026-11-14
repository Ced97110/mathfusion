import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,30,48,r'$x=9$, $y=4$','fixe','s'); text(ax,30,41,r'rectangle $3\times 2$','sujet','s')
for i in range(3):
    for j in range(2):
        poly(ax,[(18+8*i,18+8*j),(26+8*i,18+8*j),(26+8*i,26+8*j),(18+8*i,26+8*j)],'sujet')
text(ax,30,13,r'$\sqrt{x}=3$','sujet','s'); text(ax,12.5,26,r'$\sqrt{y}=2$','sujet','s',rot=90)
box(ax,54,40,32,9,role='resultat',label='aire : 6',size='m'); arrow(ax,(70,40),(70,33),'varie')
box(ax,54,24,32,9,role='varie',label='carré : 36',size='m'); arrow(ax,(70,24),(70,17),'varie')
box(ax,54,8,32,9,role='sujet',label=r'$36=9\times 4$',size='m')
save(fig,'22-061')
