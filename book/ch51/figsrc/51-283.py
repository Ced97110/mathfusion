import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, 'nombres réels pour décrire un élément', 'fixe', 's')
xs = (10, 31, 52, 73)
for x, n, name, role in zip(xs, (1, 2, 3, 4), ('ℝ', 'ℂ', 'aucun', 'ℍ'), ('sujet', 'sujet', 'limite', 'sujet')):
    for k in range(n):
        box(ax, x - 5, 52 - k * 7.5, 10, 6.5, role, fill=role != 'limite', r=0.6, dash=role == 'limite')
    text(ax, x, 18, str(n), role, 'l')
    text(ax, x, 9, name, role, 's')
save(fig, '51-283')
