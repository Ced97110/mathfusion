import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cells(ox,oy,u): return {"xx":(ox,oy,4*u,4*u),"a":(ox+4*u,oy,2*u,4*u),"b":(ox,oy+4*u,4*u,3*u),"c":(ox+4*u,oy+4*u,2*u,3*u)}
def draw(ax,C,roles):
    for k,(x,y,w,h) in C.items(): poly(ax,[(x,y),(x+w,y),(x+w,y+h),(x,y+h)],roles[k])
def mid(C,k): x,y,w,h=C[k]; return (x+w/2,y+h/2)
fig,ax=canvas(52)
u=5.4; C=cells(4,6,u)
draw(ax,C,dict(xx='sujet',a='varie',b='varie',c='fixe'))
for k,s in dict(xx=r'$x^2$'+'\n16',a=r'$2x$'+'\n8',b=r'$3x$'+'\n12',c='6').items():
    p=mid(C,k); text(ax,p[0],p[1],s,'encre','m')
text(ax,65,47,'quatre termes','fixe','s')
text(ax,65,41,r'$x^2+2x+3x+6$','encre','m')
text(ax,65,35,'16 + 8 + 12 + 6 = 42','resultat','s')
text(ax,65,28,'=','encre','l')
text(ax,65,21,'trois termes','fixe','s')
text(ax,65,15,r'$x^2+5x+6$','sujet','m')
text(ax,65,9,'16 + 5 × 4 + 6 = 42','resultat','s')
save(fig,'18-017')
