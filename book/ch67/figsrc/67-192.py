import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
R = 7.5
ys = [72, 50, 28]
labs = [r'$\alpha+1$', r'$\alpha^{2}+1$', r'$\alpha^{2}+\alpha+1$']
coords = ['(1, 1, 0)', '(1, 0, 1)', '(1, 1, 1)']
text(ax, 18, 90, 'conjugués', 'varie', 'm')
text(ax, 62, 90, r'coordonnées sur $(1,\ \alpha,\ \alpha^{2})$', 'encre', 's')
for y, l, c in zip(ys, labs, coords):
    disc(ax, 18, y, R, 'varie', label=l, size='s')
    arrow(ax, (26, y), (49, y), 'fixe')
    text(ax, 62, y, c, 'varie', 'l')
arrow(ax, (18, ys[0] - R), (18, ys[1] + R), 'varie')
arrow(ax, (18, ys[1] - R), (18, ys[2] + R), 'varie')
arrow(ax, (10.5, ys[2]), (10.5, ys[0]), 'varie', curve=-0.35)
text(ax, 27, 61, 'carré', 'varie', 's', ha='left')
text(ax, 27, 39, 'carré', 'varie', 's', ha='left')
box(ax, 10, 4, 68, 12, 'resultat', label=r'$\det=-1\neq0$ : base normale')
save(fig, '67-192')
