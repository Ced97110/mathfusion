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
fig,ax=canvas(80)
y1=58; y2=18
term(ax,4,y1); lead(ax,4,8,y1); par(ax,8,34,y1,[[I(A),I(B)],[I(A),I(Bp)],[I(A),I(A)]],dy=9,w=5.5); lead(ax,34,38,y1); term(ax,38,y1)
term(ax,4,y2); chain(ax,4,38,y2,[I(A,None,'autre')],w=8); term(ax,38,y2)
text(ax,70,70,'positions $(a, b)$','encre','s')
for l,x,yy,ro in [('(0,0)',62,60,'fixe'),('(0,1)',78,60,'fixe'),('(1,0)',62,46,'resultat'),('(1,1)',78,46,'resultat')]: box(ax,x-7,yy-4,14,8,ro,label=l,size='s')
box(ax,53,40,34,12,'resultat',fill=False,dash=True)
text(ax,70,33,'$a$ fermé : il passe','resultat','s')
arrow(ax,(42,y1),(52,48),'varie'); arrow(ax,(42,y2),(52,44),'varie')
save(fig,'80-191')
