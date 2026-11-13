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
fig,ax=canvas(84)
def circ(y,cap):
    text(ax,44,y+10,cap,'encre','s'); term(ax,8,y); term(ax,80,y)
circ(66,'deux interrupteurs en série'); chain(ax,8,80,66,[I(A),I(B,None,'varie')],w=9)
circ(40,'b devient deux en parallèle'); chain(ax,8,40,40,[I(A)],w=9); par(ax,40,64,40,[[I(B,None,'resultat')],[I(C,None,'varie')]],dy=8,w=8); lead(ax,64,80,40)
circ(14,'c devient deux en série'); chain(ax,8,36,14,[I(A)],w=9); par(ax,36,72,14,[[I(B,None,'resultat')],[I(C,None,'resultat'),I(r'$d$',None,'resultat')]],dy=8,w=7); lead(ax,72,80,14)
arrow(ax,(44,62),(44,55)); arrow(ax,(44,34),(44,29))
save(fig,'80-169')
