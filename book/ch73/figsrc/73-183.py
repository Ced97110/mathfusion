import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
box(ax,4,52,10,10,'resultat',label='5',size='l'); text(ax,9,48,'inversible','resultat','s')
box(ax,30,52,10,10,'limite',label='0',size='l'); text(ax,35,48,'non inversible','limite','s')
box(ax,60,52,10,10,'sujet',label='1',size='l'); text(ax,65,48,'déterminant 1','sujet','s')
text(ax,44,38,r'$5\times3=15=3\times5$','sujet','m'); text(ax,44,33,'commutatif','sujet','s')
for i in range(2):
    for j in range(2): box(ax,8+8*i,12+8*j,8,8,'varie' if (i,j)==(1,1) else 'fixe')
text(ax,20,6,'n = 2 : case hors diagonale','varie','s')
box(ax,62,16,8,8,'fixe'); text(ax,66,6,'n = 1 : aucune','limite','s')
line(ax,[(63,17),(69,23)],'limite',lw=1.2); line(ax,[(63,23),(69,17)],'limite',lw=1.2)
save(fig,'73-183')
