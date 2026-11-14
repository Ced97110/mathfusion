import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
box(ax,3,70,36,9,'sujet',label='premier théorème (Judson)',size='s'); box(ax,49,70,36,9,'sujet',label='théorème fondamental',size='s')
text(ax,44,74.5,'=','resultat','xl',weight='bold')
text(ax,21,62,r'$\mathbb{Z}/\ker f$','sujet','m'); text(ax,68,62,r'$\mathrm{im}\,f$','resultat','m'); text(ax,44,54,r'$\cong$','resultat','l')
L=['0, 4, 8, …','1, 5, 9, …','2, 6, 10, …','3, 7, 11, …']
for i in range(4):
    y=40-i*12
    box(ax,3,y,36,9,'sujet',label=L[i],size='s'); box(ax,60,y,16,9,'resultat',label=str(i)); arrow(ax,(39,y+4.5),(60,y+4.5),'varie')
save(fig,'48-124')
