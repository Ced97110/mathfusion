import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
for x0,mx in ((6,9),(62,79)):
    poly(ax,[(x0,20),(x0+20,20),(x0+20,40),(x0,40)],'fixe')
    disc(ax,mx,23,2,'sujet')
arrow(ax,(28,34),(60,34),'varie',curve=-0.4)
text(ax,44,47,'x : quart de tour','varie','s')
arrow(ax,(60,26),(28,26),'sujet',curve=-0.4)
text(ax,44,14,r'$x^{-1}$ : le défait','sujet','s')
text(ax,16,15,'départ','fixe','s'); text(ax,72,15,'après x','fixe','s')
save(fig,'49-049')
