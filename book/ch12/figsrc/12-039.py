import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
def sign(y,wide_left):
    x0,x1=34,54
    pts=[(x0,y+5),(x1,y),(x0,y-5)] if wide_left else [(x1,y+5),(x0,y),(x1,y-5)]
    line(ax,pts,'fixe',lw=1.4)
    xw=x0 if wide_left else x1
    line(ax,[(xw,y+5),(xw,y-5)],'varie',lw=1.6,dash=True)
for y,l,r,wl in [(40,'8','5',True),(16,'5','8',False)]:
    text(ax,16,y,l,'sujet' if l=='8' else 'fixe','xl')
    text(ax,72,y,r,'sujet' if r=='8' else 'fixe','xl')
    sign(y,wl); text(ax,44,y-9,'côté large','varie','s')
save(fig,'12-039')
