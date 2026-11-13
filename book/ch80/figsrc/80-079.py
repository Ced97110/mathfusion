import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(64)
ox,oy=8,10
line(ax,[(ox-3,oy-2.4),(ox+60,oy+48)],'fixe',lw=0.9,dash=True)
arrow(ax,(ox,oy),(ox+32,oy+25.6),'varie',lw=1.6)
arrow(ax,(ox,oy),(ox+16,oy+12.8),'sujet',lw=2.6)
disc(ax,ox,oy,1.2,'encre')
text(ax,ox+9,oy+19,'(1, 1, 1)','sujet','m')
text(ax,ox+36,oy+35,'(2, 2, 2)','varie','m')
text(ax,ox+44,oy+13,'même droite','fixe','s')
text(ax,ox+22,oy-4.5,'origine','encre','s')
text(ax,44,59,'même droite : un seul point','resultat','m')
save(fig,'80-079')
