import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 6, 76, 22, 0, 8, 1)
pts = [1, 2, 4, 8]
for i, v in enumerate(pts):
    role = 'resultat' if v == 8 else ('sujet' if v == 1 else 'varie')
    disc(ax, f(v), 22, 1.5, role)
for a, b in zip(pts[:-1], pts[1:]):
    arrow(ax, (f(a), 25), (f(b), 25), 'varie', curve=-0.45)
    text(ax, (f(a) + f(b)) / 2, 36 if b > 2 else 32.5, '× 2', 'varie', 's')
text(ax, 8, 54, 'r = 2, module de z', 'sujet', 's', ha='left')
text(ax, 8, 48, 'n = 3 fois le facteur r', 'varie', 's', ha='left')
box(ax, 50, 46, 34, 11, 'resultat', label='$r^{3}$ = 2 × 2 × 2 = 8', size='s')
text(ax, f(1), 12, 'départ', 'sujet', 's')
text(ax, f(8), 12, 'arrivée', 'resultat', 's')
save(fig, '39-077')
