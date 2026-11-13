import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
ox,oy,s=30,40,22
P=lambda a,b:(ox+a*s,oy+b*s)
line(ax,[P(-0.6,0),P(1.9,0)],'sujet',lw=1.6); line(ax,[P(0,-0.6),P(0,1.9)],'autre',lw=1.6)
line(ax,[P(1,0),P(1,1)],'fixe',dash=True); line(ax,[P(0,1),P(1,1)],'fixe',dash=True)
arrow(ax,P(0,0),P(1,0),'sujet',lw=1.6); arrow(ax,P(0,0),P(0,1),'autre',lw=1.6); arrow(ax,P(0,0),P(1,1),'resultat',lw=1.6)
text(ax,P(0.5,0)[0],P(0.5,0)[1]-4,r'$u$','sujet','m'); text(ax,P(0,0.5)[0]-4,P(0,0.5)[1],r'$w$','autre','m')
text(ax,P(0.62,0.5)[0]+3,P(0.62,0.5)[1]-2,r'$u+w$','resultat','m',ha='left')
text(ax,P(1.9,0)[0]+1,P(1.9,0)[1]+3,r'$U$','sujet','m',ha='left'); text(ax,P(0,1.9)[0]+3,P(0,1.9)[1],r'$W$','autre','m',ha='left')
text(ax,60,79,r'$U+W=\{u+w\}$','resultat','l')
text(ax,62,70,'toutes les sommes d’un','encre','s'); text(ax,62,65,'vecteur de U et d’un de W','encre','s')
text(ax,44,8,'sup : le plus petit sous-espace','encre','s'); text(ax,44,2.5,'qui contient U et W','encre','s')
save(fig,'80-057')
