import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cx,cy,R=24,34,15
for k in range(9):
    a=math.radians(90-40*k)
    disc(ax,cx+R*math.cos(a),cy+R*math.sin(a),3.3,'sujet' if k%3==0 else 'fixe',label=str(k),size='s')
box(ax,48,48,38,9,'fixe',label=r'$G$ : 9 éléments',size='s')
box(ax,48,34,38,9,'sujet',label=r'$\{0,3,6\}$ : 3 éléments',size='s')
arrow(ax,(67,48),(67,43.2),'fixe')
text(ax,67,26,r'$3<9$ : propre','resultat','s')
text(ax,67,18,'conjugué = lui-même','resultat','s')
text(ax,67,11,'donc normal','resultat','s')
save(fig,'50-226')
