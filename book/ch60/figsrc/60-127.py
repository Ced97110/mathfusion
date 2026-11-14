import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
x0, ytop, cw, ch = 4, 58, 14, 9
for i in range(4):
    for j in range(2):
        role = 'sujet' if j == 0 else ('varie' if i == 0 else 'fixe')
        box(ax, x0 + j * cw, ytop - (i + 1) * ch, cw, ch, role, label=f'({i}, {j})', size='s', r=0.5)
# K = row 0 (dashed frame)
box(ax, x0 - 0.8, ytop - ch - 0.8, 2 * cw + 1.6, ch + 1.6, 'varie', fill=False, dash=True, lw=1.1, r=0.8)
text(ax, x0 + cw, ytop + 3.5, 'grille 4 × 2', 'fixe', 's')
# legend
lx = 40
disc(ax, lx + 2, 48, 2.2, 'sujet'); text(ax, lx + 6.5, 48, r'$\langle g\rangle$, $g = (1, 0)$', 'sujet', 's', ha='left')
text(ax, lx + 6.5, 43, 'ordre 4, le plus grand', 'sujet', 's', ha='left')
disc(ax, lx + 2, 33, 2.2, 'varie'); text(ax, lx + 6.5, 33, r'$K = \langle (0, 1)\rangle$', 'varie', 's', ha='left')
text(ax, lx + 6.5, 28, '2 éléments', 'varie', 's', ha='left')
text(ax, 64, 14, r'$G = \langle g\rangle \oplus K$', 'resultat', 'l', weight='bold')
save(fig, '60-127')
