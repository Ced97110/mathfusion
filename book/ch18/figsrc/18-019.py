import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cells(ox,oy,u): return {"xx":(ox,oy,4*u,4*u),"a":(ox+4*u,oy,2*u,4*u),"b":(ox,oy+4*u,4*u,3*u),"c":(ox+4*u,oy+4*u,2*u,3*u)}
def draw(ax,C,roles):
    for k,(x,y,w,h) in C.items(): poly(ax,[(x,y),(x+w,y),(x+w,y+h),(x,y+h)],roles[k])
def mid(C,k): x,y,w,h=C[k]; return (x+w/2,y+h/2)
fig,ax=canvas(58)
u=5.4; ox,oy=10,14; C=cells(ox,oy,u)
draw(ax,C,dict(xx='fixe',a='varie',b='varie',c='sujet'))
text(ax,*mid(C,'xx'),r'$x^2$','encre','m')
text(ax,*mid(C,'a'),r'$2x$','encre','m')
text(ax,*mid(C,'b'),r'$3x$','encre','m')
text(ax,*mid(C,'c'),r'$2\times3$'+'\n= 6','encre','s')
text(ax,ox+2*u,10,'x','fixe','m'); text(ax,ox+5*u,10,'2','varie','m')
text(ax,ox-3.5,oy+2*u,'x','fixe','m'); text(ax,ox-3.5,oy+5.5*u,'3','varie','m')
t=mid(C,'c'); arrow(ax,(47,t[1]),(ox+6*u+1,t[1]),'sujet')
text(ax,48,t[1],'produit : 6 = 2 × 3','sujet','s',ha='left')
t=mid(C,'a'); arrow(ax,(47,t[1]),(ox+6*u+1,t[1]),'varie')
text(ax,48,t[1],'somme : 5 = 2 + 3','varie','s',ha='left')
save(fig,'18-019')
