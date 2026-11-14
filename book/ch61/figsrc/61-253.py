import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 10, 74, 18, -1, 1, 0.5, arrow_right=False, every=1)
for v, l, y, r in [(0.94, 'cos 20° ≈ 0,94', 8, 'sujet'), (-0.77, 'cos 140° ≈ −0,77', 8, 'varie'), (-0.17, 'cos 260° ≈ −0,17', 3, 'varie')]:
    disc(ax, f(v), 18, 2, r); text(ax, f(v), y, l, r, 's')
arrow(ax, (f(0.94), 20.5), (f(-0.17), 20.5), 'varie', curve=0.45)
arrow(ax, (f(0.94) - 1, 20.5), (f(-0.77), 20.5), 'varie', curve=0.2)
text(ax, f(0.38), 36, '?', 'varie', 'l'); text(ax, f(0.1), 28.5, '?', 'varie', 'l')
text(ax, 44, 47, r'$\mathbb{Q}(\cos 20°)$ les contient-il ?', 'sujet', 'm')
save(fig, '61-253')
