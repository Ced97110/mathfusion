import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
def sign(y,wide_left):
    x0,x1=34,54
    pts=[(x0,y+5),(x1,y),(x0,y-5)] if wide_left else [(x1,y+5),(x0,y),(x1,y-5)]
    line(ax,pts,'varie',lw=1.6)
for y,l,r,wl in [(46,'5','8',False),(10,'8','5',True)]:
    text(ax,16,y,l,'autre' if l=='5' else 'sujet','xl')
    text(ax,72,y,r,'autre' if r=='5' else 'sujet','xl')
    sign(y,wl)
text(ax,44,28,'même chose','resultat','m')
arrow(ax,(44,38),(44,32),'resultat'); arrow(ax,(44,18),(44,24),'resultat')
save(fig,'12-040')
