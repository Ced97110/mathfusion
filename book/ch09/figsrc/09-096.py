import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
def eq(x,y):
    for d in (-0.9,0.9): line(ax,[(x-1.6,y+d),(x+1.6,y+d)],'encre',lw=1.1)
def tm(x,y):
    line(ax,[(x-1.5,y-1.5),(x+1.5,y+1.5)],'encre',lw=1.1); line(ax,[(x-1.5,y+1.5),(x+1.5,y-1.5)],'encre',lw=1.1)
rows=[(44,[None,'0,30','50'],'multiplier'),(26,['15',None,'50'],'15 ÷ 50'),(8,['15','0,30',None],'15 ÷ 0,30')]
for y,v,lab in rows:
    for x,val,r in zip([4,28,52],v,['resultat','sujet','sujet']):
        if val is None: box(ax,x,y,14,12,'varie',label='?',dash=True)
        else: box(ax,x,y,14,12,r,label=val)
    eq(23,y+6); tm(47,y+6); text(ax,70,y+6,lab,'varie','s',ha='left')
save(fig,'09-096')
