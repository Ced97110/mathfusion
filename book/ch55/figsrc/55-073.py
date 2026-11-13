import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cs = [24, 42, 60, 78]
for c, sg in zip(cs, ['+', '−', '+', '−']):
    text(ax, c, 62, sg, 'varie', 'xl', weight='bold')
r2 = [r'$x^2$', r'$5x$', r'$6$']
r3 = [r'$x^3$', r'$9x^2$', r'$26x$', r'$24$']
text(ax, 7, 46, r'$r=2$', 'sujet', 's'); text(ax, 7, 24, r'$r=3$', 'autre', 's')
for c, t in zip(cs, r2):
    box(ax, c - 8, 40, 16, 12, 'sujet', label=t)
for c, t in zip(cs, r3):
    box(ax, c - 8, 18, 16, 12, 'autre', label=t)
text(ax, 44, 6, 'les signes alternent', 'varie', 's')
save(fig, '55-073')
