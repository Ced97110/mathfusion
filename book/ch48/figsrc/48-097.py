import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
Z = r'$\mathbb{Z}/12\mathbb{Z}$'
N = {'0': (43, 10, 14, '{0}'), '6': (22, 32, 20, '{0, 6}'), '4': (64, 32, 24, '{0, 4, 8}'),
     '3': (18, 54, 26, '{0, 3, 6, 9}'), '2': (64, 54, 34, '{0, 2, 4, 6, 8, 10}'), 'G': (43, 76, 34, Z)}
E = [('0', '6'), ('0', '4'), ('6', '3'), ('6', '2'), ('4', '2'), ('3', 'G'), ('2', 'G')]
for a, b in E:
    line(ax, [(N[a][0], N[a][1] + 4), (N[b][0], N[b][1] - 4)], 'fixe', lw=1.0)
for k, (x, y, w, s) in N.items():
    box(ax, x - w / 2, y - 4, w, 8, 'sujet', label=s, size='s')
text(ax, 2, 10, 'ligne montante :', 'fixe', 's', ha='left')
text(ax, 2, 5, '« contenu dans »', 'fixe', 's', ha='left')
save(fig, '48-097')
