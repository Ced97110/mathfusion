import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,52,r'0 = 0 $\times$ $q$ ?','sujet','l')
f=numberline(ax,6,82,20,0,300,50,every=2,arrow_right=False)
ax.plot([6,82],[20,20],color=FILL['resultat'],lw=3,zorder=1.2,solid_capstyle='butt')
arrow(ax,(82,20),(86,20),'fixe',lw=0.9)
for x,q in ((14,5),(44,31),(74,286)):
    text(ax,x,40,rf'0 $\times$ {q} = 0','resultat','s')
    arrow(ax,(x,37),(f(q),22.5),'resultat')
    disc(ax,f(q),20,1.3,'resultat')
text(ax,44,10,r'tous les $q$ passent le test','resultat','s')
text(ax,44,5,'aucun ne se détache','limite','s')
save(fig,'03-106')
