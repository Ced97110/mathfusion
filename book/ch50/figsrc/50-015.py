import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 10, 43, r'$d$', 'encre', 'l')
xs = [24 + 11 * i for i in range(6)]
for x, d in zip(xs, [1, 2, 3, 4, 6, 12]): text(ax, x, 43, str(d), 'encre', 'm')
rows = [(30, r'$\mathbb{Z}/12\mathbb{Z}$', 'sujet', [1] * 6), (17, r'$A_4$', 'autre', [1, 1, 1, 1, 0, 1])]
for y, name, role, ans in rows:
    text(ax, 10, y, name, role, 'm')
    for x, a in zip(xs, ans):
        if a: box(ax, x - 4.5, y - 4.5, 9, 9, 'resultat', r=0.5); disc(ax, x, y, 2.2, 'resultat', fill=False, lw=1.2)
        else:
            box(ax, x - 4.5, y - 4.5, 9, 9, 'limite', r=0.5)
            line(ax, [(x - 2.2, y - 2.2), (x + 2.2, y + 2.2)], 'limite', lw=1.4); line(ax, [(x - 2.2, y + 2.2), (x + 2.2, y - 2.2)], 'limite', lw=1.4)
box(ax, xs[4] - 6, 9.5, 12, 28, 'varie', fill=False, dash=True, lw=1.0)
disc(ax, 25, 4, 2, 'resultat', fill=False, lw=1.2); text(ax, 29, 4, 'oui', 'resultat', 's', ha='left')
line(ax, [(45, 2), (49, 6)], 'limite', lw=1.4); line(ax, [(45, 6), (49, 2)], 'limite', lw=1.4); text(ax, 51, 4, 'non', 'limite', 's', ha='left')
save(fig, '50-015')
