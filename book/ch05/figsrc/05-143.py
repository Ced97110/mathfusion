import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(56)
s=0.32; x0=4
text(ax,44,52,'case = carré de côté d','encre','m')
def bar(y,n,d,role,lab):
    for k in range(n): rect(ax,x0+k*d*s,y,d*s,d*s,role)
    text(ax,x0,y+d*s+3.2,lab,role,'s',ha='left')
bar(36,14,18,'resultat','d = 18 : 252 = 14 × 18')
bar(22,11,18,'resultat','d = 18 : 198 = 11 × 18')
bar(8,12,20,'varie','d = 20 : 252 = 12 × 20 + 12')
rect(ax,x0+12*20*s,8,12*s,20*s*1.0 if False else 12*s,'limite')
text(ax,80,4,'reste 12','limite','s')
save(fig,'05-143')
