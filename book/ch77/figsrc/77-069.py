import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(72)
u=4.5; O=(26,32); A=(O[0]+3*u,O[1]); B=(O[0]+3*u,O[1]+4*u)
poly(ax,[O,A,B],'encre')
poly(ax,[O,A,(A[0],A[1]-3*u),(O[0],O[1]-3*u)],'sujet')
poly(ax,[A,B,(B[0]+4*u,B[1]),(A[0]+4*u,A[1])],'sujet')
poly(ax,[O,B,(B[0]-4*u,B[1]+3*u),(O[0]-4*u,O[1]+3*u)],'resultat')
text(ax,O[0]+1.5*u,O[1]-1.5*u,'9','sujet','l')
text(ax,A[0]+2*u,O[1]+2*u,'16','sujet','l')
text(ax,O[0]+1.5*u-2*u,O[1]+2*u+1.5*u,'25','resultat','l')
text(ax,O[0]+1.5*u,O[1]+2.4,'3','sujet','s')
text(ax,A[0]-2.4,O[1]+2*u,'4','sujet','s')
text(ax,73,52,'$|z|=5$','resultat','m')
text(ax,73,45,'$N(z)=25$','resultat','m')
text(ax,73,38,'$a^2+b^2$','fixe','s')
save(fig,'77-069')
