import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
bw,bh=14,6.4
C0=(44,30); O=[((44,52),r'$(1,1)$',(9,1)),((25,19),r'$(0,1)$',(-8,3.5)),((63,19),r'$(1,0)$',(8,3.5))]
def edge(a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]
    t=min(bw/2/abs(dx) if dx else 9, bh/2/abs(dy) if dy else 9)+0.05
    return (a[0]+dx*t,a[1]+dy*t)
box(ax,C0[0]-bw/2,C0[1]-bh/2,bw,bh,'fixe',label=r'$(0,0)$',size='s')
for c,l,off in O:
    box(ax,c[0]-bw/2,c[1]-bh/2,bw,bh,'sujet',label=l,size='s')
    arrow(ax,edge(C0,c),edge(c,C0),'varie',both=True)
    m=((C0[0]+c[0])/2+off[0],(C0[1]+c[1])/2+off[1])
    text(ax,m[0],m[1],'2 appuis','varie','s')
text(ax,44,5,'aucun ne fait les 4 cases','limite','m')
save(fig,'45-189')
