import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(62)
u=9; O=(22,14)
P=lambda a,b:(O[0]+a*u,O[1]+b*u)
poly(ax,[P(0,0),P(2,1),P(1,3),P(-1,2)],'resultat')
arrow(ax,P(0,0),P(2,1),'sujet',lw=1.4); arrow(ax,P(0,0),P(-1,2),'varie',lw=1.4)
sq=1.1*u/ (5**0.5)*1.0
d1=(2/5**0.5,1/5**0.5); d2=(-1/5**0.5,2/5**0.5); s=3.2
line(ax,[(O[0]+d1[0]*s,O[1]+d1[1]*s),(O[0]+(d1[0]+d2[0])*s,O[1]+(d1[1]+d2[1])*s),(O[0]+d2[0]*s,O[1]+d2[1]*s)],'fixe')
text(ax,P(1.4,0.35)[0]+2,P(1.4,0.35)[1]-3.5,'$(2\\,;\\,1)$','sujet','s')
text(ax,P(-0.8,1.2)[0]-5,P(-0.8,1.2)[1]+1,'$(-1\\,;\\,2)$','varie','s')
text(ax,P(0.5,1.5)[0],P(0.5,1.5)[1],'aire $r^2=5$','resultat','s')
text(ax,P(1.1,0.2)[0]+7,P(1.1,0.2)[1]+8,'','fixe','s') if False else None
mat(ax,60,30,13,9,[['2','−1'],['1','2']],[['sujet','varie'],['sujet','varie']])
text(ax,73,52,'colonnes','fixe','s')
text(ax,73,24,'même longueur $r$','fixe','s')
text(ax,73,18,'à angle droit','fixe','s')
save(fig,'77-071')
