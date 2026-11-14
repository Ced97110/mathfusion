import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
X=lambda i:6+(i-1)*2.6
kept=[1,7,11,13,17,19,23,29]
line(ax,[(X(1)-2,26),(X(30)+2,26)],'fixe',lw=0.5)
for i in range(1,31):
    if i in kept: disc(ax,X(i),26,1.2,'resultat'); text(ax,X(i),20,str(i),'resultat','s')
    else: disc(ax,X(i),26,0.6,'fixe')
text(ax,44,40,'8 entiers gardés','resultat','l',weight='bold')
text(ax,44,33,'rayés : multiples de 2, 3 ou 5','fixe','s')
save(fig,'80-009')
