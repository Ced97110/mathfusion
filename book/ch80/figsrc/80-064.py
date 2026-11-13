import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
ox,oy,s=44,50,14
P=lambda a,b:(ox+a*s,oy+b*s)
poly(ax,[P(-2.8,-1.8),P(2.8,-1.8),P(2.8,1.8),P(-2.8,1.8)],'fixe')
line(ax,[P(-2.5,0),P(2.5,0)],'sujet',lw=2.2); line(ax,[P(0,-1.6),P(0,1.6)],'autre',lw=2.2)
disc(ax,ox,oy,1.3,'fixe')
text(ax,P(2.0,0)[0],P(2.0,0)[1]+3.5,r'$U$','sujet','l'); text(ax,P(0,1.2)[0]+5,P(0,1.2)[1],r'$U^{\prime}$','autre','l')
text(ax,44,19,r'$U^{\prime}$ : un complément de $U$','autre','s')
text(ax,44,12,'U + U′ = tout le plan','resultat','s')
text(ax,44,5,'en commun : l’origine seule','fixe','s')
save(fig,'80-064')
