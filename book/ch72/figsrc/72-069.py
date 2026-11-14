import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
o=(44,30); k=8
fig,ax=canvas(78)
poly(ax,[iso(0,0,0,o,k),iso(3,0,0,o,k),iso(3,3,0,o,k),iso(0,3,0,o,k)],'sujet')
P=iso(1,2,3,o,k); M=iso(1,2,0,o,k); S=iso(1,2,-3,o,k)
line(ax,[P,M],'fixe',dash=True); line(ax,[M,S],'fixe',dash=True)
arrow(ax,iso(0,0,0,o,k),iso(0,0,1,o,k),'autre',lw=1.4)
disc(ax,*P,1.3,'varie'); disc(ax,*M,1.3,'sujet'); disc(ax,*S,1.3,'resultat')
text(ax,P[0]+3,P[1],r'$P$ = (1, 2, 3)','varie','s',ha='left')
text(ax,M[0]+3,M[1],r'$M$ = (1, 2, 0)','sujet','s',ha='left')
text(ax,S[0]+3,S[1],r'$S_uP$ = (1, 2, −3)','resultat','s',ha='left')
text(ax,o[0]-3,o[1]+5,r'$u$','autre','m',ha='right')
text(ax,iso(3,0,0,o,k)[0]+1,iso(3,0,0,o,k)[1]-3,r'plan $H$','sujet','s',ha='left')
save(fig,'72-069')
