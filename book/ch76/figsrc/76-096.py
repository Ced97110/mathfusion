import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
s=7
poly(ax,[(6,10),(6+s,10),(6+s,10+s),(6,10+s)],'fixe')
arrow(ax,(6,10),(6+s,10),'sujet',lw=1.3); arrow(ax,(6,10),(6,10+s),'autre',lw=1.3)
text(ax,9.5,5,'aire 1','fixe','s')
arrow(ax,(16,14),(29,14),'varie'); text(ax,22.5,18,r'$A$','varie','l')
ox,oy=33,10
poly(ax,[(ox,oy),(ox+2*s,oy+s),(ox+3*s,oy+4*s),(ox+s,oy+3*s)],'resultat')
arrow(ax,(ox,oy),(ox+2*s,oy+s),'sujet',lw=1.3); arrow(ax,(ox,oy),(ox+s,oy+3*s),'autre',lw=1.3)
text(ax,ox+1.5*s+1,oy+2*s,'aire 5','resultat','m')
text(ax,70,50,r'$A=$','encre','l'); text(ax,79,53,'2   1','encre','l'); text(ax,79,47,'1   3','encre','l')
text(ax,72,30,r'$\det A=5$','resultat','xl')
save(fig,'76-096')
