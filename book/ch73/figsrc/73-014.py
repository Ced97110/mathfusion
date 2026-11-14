import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
u=14; ox,oy=12,12
arrow(ax,(ox,oy),(ox+4*u+4,oy),'fixe',lw=0.7); arrow(ax,(ox,oy),(ox,oy+3*u+4),'fixe',lw=0.7)
for k in range(1,5):
    line(ax,[(ox+k*u,oy-1),(ox+k*u,oy+1)],'fixe'); text(ax,ox+k*u,oy-4,str(k),'fixe','s')
for k in range(1,4):
    line(ax,[(ox-1,oy+k*u),(ox+1,oy+k*u)],'fixe'); text(ax,ox-4,oy+k*u,str(k),'fixe','s')
line(ax,[(ox+u,oy),(ox+u,oy+2*u)],'fixe',dash=True)
text(ax,ox+u+2,oy+u,'hauteur 2','fixe','s',ha='left')
arrow(ax,(ox+u+1.5,oy+2*u),(ox+2*u-1.5,oy+2*u),'varie',lw=1.3)
disc(ax,ox+u,oy+2*u,1.3,'varie'); disc(ax,ox+2*u,oy+2*u,1.3,'resultat')
text(ax,ox+u-3,oy+2*u+3.5,r'$P$','varie','s'); text(ax,ox+2*u+3.5,oy+2*u+3.5,r"$P'$",'resultat','s')
text(ax,ox+1.5*u,oy+2*u-3.8,'1/2 × 2 = 1','varie','s')
text(ax,66,56,r'$b$ = 1/2','sujet','m')
save(fig,'73-014')
