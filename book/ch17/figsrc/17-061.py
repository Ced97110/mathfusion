import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
def pair(yb, ya, vmax, a, b, ra, rb, lab):
    f = lambda v: 8 + v / vmax * 66
    for y, pts, role in [(yb, (a, b), 'sujet'), (ya, (ra, rb), 'resultat')]:
        line(ax, [(8, y), (76, y)], 'fixe')
        for v in pts:
            disc(ax, f(v), y, 1.5, role)
            text(ax, f(v), y + (4.2 if y == yb else -4.2), str(v).replace('.', ','), role, 's')
    for p, q in [(a, ra), (b, rb)]: arrow(ax, (f(p), yb - 1.8), (f(q), ya + 1.8), 'varie')
    return f
pair(88, 62, 56, 3, 7, 24, 56, '')
text(ax, 62, 75, r'$\times 8$ : plus loin de 0', 'varie', 's')
pair(38, 12, 8, 3, 7, 1.5, 3.5, '')
text(ax, 60, 25, r'$\times \frac{1}{2}$ : plus près de 0', 'varie', 's')
line(ax, [(8, 94), (8, 6)], 'fixe', dash=True)
text(ax, 8, 98, '0', 'fixe', 's')
save(fig, '17-061')
