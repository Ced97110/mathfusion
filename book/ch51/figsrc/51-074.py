import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
ox,oy,u=12,12,12
arrow(ax,(ox,oy),(ox+3.6*u,oy),'fixe',lw=0.8); arrow(ax,(ox,oy),(ox,oy+3.6*u),'fixe',lw=0.8)
for m in range(4):
    for n in range(4):
        disc(ax,ox+m*u,oy+n*u,1.0,'fixe')
for v in (1,2,3):
    text(ax,ox+v*u,oy-3.5,str(v),'fixe','s'); text(ax,ox-3.5,oy+v*u,str(v),'fixe','s')
px,py=ox+0.5*u,oy+u/3
line(ax,[(px,oy),(px,py)],'varie',dash=True); line(ax,[(ox,py),(px,py)],'varie',dash=True)
disc(ax,px,py,1.7,'varie')
text(ax,px+3,py+3,r'$\frac{1}{2}+\frac{1}{3}\sqrt{2}$','varie','m',ha='left')
text(ax,ox+46,oy-3.5,r'$a$','fixe','s'); text(ax,ox+3,oy+3.7*u+2,r'$b\sqrt{2}$','fixe','s',ha='left')
text(ax,ox+44,oy+30,'gris : ℤ[√2]','fixe','s',ha='left')
text(ax,ox+44,oy+23,'orange : ℚ(√2)','varie','s',ha='left')
text(ax,ox+44,oy+16,'entre les nœuds','varie','s',ha='left')
save(fig,'51-074')
