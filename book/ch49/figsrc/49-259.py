import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for y, role, k, name in [(52, 'sujet', 2, 'circuit A'), (22, 'autre', 3, 'circuit B')]:
    box(ax, 3, y - 8, 30, 16, role)
    text(ax, 18, y + 11, name, role, 's')
    for i in range(k):
        xx = 18 + (i - (k - 1) / 2) * 8
        box(ax, xx - 3, y - 3, 6, 6, 'fixe', r=0.6)
    arrow(ax, (33, y), (52, 37 + (3 if y > 40 else -3)), role)
box(ax, 52, 27, 33, 20, 'resultat')
text(ax, 68.5, 41, 'fonction', 'resultat', 'm', weight='bold')
text(ax, 68.5, 33, 'booléenne', 'resultat', 'm', weight='bold')
text(ax, 68.5, 21, r'$n$ chiffres $\to$ 0 ou 1', 'resultat', 's')
text(ax, 60, 63, 'même sortie pour chaque suite', 'encre', 's')
text(ax, 18, 6, 'appareils différents', 'fixe', 's')
save(fig, '49-259')
