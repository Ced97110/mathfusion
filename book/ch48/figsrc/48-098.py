import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
Z = r'$\mathbb{Z}/12\mathbb{Z}$'
N = {'0': (43, 10, 14, '{0}'), '6': (22, 32, 20, '{0, 6}'), '4': (64, 32, 24, '{0, 4, 8}'),
     '3': (18, 54, 26, '{0, 3, 6, 9}'), '2': (64, 54, 34, '{0, 2, 4, 6, 8, 10}'), 'G': (43, 76, 34, Z)}
E = [('0', '6'), ('0', '4'), ('6', '3'), ('6', '2'), ('4', '2'), ('3', 'G'), ('2', 'G')]
for a, b in E:
    line(ax, [(N[a][0], N[a][1] + 4), (N[b][0], N[b][1] - 4)], 'fixe', lw=1.0)
for k, (x, y, w, s) in N.items():
    box(ax, x - w / 2, y - 4, w, 8, 'limite' if k in '04' else 'sujet', label=s, size='s')
box(ax, 2, 10, 4, 4, 'sujet'); text(ax, 8, 12, 'contient 6', 'sujet', 's', ha='left')
box(ax, 2, 3, 4, 4, 'limite'); text(ax, 8, 5, 'ne contient pas 6', 'limite', 's', ha='left')
text(ax, 74, 76, '4 cases bleues', 'sujet', 's')
save(fig, '48-098')
