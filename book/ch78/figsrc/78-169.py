import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,54,r'$n=6,\ q=2$','sujet','m')
xs=[24,36,48]
for x in xs: disc(ax,x,40,4.5,'sujet')
text(ax,62,40,r'$\Phi_6(2)=3$','sujet','m',ha='left')
disc(ax,24,22,4.5,'resultat')
for x in xs[1:]: disc(ax,x,22,4.5,'limite',fill=False,label=r'$\times$')
text(ax,62,22,r'$q-1=1$','resultat','m',ha='left')
box(ax,16,12.5,40,19,'limite',fill=False,dash=True)
text(ax,44,6,'un groupe de 3 ne rentre pas','limite','s')
save(fig,'78-169')
