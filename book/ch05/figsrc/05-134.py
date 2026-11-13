import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(48)
text(ax,22,43,'mêmes premiers, autre ordre','encre','s')
top=[2,2,3,5]; bot=[5,3,2,2]; xs=[8,17,26,35]; yt,yb=31,11; r=3.4
pairs=[(0,2),(1,3),(2,1),(3,0)]
for i,j in pairs: line(ax,[(xs[i],yt-r),(xs[j],yb+r)],'fixe',lw=0.6)
for x,v in zip(xs,top): disc(ax,x,yt,r,'sujet',label=str(v))
for x,v in zip(xs,bot): disc(ax,x,yb,r,'autre',label=str(v))
box(ax,62,5,20,32,'resultat',label='60',size='xl')
arrow(ax,(40,yt),(61.5,yt),'varie',both=True); arrow(ax,(40,yb),(61.5,yb),'varie',both=True)
text(ax,51,21,'se déterminent','varie','s')
save(fig,'05-134')
