import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
# L (11), a = 5, b = 3 : 11 -> 55 -> 58 -> 6 (G)
bw, gap, x0 = 15.0, 8.0, 2.0
xs = [x0 + i * (bw + gap) for i in range(4)]
labels = ['L : 11', '55', '58', 'G : 6']
roles = ['sujet', 'varie', 'varie', 'resultat']
for x, l, r in zip(xs, labels, roles):
    box(ax, x, 50, bw, 11, r, label=l, weight='bold' if r == 'resultat' else 'normal')
for i, t in enumerate(['×5', '+3', 'mod 26']):
    xa = xs[i] + bw + 0.4
    arrow(ax, (xa, 55.5), (xa + gap - 0.8, 55.5), 'fixe')
    text(ax, xa + gap / 2, 64, t, 'varie', 's')
text(ax, 44, 70, 'multiplier, puis ajouter', 'sujet', 'm', weight='bold')
box(ax, 14, 30, 60, 10, 'sujet', label=r'clé : le couple $(a,\,b)=(5,\,3)$')
line(ax, [(44, 49), (44, 41)], 'sujet', lw=0.8, dash=True)
box(ax, 2, 6, 40, 11, 'fixe', label='$a=1$ : César')
box(ax, 46, 6, 40, 11, 'autre', label='$b=0$ : seulement ×')
line(ax, [(22, 18), (22, 24), (66, 24), (66, 18)], 'fixe', lw=0.6)
line(ax, [(44, 24), (44, 29)], 'fixe', lw=0.6)
save(fig, '53-043')
