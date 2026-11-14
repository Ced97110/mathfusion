import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 68, r'$E=\mathbb{Q}(\sqrt{2},\sqrt{3})$, $F=\mathbb{Q}$', 'fixe', 's')
cols = [r'$\sqrt{3}\mapsto\sqrt{3}$', r'$\sqrt{3}\mapsto-\sqrt{3}$']
rows = [r'$\sqrt{2}\mapsto\sqrt{2}$', r'$\sqrt{2}\mapsto-\sqrt{2}$']
xs = [30, 60]
ys = [38, 22]
for i, c in enumerate(cols):
    text(ax, xs[i] + 12, 58, c, 'sujet', 's')
for j, r in enumerate(rows):
    text(ax, 14, ys[j] + 7, r, 'autre', 's')
pairs = [[(r'$\sqrt{2}$', r'$\sqrt{3}$'), (r'$\sqrt{2}$', r'$-\sqrt{3}$')],
         [(r'$-\sqrt{2}$', r'$\sqrt{3}$'), (r'$-\sqrt{2}$', r'$-\sqrt{3}$')]]
vals = [[r'$(\sqrt{2},\sqrt{3})$', r'$(\sqrt{2},-\sqrt{3})$'],
        [r'$(-\sqrt{2},\sqrt{3})$', r'$(-\sqrt{2},-\sqrt{3})$']]
for j in range(2):
    for i in range(2):
        box(ax, xs[i], ys[j], 24, 14, 'fixe', label=vals[j][i], size='s')
text(ax, 44, 11, r'au plus $2\times2=4$ automorphismes', 'resultat', 's')
text(ax, 44, 4, r'$[E:F]=4$', 'resultat', 'm')
save(fig, '63-081')
