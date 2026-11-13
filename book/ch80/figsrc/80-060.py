import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
ox,oy,s=44,40,15
P=lambda a,b:(ox+a*s,oy+b*s)
poly(ax,[P(-1.8,-1.4),P(1.8,-1.4),P(1.8,1.4),P(-1.8,1.4)],'resultat')
line(ax,[P(-1.8,0),P(1.8,0)],'sujet',lw=2.2); line(ax,[P(0,-1.4),P(0,1.4)],'autre',lw=2.2)
text(ax,P(1.4,0)[0],P(1.4,0)[1]+3,r'$U$','sujet','m'); text(ax,P(0,1.1)[0]+4,P(0,1.1)[1],r'$W$','autre','m')
text(ax,P(-1.0,-0.8)[0],P(-1.0,-0.8)[1],'le plan entier','resultat','s')
text(ax,44,74,r'$U\vee W=U+W$','encre','l')
text(ax,44,10,'sup : le plus petit sous-espace','encre','s'); text(ax,44,4.5,'qui contient U et W','encre','s')
save(fig,'80-060')
