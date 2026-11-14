import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
ox,oy,s=46,30,8
line(ax,[(4,oy),(84,oy)],'fixe',lw=0.6); line(ax,[(ox,14),(ox,50)],'fixe',lw=0.6)
arrow(ax,(ox,oy),(ox-3*s+1.5,oy),'sujet',lw=1.6)
disc(ax,ox-3*s,oy,1.5,'sujet')
text(ax,ox-3*s,oy+5,'A = H','sujet','s')
text(ax,ox+3,oy-4,'O','encre','s')
brace(ax,ox-3*s,ox,oy-3,'sujet',label=r'$R=|a|=3$')
arc=[(ox+9*math.cos(math.radians(t)),oy+9*math.sin(math.radians(t))) for t in range(0,181,4)]
line(ax,arc,'varie',lw=1.1)
text(ax,ox,oy+14,r'$\alpha=180°$','varie','s')
disc(ax,ox+3*s,oy,1.5,'fixe',fill=False)
text(ax,ox+3*s,oy+5,'$a=3$ : $\\alpha=0°$','fixe','s')
text(ax,44,54,'$b=0$ : le triangle est plat','encre','m')
save(fig,'35-088')
