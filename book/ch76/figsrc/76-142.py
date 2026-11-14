import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50); O=(30,6); s=5
P=lambda a,b:(O[0]+a*s,O[1]+b*s)
poly(ax,[P(0,0),P(2,3),P(-1,5),P(-3,2)],'varie')
arrow(ax,P(0,0),P(2,3),'varie',lw=1.2); arrow(ax,P(0,0),P(-3,2),'varie',lw=1.2)
text(ax,P(2,3)[0]+2,P(2,3)[1]-1,'(2, 3)','varie','s',ha='left'); text(ax,P(-3,2)[0]-2,P(-3,2)[1],'(−3, 2)','varie','s',ha='right')
text(ax,P(-0.5,2.6)[0],P(-0.5,2.6)[1],'aire 13','varie','m')
def grid(x0,y0,n,role):
    for i in range(n):
        for j in range(n): poly(ax,[(x0+i*5,y0+j*5),(x0+i*5+5,y0+j*5),(x0+i*5+5,y0+j*5+5),(x0+i*5,y0+j*5+5)],role)
grid(54,12,2,'sujet'); grid(67,12,3,'autre')
text(ax,59,8,r'$a^2=4$','sujet','m'); text(ax,74.5,8,r'$b^2=9$','autre','m')
text(ax,70,34,'4 + 9 = 13','resultat','l'); text(ax,70,41,r'$\det=a^2+b^2$','resultat','m')
save(fig,'76-142')
