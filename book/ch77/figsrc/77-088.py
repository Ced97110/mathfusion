import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
f = numberline(ax, 10, 70, 22, -3, 3, step=1)
line(ax, [(f(0), 22), (f(3), 22)], 'autre', lw=2.6)
for v in (0,):
    disc(ax, f(v), 22, 1.1, 'autre')
text(ax, f(1.5), 11, r'$\mathbb{C}$ : $a^2+b^2\geq0$', 'autre', 'm')
text(ax, f(1.5), 6, 'jamais négative', 'autre', 's')
disc(ax, f(-1), 22, 1.6, 'sujet')
arrow(ax, (f(-1), 33), (f(-1), 24.5), 'sujet')
text(ax, 34, 36.5, r'$N(1+\sqrt{2})=1-2=-1$', 'sujet', 's')
text(ax, 34, 41.5, r'sur $\mathbb{Q}(\sqrt{2})$ : négative possible', 'sujet', 's')
save(fig, '77-088')
