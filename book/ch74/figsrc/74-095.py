import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
cx, cy, u = 44, 27, 9
for i in range(-4, 5):
    for j in range(-2, 3):
        disc(ax, cx + i*u*0.9, cy + j*u*0.9, 0.45, 'fixe')
P = lambda a, b: (cx + a*u*0.9, cy + b*u*0.9)
line(ax, [P(2, 1), P(-2, -1)], 'fixe', dash=True)
arrow(ax, P(2, 1), P(-2, -1), 'varie', curve=0.8, lw=1.3)
disc(ax, *P(0, 0), 0.9, 'encre')
disc(ax, *P(2, 1), 1.4, 'sujet'); disc(ax, *P(-2, -1), 1.4, 'resultat')
text(ax, P(2, 1)[0] + 2.5, P(2, 1)[1] + 2, r'$P\ (2\ ;\ 1)$', 'sujet', 's', ha='left')
text(ax, P(-2, -1)[0] - 2.5, P(-2, -1)[1] - 3, r'$R_\theta(P)\ (-2\ ;\ -1)$', 'resultat', 's', ha='left')
text(ax, 44, 49, r'$\theta=180°$ : demi-tour', 'varie', 's')
text(ax, cx + 1.5, cy - 3, 'origine', 'encre', 's', ha='left')
save(fig, '74-095')
