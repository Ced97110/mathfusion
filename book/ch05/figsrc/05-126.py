import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
f=numberline(ax,6,76,26,0,36,step=1,every=12)
ya,yb=58,42
for k in range(1,10):
    v=4*k; c='resultat' if v%12==0 else 'sujet'
    disc(ax,f(v),ya,1.5,c)
for k in range(1,7):
    v=6*k; c='resultat' if v%12==0 else 'autre'
    disc(ax,f(v),yb,1.5,c)
for v in (12,24,36): line(ax,[(f(v),ya-2),(f(v),27.5)],'resultat',dash=True)
text(ax,2,ya+6,'bus : toutes les 4 minutes','sujet','s',ha='left')
text(ax,2,yb+6,'bus : toutes les 6 minutes','autre','s',ha='left')
text(ax,f(24),72,'moments communs : multiples communs','resultat','s')
text(ax,82,19,'min','fixe','s')
save(fig,'05-126')
