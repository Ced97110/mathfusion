import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def seq(fig,ax,x,y,parts,size="l"):
    out=[]
    for s,r in parts:
        t=text(ax,x,y,s,r,size,ha="left"); fig.canvas.draw()
        bb=t.get_window_extent(fig.canvas.get_renderer()); wmm=bb.width/fig.dpi*25.4
        out.append((x,x+wmm)); x+=wmm
    return out
rows=[(54,[('0,','encre'),('3','sujet'),('…','fixe')],'période 3'),
      (34,[('3,','encre'),('703','sujet'),('703…','fixe')],'période 703'),
      (14,[('0,','encre'),('142857','sujet'),('142857…','fixe')],'période 142857')]
for y,parts,lab in rows:
    sp=seq(fig,ax,6,y,parts)
    x0,x1=sp[1]; brace(ax,x0,x1,y-4.5,'sujet',label=lab,down=True)
save(fig,'08-074')
