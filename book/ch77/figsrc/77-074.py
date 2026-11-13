import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(66)
u=5; O=(12,33)
P=lambda a,b:(O[0]+a*u,O[1]+b*u)
arrow(ax,(2,33),(58,33),'fixe',lw=0.8); arrow(ax,(12,6),(12,62),'fixe',lw=0.8)
text(ax,52,28.5,'axe réel','fixe','s'); text(ax,12,64,'','fixe','s') if False else None
line(ax,[P(3,4),P(3,-4)],'fixe',dash=True)
disc(ax,*P(3,4),1.6,'sujet'); disc(ax,*P(3,-4),1.6,'autre')
text(ax,P(3,4)[0]+3,P(3,4)[1]+1,'$3+4i$','sujet','m',ha='left')
text(ax,P(3,-4)[0]+3,P(3,-4)[1]-1,'$3-4i$','autre','m',ha='left')
text(ax,P(3,0)[0],P(3,0)[1]-3.5,'3','fixe','s')
text(ax,72,50,'$\\lambda^2-6\\lambda+25=0$','fixe','s') if False else None
text(ax,72,47,'$\\frac{6\\pm8i}{2}$','resultat','l')
text(ax,72,38,'$a\\pm bi$','resultat','m')
text(ax,P(0,0)[0]-1,P(0,0)[1]+36*0,'','fixe','s') if False else None
text(ax,72,20,'conjugués','resultat','s')
save(fig,'77-074')
