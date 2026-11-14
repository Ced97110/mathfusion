import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# triangle aplati : trois côtés sur une même droite graduée (1 mm par unité x 6)
f = numberline(ax, 8, 68, 30, 0, 10, 1, every=5, arrow_right=False)
def bar(y, a, b, role, label):
    arrow(ax, (f(a), y), (f(b), y), role, lw=1.6)
    text(ax, (f(a) + f(b)) / 2, y + 4, label, role, 's')
bar(52, 0, 10, 'autre', r'$\|v\|=10$')
bar(42, 0, 5, 'sujet', r'$\|u\|=5$')
bar(18, 5, 10, 'varie', r'$\|u-v\|=5$')
for x in (5, 10):
    line(ax, [(f(x), 18), (f(x), 52)], 'fixe', lw=0.4, dash=True)
box(ax, 4, 2, 80, 8, 'resultat', label=r'$|\,5-10\,|=5=\|u-v\|$', size='s')
save(fig, '41-154')
