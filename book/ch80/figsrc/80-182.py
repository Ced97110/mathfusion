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
fig,ax=canvas(70)
y=44
text(ax,24,64,r'$a$ en parallèle avec $O$','encre','s'); text(ax,70,64,'a seul','encre','s')
term(ax,4,y); lead(ax,4,12,y); par(ax,12,36,y,[[I(A)],[I(r'$O$',None,'brk')]],dy=14,w=8); lead(ax,36,44,y); term(ax,44,y)
text(ax,51,y,'=','varie','xl')
term(ax,58,y); chain(ax,58,82,y,[I(A,None,'autre')],w=8); term(ax,82,y)
text(ax,44,16,'a fermé : le courant passe','resultat','s')
save(fig,'80-182')
