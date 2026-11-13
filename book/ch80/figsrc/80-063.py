import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for x,t in ((15,'droite'),(44,'plan'),(73,'espace')): text(ax,x,60,t,'encre','m',weight='bold')
# droite
line(ax,[(4,34),(26,34)],'fixe'); arrow(ax,(8,34),(22,34),'sujet',lw=1.6)
# plan
poly(ax,[(32,26),(54,26),(59,42),(37,42)],'fixe')
arrow(ax,(38,29),(52,29),'sujet',lw=1.6); arrow(ax,(38,29),(42,40),'sujet',lw=1.6)
# espace
o=(73,26); u=13
for p in ((1,0,0),(0,1,0),(0,0,1)): arrow(ax,iso(0,0,0,o,u),iso(*p,o,u),'sujet',lw=1.6)
for x,t in ((15,'1 vecteur'),(44,'2 vecteurs'),(73,'3 vecteurs')): text(ax,x,14,t,'sujet','s')
for x,n in ((15,1),(44,2),(73,3)): text(ax,x,6,r'$\dim U=%d$'%n,'resultat','m')
save(fig,'80-063')
