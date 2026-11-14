import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
u=14; cx,cy=34,32
arrow(ax,(8,cy),(64,cy),'fixe',lw=0.8); arrow(ax,(cx,6),(cx,64),'fixe',lw=0.8)
text(ax,70,cy,'ℝ','fixe','s'); text(ax,cx+6,64,'Im','fixe','s') if False else None
text(ax,cx-5,cy+4,'0','fixe','s') if False else None
disc(ax,cx,cy+u,2.2,'resultat'); disc(ax,cx,cy-u,2.2,'resultat')
text(ax,cx+6,cy+u,r'$i$','resultat','m'); text(ax,cx+8,cy-u,r'$-i$','resultat','m')
text(ax,cx+8,cy+4,'aucune ici','limite','s') if False else None
text(ax,cx-17,cy+7,'sur ℝ : 0 racine','limite','s') if False else None
text(ax,44,72,r'$x^2+1=0$ : 2 racines dans ℂ','sujet','s')
text(ax,70,50,'ℂ : tout','sujet','s') if False else None
save(fig,'61-140')
