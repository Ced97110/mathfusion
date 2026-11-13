import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,41,76,r'$g$','sujet','xl'); text(ax,48,76,r'$x$','autre','xl')
text(ax,22,64,'élément de G','sujet','s'); text(ax,66,64,'point de S','autre','s')
line(ax,[(38,73),(26,66.5)],'sujet',lw=0.7); line(ax,[(50,73),(62,66.5)],'autre',lw=0.7)
text(ax,44,55,r'$gx$ : le point $x$ transformé par $g$','resultat','s')
# square vertices 1..4 clockwise from top-left
c=(30,26); a=12
V=[(c[0]-a,c[1]+a),(c[0]+a,c[1]+a),(c[0]+a,c[1]-a),(c[0]-a,c[1]-a)]
box(ax,c[0]-a,c[1]-a,2*a,2*a,'fixe',fill=False)
roles=['autre','resultat','fixe','fixe']
for i,v in enumerate(V):
    disc(ax,v[0],v[1],3.2,roles[i],label=str(i+1),size='s')
arrow(ax,(V[0][0]+3.4,V[0][1]),(V[1][0]-3.4,V[1][1]),'varie',curve=-0.3)
text(ax,71,36,r'$g$ = quart de tour','sujet','s')
text(ax,71,28,r'$x$ = sommet 1','autre','s')
text(ax,71,20,r'$gx$ = sommet 2','resultat','s')
save(fig,'49-094')
