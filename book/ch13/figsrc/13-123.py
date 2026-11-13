import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
for y0, a, b, lab in [(60, -12, 13, '+ 25 : −12 + 25 = 13'), (22, 13, -7, '13 − (−7) = 20')]:
    f = numberline(ax, 6, 76, y0, -15, 15, 5, every=3)
    ax.plot([f(0)] * 2, [y0 - 1.2, y0 + 1.2], color=COL['fixe'])
    disc(ax, f(a), y0, 1.7, 'sujet'); disc(ax, f(b), y0, 1.7, 'resultat' if y0 > 30 else 'varie')
    arrow(ax, (f(a), y0 + 3), (f(b), y0 + 3), 'varie', curve=-0.35 if b > a else 0.35)
    text(ax, f(a), y0 - 8, str(a).replace('-', '−'), 'sujet', 's'); text(ax, f(b), y0 - 8, str(b).replace('-', '−'), 'resultat' if y0 > 30 else 'varie', 's')
    text(ax, (f(a) + f(b)) / 2, y0 + 15, lab, 'varie', 's')
save(fig, '13-123')
