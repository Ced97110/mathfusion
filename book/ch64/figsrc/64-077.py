import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 30, 52, 28, 9, 'sujet', label=r'$G_1=\mathbb{Z}/6$')
box(ax, 2, 30, 30, 9, 'sujet', label=r'$G_2=\{0,2,4\}$', size='s')
box(ax, 56, 30, 30, 9, 'autre', label=r'$H_2=\{0,3\}$', size='s')
box(ax, 22, 8, 44, 11, 'varie', label=r'$K_3=G_2\cap H_2=\{0\}$', size='s')
edges = [((37, 52), (20, 39), 'sujet', r'$\mathbb{Z}/2$', (24, 48)),
         ((51, 52), (68, 39), 'autre', r'$\mathbb{Z}/3$', (64, 48)),
         ((20, 30), (37, 19), 'autre', r'$\mathbb{Z}/3$', (24, 24)),
         ((68, 30), (51, 19), 'sujet', r'$\mathbb{Z}/2$', (64, 24))]
for p, q, role, lab, tp in edges:
    arrow(ax, p, q, role)
    text(ax, tp[0], tp[1], lab, role, 's')
text(ax, 44, 3, r'$G_1/G_2\cong H_2/K_3$ : facteurs échangés', 'resultat', 's', weight='bold')
save(fig, '64-077')
