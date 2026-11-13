import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cells(ox,oy,u): return {"xx":(ox,oy,4*u,4*u),"a":(ox+4*u,oy,2*u,4*u),"b":(ox,oy+4*u,4*u,3*u),"c":(ox+4*u,oy+4*u,2*u,3*u)}
def draw(ax,C,roles):
    for k,(x,y,w,h) in C.items(): poly(ax,[(x,y),(x+w,y),(x+w,y+h),(x,y+h)],roles[k])
def mid(C,k): x,y,w,h=C[k]; return (x+w/2,y+h/2)
fig,ax=canvas(58)
u=5.4; C=cells(12,12,u)
draw(ax,C,dict(xx='fixe',a='fixe',b='fixe',c='fixe'))
for k,s in dict(xx=r'$x^2$',a=r'$2x$',b=r'$3x$',c='6').items():
    p=mid(C,k); text(ax,p[0],p[1],s,'encre','m')
arrow(ax,(12,8.5),(12+6*u,8.5),'sujet',both=True); text(ax,12+3*u,4.5,r'$x+2$','sujet','m')
arrow(ax,(8,12),(8,12+7*u),'sujet',both=True); text(ax,3.5,12+3.5*u,r'$x+3$','sujet','m',rot=90)
text(ax,66,50,'par les régions','fixe','s')
text(ax,66,44,r'$x^2+5x+6$','sujet','m')
text(ax,66,35,'=','encre','l')
text(ax,66,26,'par les côtés','fixe','s')
text(ax,66,20,r'$(x+2)(x+3)$','sujet','m')
text(ax,66,10,'x = 4 : 6 × 7 = 42','resultat','s')
save(fig,'18-018')
