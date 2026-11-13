import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
u=6; x0=14
box(ax,x0,40,0.995*u,7,'sujet')
box(ax,x0,24,10*u,7,'varie',label=r'$\tan A=10$')
text(ax,x0+0.995*u+2,43.5,r'$\sin A\approx0{,}995$','sujet','s',ha='left')
numberline(ax,x0,x0+10*u,13,0,10,step=1,every=5,arrow_right=False)
line(ax,[(x0+u,11),(x0+u,50)],'fixe',dash=True)
text(ax,x0+u,53,'1','fixe','s')
text(ax,56,53,r'$a\div b=10\div1$','encre','s')
save(fig,'26-034')
