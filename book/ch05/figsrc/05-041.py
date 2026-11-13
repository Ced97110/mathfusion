import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
X=lambda v: 14+(v-20)*6
def panel(yA,yB,title,trole,closedA,rA,rB,eqA,eqB,concl,crole):
    text(ax,44,yA+8,title,trole,'m')
    line(ax,[(X(20),yA),(X(25),yA)],'sujet',lw=2.4); line(ax,[(X(25),yB),(X(30),yB)],'sujet',lw=2.4)
    disc(ax,X(20),yA,1.4,'sujet'); disc(ax,X(30),yB,1.4,'sujet',fill=False); disc(ax,X(25),yB,1.4,rB)
    disc(ax,X(25),yA,1.4,rA,fill=closedA)
    if eqA: text(ax,X(22.5),yA+3.6,eqA,'limite','s')
    text(ax,X(27.5),yB+3.6,eqB,'sujet' if not eqA else 'limite','s')
    text(ax,44,yB-5,concl,crole,'s')
panel(60,52,r'$0\leq r<5$','sujet',False,'sujet','resultat',None,r'$5\times5+0$','25 : une seule écriture','resultat')
panel(28,20,r'$0\leq r\leq 5$','limite',True,'limite','limite',r'$5\times4+5$',r'$5\times5+0$','25 : deux écritures','limite')
line(ax,[(X(25),52),(X(25),60)],'fixe',dash=True); line(ax,[(X(25),20),(X(25),28)],'fixe',dash=True); line(ax,[(X(25),8),(X(25),11.5)],'fixe',dash=True)
numberline(ax,X(20),X(30),8,20,30,step=5,labels=True,arrow_right=False,size='s')
save(fig,'05-041')
