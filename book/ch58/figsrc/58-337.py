import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# le signe [L : K] découpé, chaque morceau relié à son sens
yS = 52
xs = dict(lb=22, L=29, col=37, K=45, rb=52, eq=66)
big = 16
text(ax, xs['lb'], yS, '[', 'encre', big)
text(ax, xs['L'], yS, r'$L$', 'sujet', big, weight='bold')
text(ax, xs['col'], yS, ':', 'encre', big)
text(ax, xs['K'], yS, r'$K$', 'varie', big, weight='bold')
text(ax, xs['rb'], yS, ']', 'encre', big)
text(ax, xs['eq'], yS, r'$=\,2$', 'resultat', big, weight='bold')
# sens de chaque morceau
yL = 22
text(ax, 17, yL, r'$L = \mathbb{Q}(\sqrt{2})$', 'sujet', 's')
text(ax, 17, yL - 5, 'le corps qui contient', 'sujet', 's')
text(ax, 47, yL, r'$K = \mathbb{Q}$', 'varie', 's')
text(ax, 47, yL - 5, 'les scalaires', 'varie', 's')
text(ax, 73, yL, 'dimension', 'resultat', 's')
text(ax, 73, yL - 5, '2 vecteurs de base', 'resultat', 's')
arrow(ax, (17, yL + 4), (xs['L'] - 1.5, yS - 6), 'sujet', lw=0.9)
arrow(ax, (47, yL + 4), (xs['K'] + 0.5, yS - 6), 'varie', lw=0.9)
arrow(ax, (73, yL + 4), (xs['eq'] + 2, yS - 6), 'resultat', lw=0.9)
save(fig, '58-337')
