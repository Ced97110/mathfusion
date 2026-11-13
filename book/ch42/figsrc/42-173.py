import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
gxs = [14, 42, 68]; rows = {'a': 22, 'b': 32}
chosen = [[(0, 'a'), (1, 'a'), (2, 'b')], [(0, 'a'), (0, 'b'), (1, 'a'), (2, 'b')], [(0, 'a'), (2, 'b')]]
titles = ['une\napplication', '1 a deux\nlettres', '2 n\'a\naucune']
for g, (gx, ch, ti) in enumerate(zip(gxs, chosen, titles)):
    role = 'resultat' if g == 0 else 'limite'
    for i in range(3):
        text(ax, gx + 8 * i, 14, str(i + 1), 'sujet', 's')
        for n, y in rows.items():
            if (i, n) in ch: disc(ax, gx + 8 * i, y, 2.3, 'limite' if (g == 1 and i == 0) else 'sujet')
            else: disc(ax, gx + 8 * i, y, 1.2, 'fixe', fill=False)
    if g == 2: box(ax, gx + 8 - 3.5, 17, 7, 20, 'limite', fill=False, dash=True)
    text(ax, gx + 8, 45, ti, role, 's', weight='bold')
text(ax, 8, 22, 'a', 'autre', 's'); text(ax, 8, 32, r'$b$', 'autre', 's')
save(fig, '42-173')
