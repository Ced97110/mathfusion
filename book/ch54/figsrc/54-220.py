import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# left: monic x - 3, root 3 on the integer ticks
box(ax, 2, 54, 40, 11, 'sujet', label=r'$x-3$', size='l')
text(ax, 22, 49, 'coefficient dominant 1', 'sujet', 's')
f = numberline(ax, 5, 37, 34, 0, 4, step=1, arrow_right=False, size='s', tick=1.4)
disc(ax, f(3), 34, 1.6, 'resultat')
text(ax, 22, 20, 'racine 3 : entière,\n3 divise −3', 'resultat', 's')
# right: 2x - 1, root 1/2 falls between the integer ticks 0 and 1
box(ax, 46, 54, 40, 11, 'autre', label=r'$2x-1$', size='l')
text(ax, 66, 49, 'coefficient dominant 2', 'autre', 's')
g = numberline(ax, 50, 82, 34, 0, 1, step=1, arrow_right=False, size='s', tick=1.4)
disc(ax, g(0.5), 34, 1.6, 'limite')
text(ax, 66, 20, 'racine 1/2 :\npas entière', 'limite', 's')
save(fig, '54-220')
