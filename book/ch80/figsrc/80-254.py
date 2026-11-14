import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
xs=(26,46,66)
for i,x in enumerate(xs):
    text(ax,x+9,68,'$y$ = %d'%(i+1),'encre','s')
    box(ax,x,48,18,10,'sujet',label=str((12,19,27)[i]),size='s')
    box(ax,x,30,18,10,'varie',label=('0','−1','1')[i],size='s')
text(ax,2,53,r'$g(y)$','sujet','s',ha='left')
text(ax,2,35,r'$\mu(y,3)$','varie','s',ha='left')
text(ax,44,18,r'$0\times12+(-1)\times19+1\times27=8$','resultat','s')
text(ax,44,8,r'$=f(3)$ : points du contrôle 3','resultat','s')
save(fig,'80-254')
