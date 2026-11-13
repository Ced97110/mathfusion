import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
box(ax,2,52,26,11,'sujet',label=r'$B(x,x)$',size='m'); text(ax,32,57.5,'=','encre','l')
box(ax,36,52,24,11,'varie',label=r'$2\,Q(x)$',size='m'); text(ax,64,57.5,'=','encre','l')
box(ax,68,52,18,11,'resultat',label=r'$0$',size='l')
text(ax,48,45,r'car $2=0$ dans ce corps','varie','s')
for r,c,v,role in [(0,0,'0','resultat'),(0,1,'b','fixe'),(1,0,'b','fixe'),(1,1,'0','resultat')]:
    box(ax,30+c*13,12+(1-r)*10,13,10,role,label=v if v=='0' else r'$b$',size='m')
text(ax,18,27,r'matrice de $B$','sujet','s')
text(ax,72,27,'diagonale\nnulle','resultat','s')
save(fig,'71-126')
