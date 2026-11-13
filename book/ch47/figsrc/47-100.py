import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,22,72,'même nb de chiffres','fixe','s'); text(ax,66,72,'même reste mod 12','sujet','s')
text(ax,44,44,'× 3','varie','m')
for dx,r,t,b in [(0,'fixe',('3','4'),('9','12')),(44,'sujet',('$x$','$y$'),('$3x$','$3y$'))]:
    box(ax,6+dx,54,13,10,'sujet',label=t[0]); box(ax,23+dx,54,13,10,'autre',label=t[1]); line(ax,[(19+dx,59),(23+dx,59)],'fixe')
    arrow(ax,(12.5+dx,53),(12.5+dx,30),'varie'); arrow(ax,(29.5+dx,53),(29.5+dx,30),'varie')
    rr='limite' if dx==0 else 'resultat'
    box(ax,6+dx,18,13,11,'sujet',label=b[0]); box(ax,23+dx,18,13,11,'autre',label=b[1])
    line(ax,[(19+dx,23.5),(23+dx,23.5)],rr,dash=(dx==0))
    text(ax,21+dx,11,'non liés' if dx==0 else 'liés',rr,'m')
save(fig,'47-100')
