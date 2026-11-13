import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
s = 5.0; ox, oy = 6, 8
P = lambda x, y: (ox + x * s, oy + y * s)
cs = list(range(-2, 6))
fx = lambda c: P(c + 8, 0)[0]
for c in cs:
    p0 = (c, 0) if c >= 0 else (0, -c / 2)
    line(ax, [P(*p0), P(c + 8, 4)], 'sujet' if c == 0 else 'fixe', lw=1.5 if c == 0 else 0.8)
    arrow(ax, (fx(c), P(0, 4)[1] + 1.2), (fx(c), 48), 'varie', lw=0.9)
    text(ax, fx(c), 53.5, f'{c}'.replace('-', '−'), 'resultat', 's')
line(ax, [(fx(-2) - 3, 50.5), (fx(5) + 3, 50.5)], 'resultat', lw=1.2)
text(ax, 6, 64, 'classes du quotient (droites)', 'sujet', 's', ha='left')
text(ax, 6, 60, 'image : tous les entiers', 'resultat', 's', ha='left')
text(ax, 10, 3, 'noyau', 'sujet', 's')
save(fig, '57-156')
