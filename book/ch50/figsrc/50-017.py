import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
cols = [1, 2, 3, 4, 6, 12]
x0, cw, ch, gap = 16, 10.0, 9.0, 1.4
rows = [(r'$\mathbb{Z}/12\mathbb{Z}$', 28), (r'$A_4$', 15)]
text(ax, 8, 43, r'$d$', 'encre', 'm')
for i, d in enumerate(cols):
    text(ax, x0 + i * (cw + gap) + cw / 2, 43, str(d), 'encre', 'm')
for name, y in rows:
    text(ax, 8, y + ch / 2, name, 'encre', 's')
    for i, d in enumerate(cols):
        bad = (name == rows[1][0] and d == 6)
        box(ax, x0 + i * (cw + gap), y, cw, ch, 'limite' if bad else 'resultat', lw=1.8 if bad else 0.8)
box(ax, 20, 3, 8, 6, 'resultat'); text(ax, 30, 6, 'oui', 'resultat', 's', ha='left')
box(ax, 50, 3, 8, 6, 'limite'); text(ax, 60, 6, 'non', 'limite', 's', ha='left')
save(fig, '50-017')
