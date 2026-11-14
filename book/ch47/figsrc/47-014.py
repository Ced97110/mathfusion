import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 68, 'Chaque heure a une ligne', 'encre', 'm')
roles = ['sujet', 'varie', 'autre']
for h in range(12):
    box(ax, 2 + h * 7.2, 50, 6.4, 8, roles[h % 3], label=str(h), size='s', r=0.3, lw=0.6)
    xb = 2 + h * 7.2 + 3.2; tx = 22 + (h % 3) * 22 + (h // 3 - 1.5) * 3.2
    line(ax, [(xb, 49.5), (tx, 24)], roles[h % 3], lw=0.6)
for k in range(3):
    box(ax, 6 + k * 27, 8, 24, 15, roles[k], label=f'reste {k}', size='m')
text(ax, 44, 2, '12 heures, aucune oubliée', 'resultat', 's')
save(fig, '47-014')
