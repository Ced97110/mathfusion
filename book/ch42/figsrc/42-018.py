import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
bw, bh = 16, 8; xs = [24, 44, 64]
rows = {0: [(44, r'$\emptyset$')], 1: list(zip(xs, [r'$\{a\}$', r'$\{b\}$', r'$\{c\}$'])),
        2: list(zip(xs, [r'$\{a,b\}$', r'$\{a,c\}$', r'$\{b,c\}$'])), 3: [(44, r'$\{a,b,c\}$')]}
ys = {0: 6, 1: 27, 2: 48, 3: 69}
edges = [(0,44,1,24),(0,44,1,44),(0,44,1,64),(1,24,2,24),(1,24,2,44),(1,44,2,24),(1,44,2,64),(1,64,2,44),(1,64,2,64),
         (2,24,3,44),(2,44,3,44),(2,64,3,44)]
for l0, x0, l1, x1 in edges:
    line(ax, [(x0, ys[l0] + bh), (x1, ys[l1])], 'fixe', lw=1.0)
for l, items in rows.items():
    for x, lab in items:
        box(ax, x - bw/2, ys[l], bw, bh, 'sujet', label=lab, size='s')
    text(ax, 7, ys[l] + bh/2, f'niveau {l}', 'fixe', 's')
text(ax, 71, 12, 'trait : +1 objet', 'varie', 's')
save(fig, '42-018')
