import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

A=r'$a$'; B=r'$b$'; C=r'$c$'; Ap=r"$a'$"; Bp=r"$b'$"
def I(lab,st=None,ro='sujet'): return (lab,st,ro)
def sw(ax,cx,cy,lab,st=None,ro='sujet',w=7,h=5.5):
    if st is False: box(ax,cx-w/2,cy-h/2,w,h,'fixe',fill=False,label=lab,size='s',dash=True)
    elif st is True: box(ax,cx-w/2,cy-h/2,w,h,'resultat',label=lab,size='s')
    else: box(ax,cx-w/2,cy-h/2,w,h,ro,label=lab,size='s')
def lead(ax,x0,x1,y,ro='fixe'): line(ax,[(x0,y),(x1,y)],ro)
def term(ax,x,y): disc(ax,x,y,0.9,'fixe')
def chain(ax,xl,xr,y,items,w=7):
    n=len(items); x=xl
    if n==0:
        lead(ax,xl,xr,y); return
    sp=(xr-xl-n*w)/(n+1); pos=xl
    for lab,st,ro in items:
        bx=pos+sp; cx=bx+w/2
        if ro=='brk':
            lead(ax,x,cx-2.5,y); text(ax,cx,y+2.8,lab,'limite','s'); x=cx+2.5
        else:
            lead(ax,x,bx,y); sw(ax,cx,y,lab,st,ro,w); x=bx+w
        pos=bx+w
    lead(ax,x,xr,y)
def par(ax,xl,xr,y,branches,dy=11,w=7):
    n=len(branches); ys=[y+dy*((n-1)/2-k) for k in range(n)]
    line(ax,[(xl,ys[0]),(xl,ys[-1])]); line(ax,[(xr,ys[0]),(xr,ys[-1])])
    for yy,b in zip(ys,branches): chain(ax,xl,xr,yy,b,w)
def cross(ax,x,y,r=2.2): line(ax,[(x-r,y-r),(x+r,y+r)],'limite',1.2); line(ax,[(x-r,y+r),(x+r,y-r)],'limite',1.2)
def six(ax,xl,xr,y,w=6):
    par(ax,xl,xr,y,[[I(A),I(A)],[I(A),I(A)],[I(A),I(A)]],dy=8,w=w)
fig,ax=canvas(92)
oy=12
text(ax,44,70+oy,'ensemble des circuits série-parallèle','sujet','s')
box(ax,2,6+oy,84,58,'sujet',fill=False,dash=True)
y=42+oy
lead(ax,5,6,y); chain(ax,6,30,y,[I(A,None,'resultat'),I(B,None,'resultat')],w=6)
lead(ax,33,37,y); par(ax,37,54,y,[[I(A,None,'resultat')],[I(B,None,'resultat')]],dy=9,w=6); lead(ax,54,58,y)
lead(ax,62,66,y); sw(ax,70,y,Ap,None,'resultat',w=8); lead(ax,74,82,y)
text(ax,18,24+oy,'série','encre','s'); text(ax,46,24+oy,'parallèle','encre','s'); text(ax,72,24+oy,'couplé','encre','s')
text(ax,18,14+oy,r'$a\wedge b$','resultat','m'); text(ax,46,14+oy,r'$a\vee b$','resultat','m'); text(ax,72,14+oy,Ap,'resultat','m')
text(ax,44,8,'les cinq axiomes de Judson tiennent','encre','s')
text(ax,44,1.5,'donc : algèbre de Boole','resultat','m',weight='bold')
save(fig,'80-180')
