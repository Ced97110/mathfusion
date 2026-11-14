import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
groups = [('centre', 'fixe', False), (r'$y_1$', 'sujet', True), (r'$y_2$', 'sujet', True), (r'$y_3$', 'sujet', True)]
bw = 17; gap = 4; x0 = (W - (4 * bw + 3 * gap)) / 2; y = 30
for k, (lab, role, rep) in enumerate(groups):
    x = x0 + k * (bw + gap)
    box(ax, x, y - 5, bw, 10, role)
    for j in range(2):
        disc(ax, x + bw / 2 - 3.5 + 7 * j, y, 2.2, 'varie' if (rep and j == 0) else role)
    text(ax, x + bw / 2, y + 9, lab, 'varie' if rep else 'fixe', 'm')
    text(ax, x + bw / 2, y - 10, '2', role, 'l', weight='bold')
brace(ax, x0, W - x0, 41, 'sujet', None, down=False, depth=2.4)
text(ax, W / 2, 49, r'$|G|$ = 8 éléments', 'sujet', 'm')
text(ax, W / 2, 10, r'$8 = |C| + \sum_j [G:C(y_j)] = 2 + 2 + 2 + 2$', 'resultat', 'm', weight='bold')
save(fig, '49-181')
