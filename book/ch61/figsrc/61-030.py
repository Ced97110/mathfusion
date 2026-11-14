import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
ox,oy=14,12; sx,sy=11,6.5
arrow(ax,(ox,oy),(ox+5.6*sx,oy),'fixe',lw=0.9); arrow(ax,(ox,oy),(ox,oy+8.8*sy),'fixe',lw=0.9)
text(ax,ox+3*sx,3,r'coefficient de $1$','fixe','s'); text(ax,4,oy+4*sy,r'coefficient de $\sqrt{2}$','fixe','s',rot=90)
for a,b,role,lab,dx in ((4,7,'sujet',r'$4+7\sqrt{2}$',-2),(0.5,1,'varie',r'$\frac{1}{2}+\sqrt{2}$',0)):
    px,py=ox+a*sx,oy+b*sy
    line(ax,[(px,oy),(px,py),(ox,py)],role,dash=True,lw=0.7)
    disc(ax,px,py,1.2,role)
    text(ax,px+4,py+(4 if role=='sujet' else -5)+dx*0,lab,role,'s',ha='left' if role=='varie' else 'center')
text(ax,ox+4*sx,oy-2.5,'4','sujet','s'); text(ax,ox-2.5,oy+7*sy,'7','sujet','s')
text(ax,62,32,'deux coefficients :','encre','s'); text(ax,62,27.5,'degré 2','sujet','s')
save(fig,'61-030')
