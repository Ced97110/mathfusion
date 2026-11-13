import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# integers 0..24, multiples of 3 in violet, multiples of 12 in blue
f = numberline(ax, 6, 76, 62, 0, 24, 1, labels=False, arrow_right=False, tick=0.8)
for v in range(0, 25, 3):
    big = v % 12 == 0
    disc(ax, f(v), 62, 2.0 if big else 1.4, 'sujet' if big else 'autre')
for v in (0, 12, 24):
    text(ax, f(v), 55.5, str(v), 'sujet', 's')
text(ax, 44, 74, r'$G=\mathbb{Z}$ : les entiers', 'fixe', 'm')
text(ax, 22, 48, r'$N$ = 12ℤ', 'sujet', 's'); text(ax, 62, 48, r'$H$ = 3ℤ', 'autre', 's')
# three steps of the proof
box(ax, 2, 24, 26, 18, 'fixe', label=None)
text(ax, 15, 38, 'départ', 'fixe', 's'); text(ax, 15, 31, 'ℤ, 12ℤ, 3ℤ', 'encre', 's')
box(ax, 31, 24, 26, 18, 'varie', label=None, lw=1.6)
text(ax, 44, 38, 'étape clé', 'varie', 's'); text(ax, 44, 31, '12ℤ ⊆ 3ℤ', 'encre', 's')
box(ax, 60, 24, 26, 18, 'resultat', label=None)
text(ax, 73, 38, 'arrivée', 'resultat', 's'); text(ax, 73, 31, 'ℤ/12ℤ… ≅ ℤ/3ℤ', 'encre', 's')
arrow(ax, (28.5, 33), (30.5, 33), 'fixe'); arrow(ax, (57.5, 33), (59.5, 33), 'fixe')
text(ax, 44, 17, '24 = 3 × 8 : 24 est dans 3ℤ', 'varie', 's')
save(fig, '48-177')
