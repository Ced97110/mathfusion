import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
bw, g = 17, (84 - 4 * 17) / 3
xs = [2 + i * (bw + g) for i in range(4)]
labs = ['v', '(T − r)v', '(T − r)²v', '0']
roles = ['sujet', 'sujet', 'sujet', 'resultat']
for x, lab, role in zip(xs, labs, roles):
    box(ax, x, 44, bw, 11, role, label=lab, size='s')
for i in range(3):
    arrow(ax, (xs[i] + bw + 0.3, 49.5), (xs[i + 1] - 0.3, 49.5), 'varie')
    text(ax, xs[i] + bw + g / 2, 58, str(i + 1), 'varie', 'm', weight='bold')
brace(ax, xs[0] + bw / 2, xs[3] + bw / 2, 42, 'varie', label='3 flèches avant 0 : longueur 3', size='s')
text(ax, 44, 30, '(T − r)²v ≠ 0 : trois, pas moins', 'fixe', 's')
box(ax, 10, 6, 68, 14, 'resultat', label='annulateur de v : (λ − r)³', size='m')
arrow(ax, (44, 26), (44, 21), 'resultat')
save(fig, '60-183')
