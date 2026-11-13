import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u, x0 = 10.5, 20
text(ax, 44, 60, 'cadran à 4 heures : 5 pas = 1', 'fixe', 'm')
def row(y, parts, lab):
    x = x0
    for n, role in parts:
        box(ax, x, y, n * u, 9, role, label=str(n), size='l'); x += n * u
    b = [n * u for n, _ in parts][0]
    for k in range(1, 5):
        if k != parts[0][0]: line(ax, [(x0 + k * u, y + 1.2), (x0 + k * u, y + 3.2)], 'encre', lw=0.5)
    text(ax, 10, y + 4.5, lab, 'encre', 'm')
    text(ax, 80, y + 4.5, '= 1', 'resultat', 'm', weight='bold')
row(40, [(2, 'sujet'), (3, 'varie')], '2 + 3')
row(22, [(3, 'varie'), (2, 'sujet')], '3 + 2')
box(ax, 14, 3, 60, 9, 'resultat', label='même arrivée : 1', size='m')
save(fig, '51-035')
