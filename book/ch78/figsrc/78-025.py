import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
names = [('ℝ', 1), ('ℂ', 2), ('ℍ', 4), ('𝕆', 8)]
roles = ['sujet', 'sujet', 'sujet', 'sujet']
for k, (n, d) in enumerate(names):
    box(ax, 4, 6 + 24 * k, 32, 14, 'sujet', label=f'{n}  dimension {d}')
lost = ["perd l'ordre", 'perd la commutativité', "perd l'associativité"]
for k, t in enumerate(lost):
    y0 = 20 + 24 * k
    arrow(ax, (20, y0), (20, y0 + 10), 'varie', lw=1.4)
    text(ax, 24, y0 + 5, '×2', 'varie', 's', ha='left')
    text(ax, 33, y0 + 5, t, 'limite', 's', ha='left')
box(ax, 44, 78, 40, 14, 'resultat', label=r'$|xy| = |x||y|$')
arrow(ax, (82, 12), (82, 76), 'resultat', lw=1.4)
text(ax, 86, 44, 'vrai aux 4 étages', 'resultat', 's', rot=90)
save(fig, '78-025')
