import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cells(ox,oy,u): return {"xx":(ox,oy,4*u,4*u),"a":(ox+4*u,oy,2*u,4*u),"b":(ox,oy+4*u,4*u,3*u),"c":(ox+4*u,oy+4*u,2*u,3*u)}
def draw(ax,C,roles):
    for k,(x,y,w,h) in C.items(): poly(ax,[(x,y),(x+w,y),(x+w,y+h),(x,y+h)],roles[k])
def mid(C,k): x,y,w,h=C[k]; return (x+w/2,y+h/2)
fig,ax=canvas(66)
u=3.6; ox,oy=10,6; C=cells(ox,oy,u)
box(ax,4,52,62,10,'fixe',label='recette : produit 6, somme 5',size='s')
arrow(ax,(21,52),(21,oy+7*u+1.5),'varie')
text(ax,24,42,'on redessine le rectangle','varie','s',ha='left')
draw(ax,C,dict(xx='fixe',a='varie',b='varie',c='sujet'))
text(ax,*mid(C,'xx'),r'$x^2$','encre','m')
text(ax,*mid(C,'a'),r'$2x$','encre','s')
text(ax,*mid(C,'b'),r'$3x$','encre','m')
text(ax,*mid(C,'c'),'6','encre','m')
t=mid(C,'c'); arrow(ax,(39.5,t[1]),(ox+6*u+0.8,t[1]),'sujet'); text(ax,41,t[1],'coin : aire 2 × 3 = 6','sujet','s',ha='left')
t=mid(C,'a'); arrow(ax,(39.5,t[1]),(ox+6*u+0.8,t[1]),'varie'); text(ax,41,t[1],'milieu : 2x + 3x = 5x','varie','s',ha='left')
text(ax,41,5,'le dessin donne la raison','resultat','s',ha='left')
save(fig,'18-021')
