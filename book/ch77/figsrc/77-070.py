import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(60)
u=7; O=(30,22)
P=lambda a,b:(O[0]+a*u,O[1]+b*u)
arrow(ax,(6,22),(56,22),'fixe',lw=0.7); arrow(ax,(30,6),(30,54),'fixe',lw=0.7)
ax.add_patch(Circle(O,5**0.5*u,ec=COL['fixe'],fc='none',lw=0.8,ls='--',zorder=1))
poly(ax,[P(0,0),P(2,1),P(1,3),P(-1,2)],'varie')
poly(ax,[P(0,0),P(1,0),P(1,1),P(0,1)],'sujet')
text(ax,P(0.5,0.5)[0],P(0.5,0.5)[1],'1','sujet','s')
text(ax,P(0.5,1.7)[0],P(0.5,1.7)[1],'5','varie','l')
text(ax,P(1.6,-0.35)[0],P(1.6,-0.35)[1],'$r=\\sqrt{5}$','fixe','s')
text(ax,P(2,1)[0]+3,P(2,1)[1]+2,'$2+i$','varie','s',ha='left')
text(ax,72,42,'$5=2^2+1^2$','resultat','s')
text(ax,72,35,'$N(2+i)=5$','resultat','s')
text(ax,72,12,'aire = 5','varie','s') if False else None
save(fig,'77-070')
