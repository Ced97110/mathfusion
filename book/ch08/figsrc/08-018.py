import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
rows = [(74, 2, 3, 0.35, 'varie_off', '1 chiffre : dixièmes', ('2', '3'), (2.3, 2.4)),
        (46, 2.3, 2.4, 0.5, 'varie', '2 chiffres : centièmes', ('2,3', '2,4'), (2.35, 2.36)),
        (18, 2.35, 2.36, 0.4, 'varie', '3 chiffres : millièmes', ('2,35', '2,36'), None)]
x0, x1 = 8, 78
for y, a, b, p, role, title, ends, hl in rows:
    r = 'fixe' if role == 'varie_off' else 'varie'
    f = numberline(ax, x0, x1, y, a, b, (b - a) / 10, labels=False, role=r, arrow_right=False)
    text(ax, x0, y - 3.6, ends[0], r, 's'); text(ax, x1, y - 3.6, ends[1], r, 's')
    text(ax, x0 - 4, y + 11, title, 'encre', 's', ha='left')
    px = f(a + p * (b - a)); disc(ax, px, y, 1.3, 'sujet')
    text(ax, px, y + 5, 'P', 'sujet', 'm', weight='bold')
    if hl:
        line(ax, [(f(hl[0]), y), (f(hl[1]), y)], 'varie', lw=2.6)
fig_ = save(fig, '08-018')
