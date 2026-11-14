import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
s=4
def panel(ox,oy,lines,name,rt):
    P=lambda x,y:(ox+s*x,oy+s*y)
    arrow(ax,P(0,0),P(6.2,0),'fixe',lw=0.6); arrow(ax,P(0,0),P(0,8.6),'fixe',lw=0.6)
    for (a,b,role) in lines:
        xe=min(6,b/-a if a<0 else 6)
        line(ax,[P(0,b),P(xe,b+a*xe)],role,lw=1.3)
    text(ax,ox+14,oy+39,name,'encre','m')
    return P
Pa=panel(8,16,[(-1,5,'sujet'),(-2,8,'autre')],'Système A',0)
Pb=panel(50,16,[(-1,5,'sujet'),(-1,8,'autre')],'Système B',0)
disc(ax,*Pa(3,2),1.3,'resultat')
text(ax,Pa(4.5,0.3)[0]+3,Pa(4.5,0.3)[1]+8,r'pente $-2$','autre','s')
text(ax,Pa(3.4,3.2)[0]+9,Pa(3.4,3.2)[1]+3,r'pente $-1$','sujet','s')
text(ax,Pb(2.2,6.8)[0]+11,Pb(2.2,6.8)[1],r'pente $-1$','autre','s')
text(ax,Pb(2.8,1.6)[0]+11,Pb(2.8,1.6)[1]-1,r'pente $-1$','sujet','s')
text(ax,28,8,r'$-1 - (-2) = 1$','resultat','s')
text(ax,70,8,r'$-1 - (-1) = 0$','fixe','s')
save(fig,'24-076')
