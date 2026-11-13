import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(76)
text(ax,44,70,'recouper 1/2 en sixièmes','encre','m')
row(ax,20,50,24,9,['sujet',None]); text(ax,10,54.5,'1/2','sujet','m')
row(ax,20,24,8,9,['sujet']*3+[None]*3); text(ax,10,28.5,'3/6','sujet','m')
line(ax,[(44,50),(44,33)],'fixe',dash=True)
brace(ax,20,44,24,'sujet','6 ÷ 2 = 3 sixièmes')
text(ax,44,10,'haut : 1 × 3 = 3','varie','m')
save(fig,'07-029')
