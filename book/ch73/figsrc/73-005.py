import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
ox,oy,u=28,10,26
arrow(ax,(ox-4,oy),(ox+u+8,oy),'fixe',lw=0.7); arrow(ax,(ox,oy-1),(ox,oy+u+8),'fixe',lw=0.7)
a=[math.radians(t) for t in range(0,91,3)]
line(ax,[(ox+u*math.cos(t),oy+u*math.sin(t)) for t in a],'resultat',dash=True)
arrow(ax,(ox+u,oy+1.5),(ox+u,oy+u-1.8),'limite',lw=1.2)
arrow(ax,(ox+u-2,oy+u),(ox+2,oy+u),'resultat',lw=1.0)
disc(ax,ox+u,oy,1.2,'sujet'); disc(ax,ox+u,oy+u,1.2,'limite'); disc(ax,ox,oy+u,1.2,'resultat')
text(ax,ox+u,oy-4,'(1, 0)','sujet','s')
text(ax,ox+u+3,oy+u,'(1, 1)','limite','s',ha='left')
text(ax,ox-3,oy+u,'(0, 1)','resultat','s',ha='right')
text(ax,ox+u+3,oy+u/2,'2 glissements','limite','s',ha='left')
text(ax,ox+u/2+2,oy+u+4.2,'3e glissement','resultat','s')
text(ax,ox+u/2-2,oy+8,'quart de tour','resultat','s')
save(fig,'73-005')
