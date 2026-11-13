import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
d=12
text(ax,44,88,r'à prouver : $2^{n} > n+4$','sujet','m',weight='bold')
text(ax,44,d+66,r'$n$ = 3 : 8 > 7, on double','sujet','m')
u=4
box(ax,6,d+48,16*u,7,'sujet',label=r'$2^{n+1}$ = 16')
text(ax,79,d+51.5,'16 > 14','fixe','s')
line(ax,[(62,d+41),(62,d+48)],'fixe',dash=True)
box(ax,6,d+34,8*u,7,'resultat',label=r'$n+5$ = 8')
box(ax,38,d+34,6*u,7,'varie',lw=1.4,label=r'$n+3$ = 6 > 0',size='s')
text(ax,75,d+37.5,r'$2n+8$ = 14','fixe','s')
box(ax,6,d+14,8*u,7,'resultat',label=r'$(n+1)+4$ = 8')
line(ax,[(38,d+21),(38,d+34)],'fixe',dash=True)
text(ax,42,d+17.5,r'14 > 8 : on retire $n+3$ > 0','fixe','s',ha='left')
text(ax,44,d+3,r'donc $2^{n+1} > (n+1)+4$','resultat','m')
text(ax,44,d-3,"c'est l'affirmation au rang $n+1$",'resultat','s')
save(fig,'01-140')
