import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
g=12
line(ax,[(3,g),(85,g)],'fixe',lw=1.2)
line(ax,[(6,g),(6,g+8)],'sujet',lw=1.8); line(ax,[(6,g),(18,g)],'sujet',lw=2.4)
line(ax,[(6,g+8),(18,g)],'fixe',dash=True)
line(ax,[(30,g),(30,g+32)],'autre',lw=1.8); line(ax,[(30,g),(78,g)],'autre',lw=2.4)
line(ax,[(30,g+32),(78,g)],'fixe',dash=True)
text(ax,12,g+13,'bâton 2 m','sujet','s'); text(ax,12,g-4,'ombre 3 m','sujet','s')
text(ax,54,g-4,'ombre 12 m','autre','s')
text(ax,49,g+36,r'$\frac{2}{3}=\frac{8}{12}$','encre','m')
text(ax,28,g+37,'mât : 8 m (calculé)','resultat','m',ha='right')
save(fig,'09-097')
