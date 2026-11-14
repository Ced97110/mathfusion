import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
cx, cy, u = 32, 16, 7
for i in range(-3, 4):
    for j in range(-1, 4):
        disc(ax, cx + i*u, cy + j*u, 0.5, 'fixe')
P = lambda a, b: (cx + a*u, cy + b*u)
disc(ax, *P(0, 0), 0.9, 'encre')
for a, b, c, d in [(1, 0, 0, 1), (2, 3, -3, 2)]:
    arrow(ax, P(a, b), P(c, d), 'varie', curve=0.35)
    disc(ax, *P(a, b), 1.3, 'sujet'); disc(ax, *P(c, d), 1.3, 'resultat')
text(ax, P(2, 3)[0] + 3, P(2, 3)[1] + 2, r'$P\ (2\ ;\ 3)$', 'sujet', 's', ha='left')
text(ax, P(-3, 2)[0] - 2, P(-3, 2)[1] - 3.5, r'$f(P)\ (-3\ ;\ 2)$', 'resultat', 's', ha='left')
text(ax, 66, 22, r'$f$ : le quart', 'varie', 's', ha='left')
text(ax, 66, 18.5, 'de tour autour', 'varie', 's', ha='left')
text(ax, 66, 15, 'de l’origine', 'varie', 's', ha='left')
text(ax, 66, 8, 'bleu : point', 'sujet', 's', ha='left')
text(ax, 66, 4.5, 'vert : son image', 'resultat', 's', ha='left')
save(fig, '74-089')
