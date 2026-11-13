import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(112)
def grid(cx, cy, filled, names=False):
    S = 18 if names else 12; hf = 15 if names else 12
    box(ax, cx - hf, cy - hf, 2 * hf, 2 * hf, 'fixe', fill=False)
    for (i, j) in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        x, y = cx - S / 2 + S * i, cy - S / 2 + S * j
        on = (i, j) in filled
        disc(ax, x, y, 2.4, ('fixe' if (i, j) == (0, 0) else 'sujet') if on else 'fixe', fill=on)
        if names: text(ax, x, y + (4.2 if j else -4.2), f'({i}, {j})', 'sujet' if on and (i, j) != (0, 0) else 'fixe', 's')
nodes = {'0': (44, 20, {(0, 0)}), 'D1': (14, 58, {(0, 0), (1, 0)}), 'D2': (44, 58, {(0, 0), (0, 1)}),
         'D3': (74, 58, {(0, 0), (1, 1)}), 'E': (44, 96, {(0, 0), (1, 0), (0, 1), (1, 1)})}
for k in ('D1', 'D2', 'D3'):
    x = nodes[k][0]
    line(ax, [(44, 32), (x, 46)], 'fixe'); line(ax, [(x, 70), (44, 81)], 'fixe')
for k, (x, y, f) in nodes.items():
    grid(x, y, f, names=(k == 'E'))
text(ax, 31, 20, r'$\{0\}$', 'fixe', 'm', ha='right')
text(ax, 14, 73, r'$D_1$', 'sujet', 'm'); text(ax, 44, 73, r'$D_2$', 'sujet', 'm'); text(ax, 74, 73, r'$D_3$', 'sujet', 'm')
text(ax, 62, 96, r'$E$', 'sujet', 'm', ha='left')
text(ax, 2, 106, 'plan $\\mathbb{F}_2^2$ :\n4 vecteurs', 'encre', 's', ha='left')
disc(ax, 61, 22, 1.8, 'fixe'); text(ax, 64.5, 22, 'nul, commun à tous', 'fixe', 's', ha='left')
disc(ax, 61, 16, 1.8, 'sujet'); text(ax, 64.5, 16, 'vecteur dedans', 'sujet', 's', ha='left')
disc(ax, 61, 10, 1.8, 'fixe', fill=False); text(ax, 64.5, 10, 'vecteur dehors', 'fixe', 's', ha='left')
save(fig, '79-149')
