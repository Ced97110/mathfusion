import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
ox,oy=14,12
arrow(ax,(ox,oy),(ox+68,oy),'fixe',lw=0.9); arrow(ax,(ox,oy),(ox,oy+52),'varie',lw=0.9)
text(ax,ox+60,oy-4.5,r'$a$  (réel)','fixe','s')
text(ax,ox+1,oy+56,r'$b\sqrt{-1}$','varie','s',ha='left')
px,py=ox+40,oy+32
line(ax,[(px,oy),(px,py)],'varie',dash=True); line(ax,[(ox,oy+0),(px,oy)],'sujet',lw=1.6)
line(ax,[(ox,py),(px,py)],'varie',dash=True)
disc(ax,px,py,1.6,'sujet')
text(ax,px+3,py+4,r'$a+b\sqrt{-1}$','sujet','m',ha='left')
text(ax,px+1.5,oy+14,r'$b$ fois $\sqrt{-1}$','varie','s',ha='left')
text(ax,ox+4,oy+44,r'$(\sqrt{-1})^2=-1$','varie','m',ha='left')
save(fig,'51-067')
