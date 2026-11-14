import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
def seq(fig,ax,x,y,parts,size="l"):
    out=[]
    for s,r in parts:
        t=text(ax,x,y,s,r,size,ha="left"); fig.canvas.draw()
        bb=t.get_window_extent(fig.canvas.get_renderer()); wmm=bb.width/fig.dpi*25.4
        out.append((x,x+wmm)); x+=wmm
    return out
text(ax,44,50,'le trait couvre le bloc qui revient','encre','s')
rows=[(38,[('0,','encre'),('3','sujet')],'0,333…','encre'),
      (24,[('3,','encre'),('703','sujet')],'3,703703…','encre'),
      (10,[('3,70','encre'),('3','varie')],'3,7033333…','limite')]
for y,parts,ex,r in rows:
    sp=seq(fig,ax,6,y,parts)
    x0,x1=sp[1]; line(ax,[(x0+0.3,y+4.2),(x1-0.3,y+4.2)],parts[1][1],lw=1.1)
    text(ax,42,y,'=' if r=='encre' else r'$\neq$',r,'l')
    text(ax,48,y,ex,r,'l',ha='left')
save(fig,'08-075')
