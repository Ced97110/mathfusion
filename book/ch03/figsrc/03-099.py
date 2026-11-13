import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
f=lambda v: 6+v*72/99
numberline(ax,6,78,34,0,99,step=9,labels=False)
for k in range(11): arrow(ax,(f(9*k),35.5),(f(9*k+9),35.5),'varie',curve=-0.5,lw=0.8)
text(ax,24,52,'bonds de 9 depuis 0','varie','s')
for v,t in ((9,'9 × 1'),(63,'9 × 7'),(99,'9 × 11')):
    disc(ax,f(v),34,1.2,'resultat'); text(ax,f(v),42,t,'resultat','s')
for v in (0,9,63,99): text(ax,f(v),29.6,str(v),'fixe','s')
text(ax,70,52,'693 = 9 × 77','resultat','s')
box(ax,4,8,32,10,'autre',label='9 divise 63',size='m')
box(ax,52,8,34,10,'sujet',label='63 est multiple de 9',size='s')
arrow(ax,(37,13),(51,13),'varie',both=True)
text(ax,44,22,'même fait','varie','s')
save(fig,'03-099')
