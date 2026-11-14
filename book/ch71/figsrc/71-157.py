import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(62)
text(ax,44,57,r'retirer 2 fois $u_1$','encre','m')
o=(24,26); u=9
P=lambda a,b:(o[0]+a*u,o[1]+b*u)
line(ax,[o,P(2,2)],'fixe',dash=True)
arrow(ax,o,P(1,1),'sujet'); arrow(ax,o,P(3,1),'varie'); arrow(ax,P(2,2),P(3,1),'resultat'); arrow(ax,o,P(1,-1),'resultat')
k=3*math.sqrt(0.5)
line(ax,[(o[0]+k,o[1]+k),(o[0]+2*k,o[1]),(o[0]+k,o[1]-k)],'fixe')
text(ax,P(1,1)[0]-5,P(1,1)[1]+1,r'$u_1$','sujet','m'); text(ax,P(3,1)[0]+3,P(3,1)[1],r'$x$','varie','m')
text(ax,P(2,2)[0],P(2,2)[1]+4,r'$2u_1$','fixe','m'); text(ax,P(1,-1)[0],P(1,-1)[1]-4,r'$x-2u_1$','resultat','m')
text(ax,62,12,r'$B(x-2u_1,u_1)=0$','resultat','m')
save(fig,'71-157')
