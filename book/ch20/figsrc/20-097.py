import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
f = numberline(ax, 12, 72, 58, -4, 2, step=1, every=2, arrow_right=False)
disc(ax, f(-3), 58, 1.6, 'limite'); disc(ax, f(0), 58, 1.6, 'limite')
text(ax, f(-3), 64, r'$c=-3$', 'limite'); text(ax, f(0), 64, r'$c=0$', 'limite')
box(ax, f(-3) - 18, 34, 36, 12, 'limite', label=r'$0<-3$ : faux')
box(ax, f(0) - 18, 34, 36, 12, 'limite', label=r'$0<0$ : faux')
box(ax, 14, 4, 60, 22, 'limite', fill=False, dash=True, label="aucun point n'est solution")
save(fig, '20-097')
