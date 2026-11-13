import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,53,65,r'pour $a=23$ et $b=5$','encre','m')
hs=[r'1. $b\neq 0$',r'2. $a=b\times q+r$',r'3. $0\leq r<b$']
xs=[22,43,64]
for x,h in zip(xs,hs): box(ax,x,46,20,10,'fixe',label=h,size='s')
def mark(cx,cy,ok):
    if ok: line(ax,[(cx-2,cy),(cx-0.5,cy-1.8),(cx+2.5,cy+2.2)],'resultat',lw=1.5)
    else:
        line(ax,[(cx-2,cy-2),(cx+2,cy+2)],'limite',lw=1.5); line(ax,[(cx-2,cy+2),(cx+2,cy-2)],'limite',lw=1.5)
for y,lab,oks in ((30,r'$q=4,\ r=3$',(1,1,1)),(16,r'$q=3,\ r=8$',(1,1,0))):
    text(ax,11,y+5,lab,'encre','s')
    for x,ok in zip(xs,oks):
        box(ax,x,y,20,10,'resultat' if ok else 'limite'); mark(x+10,y+5,ok)
text(ax,74,11,'8 ≥ 5 : échoue','limite','s')
save(fig,'05-032')
