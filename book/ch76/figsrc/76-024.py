import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'dans $\mathbb{Q}(\sqrt{2})$', 'sujet', 'm', weight='bold')
cw, ch, gx, gy = 14, 10, 24, 26
vals = [['3', r'$\sqrt{2}$'], [r'$3\sqrt{2}$', '2']]
for c, h in enumerate([r'$3$', r'$\sqrt{2}$']): text(ax, gx + c * cw + cw / 2, gy + 2 * ch + 4, h, 'autre', 'm')
text(ax, gx + cw, gy + 2 * ch + 10, r'$3 + \sqrt{2}$', 'autre', 'm')
for r, h in enumerate([r'$1$', r'$\sqrt{2}$']): text(ax, gx - 3, gy + (1 - r) * ch + ch / 2, h, 'sujet', 'm')
text(ax, 10, gy + 2 * ch + 4, r'$1+\sqrt{2}$', 'sujet', 's')
for r in range(2):
    for c in range(2):
        box(ax, gx + c * cw, gy + (1 - r) * ch, cw, ch, 'fixe', label=vals[r][c])
arrow(ax, (gx + 2 * cw + 2, gy + ch), (66, gy + ch), 'varie'); text(ax, 60, gy + ch + 4, 'somme', 'varie', 's')
box(ax, 66, gy + ch - 5, 20, 10, 'resultat', label=r'$5 + 4\sqrt{2}$', size='s')
text(ax, 76, gy + ch - 9, 'deux rationnels', 'resultat', 's')
text(ax, 44, 12, 'un seul produit calculé', 'fixe', 's')
save(fig, '76-024')
