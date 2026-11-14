import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,53,'groupe commutatif : g + h = h + g','encre','s')
vals=[2,5,8,11]; xs=[22+i*17 for i in range(4)]
text(ax,8,38,r'$gH$','autre','m'); text(ax,8,14,r'$Hg$','sujet','m')
for x,v in zip(xs,vals):
    box(ax,x-6,33,12,10,'autre',label=str(v)); box(ax,x-6,9,12,10,'sujet',label=str(v))
    line(ax,[(x-1,28),(x+1,28)],'resultat',lw=1.2); line(ax,[(x-1,24),(x+1,24)],'resultat',lw=1.2)
text(ax,86,26,'','fixe')
save(fig,'47-042')
