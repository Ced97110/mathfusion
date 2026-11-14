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
fig,ax=canvas(75)
y=38
disc(ax,34.5,y,17,'sujet',fill=False,lw=1.1); disc(ax,53.5,y,17,'autre',fill=False,lw=1.1)
text(ax,24,60,'premier circuit','sujet','s'); text(ax,64,60,'second circuit','autre','s')
box(ax,19.5,y-3,11,6,'sujet',label='(1,0)',size='s'); box(ax,38.5,y-3,11,6,'resultat',label='(1,1)',size='s'); box(ax,57.5,y-3,11,6,'autre',label='(0,1)',size='s')
text(ax,22,28,'seul le premier passe','limite','s')
text(ax,44,8,r'série : on garde $\cap$','resultat','s')
save(fig,'80-192')
