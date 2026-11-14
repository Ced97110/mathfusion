import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
yl = 24
f = numberline(ax, 8, 72, yl, -4, 4, 1, labels=False, arrow_right=True)
line(ax, [(f(-4), yl), (f(-0.6), yl)], 'sujet', lw=2.2); line(ax, [(f(0.6), yl), (f(4), yl)], 'sujet', lw=2.2)
for v in (-4, -3, -2, -1, 1, 2, 3, 4): text(ax, f(v), yl - 3.4, str(v).replace('-', '−'), 'sujet', 's')
disc(ax, f(0), yl, 2.2, 'limite', fill=False, lw=1.2); text(ax, f(0), yl - 3.4, '0', 'limite', 's')
disc(ax, f(2), yl, 1.6, 'sujet')
arrow(ax, (f(2) - 1, yl + 2.5), (f(0) + 1, yl + 2.5), 'varie', curve=0.35)
text(ax, f(1), yl + 10, '2 − 2', 'varie', 'm')
text(ax, f(2), yl + 18, 'g = 2 est dans ℝ*', 'sujet', 's')
text(ax, f(0), 6, '0 n’est pas dans ℝ*', 'limite', 'm', weight='bold')
save(fig, '46-055')
