import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,r'$I$ : multiples de 4','sujet')
y=44; f=numberline(ax,8,76,y,0,16,step=4,arrow_right=False)
for v in (0,4,12,16): disc(ax,f(v),y,1.8,'sujet')
disc(ax,f(8),y,2.4,'varie'); text(ax,f(8),y+6,r'$b$ = 8','varie','s')
for x,l,r in ((3,r'$8\in I$','sujet'),(32,r'$8-0\in I$','fixe'),(61,r'$8\equiv 0$','resultat')):
    box(ax,x,10,24,12,r,label=l)
arrow(ax,(27,16),(32,16),'varie'); arrow(ax,(56,16),(61,16),'varie')
save(fig,'52-037')
