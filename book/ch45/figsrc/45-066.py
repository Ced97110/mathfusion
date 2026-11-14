import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cs = 8.5; roles = ['fixe', 'sujet', 'varie', 'autre']
def table(x0, y0):
    for i in range(4):
        for j in range(4):
            box(ax, x0 + j * cs, y0 + (3 - i) * cs, cs, cs, roles[(i + j) % 4], r=0.2, lw=0.5)
    line(ax, [(x0, y0 + 4 * cs), (x0 + 4 * cs, y0)], 'encre', lw=0.9, dash=True)
    for (i, j) in [(1, 2), (2, 1)]:
        box(ax, x0 + j * cs, y0 + (3 - i) * cs, cs, cs, 'encre', fill=False, r=0.2, lw=1.6)
        text(ax, x0 + (j + 0.5) * cs, y0 + (3 - i + 0.5) * cs, f'${i}+{j}$', 'encre', 's')
table(3, 26); table(51, 26)
arrow(ax, (38, 43), (50, 43), 'varie', lw=1.2); text(ax, 44, 47, r'$\eta$', 'varie', 'l')
text(ax, 20, 66, 'horloge', 'sujet', 'm'); text(ax, 68, 66, 'rotations', 'sujet', 'm')
text(ax, 44, 20, 'cases cerclées : symétriques', 'encre', 's')
for k, (r, t) in enumerate(zip(roles, ['0', '1', '2', '3'])):
    box(ax, 6 + k * 14, 2, 6, 6, r, r=0.2, lw=0.5); text(ax, 14.5 + k * 14, 5, t, 'encre', 's', ha='center')
text(ax, 44, 13, 'même couleur des deux côtés', 'encre', 's')
save(fig, '45-066')
