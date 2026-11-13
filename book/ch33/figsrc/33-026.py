import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for y, lo, cap, role in ((48, -2, 'de −2 à 3 : 4 vient de deux', 'limite'), (16, 0, 'de 0 à 3 : 4 vient d’un seul', 'resultat')):
    f = numberline(ax, 6, 54, y, -3, 4, labels=False, arrow_right=False)
    line(ax, [(f(lo), y), (f(3), y)], 'sujet', lw=3)
    pts = (-2, 2) if lo == -2 else (2,)
    for p in pts:
        disc(ax, f(p), y, 1.8, 'varie')
    for v in sorted({lo, 2, 3}):
        text(ax, f(v), y - 4.6, f'{v}'.replace('-', '−') + '°' * 0, 'sujet', 's')
    disc(ax, 74, y, 5, role, label='4')
    arrow(ax, (f(2) + 1, y + 2), (69.3, y + 1.5), 'varie')
    if lo == -2:
        arrow(ax, (f(-2), y + 2.5), (70, y + 3.6), 'varie', curve=-0.3)
    text(ax, 44, y - 10, cap, role, 's')
save(fig, '33-026')
