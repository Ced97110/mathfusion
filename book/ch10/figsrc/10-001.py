import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
k = 0.37; x0 = 4; h = 8
rows = [(50, 'de tête : 23 + 61 = 84', 'sujet', False), (32, 'écran 84,63 : proche de 84', 'resultat', True), (14, 'écran 184,63 : 100 de plus', 'limite', True)]
for i, (y, lab, role, cent) in enumerate(rows):
    text(ax, x0, y + 12, lab, role, 'm', ha='left')
    box(ax, x0, y, 84 * k, h, 'sujet', label='84')
    if cent:
        xs = x0 + 84.3 * k
        line(ax, [(xs, y), (xs, y + h)], 'varie', lw=1.6)
    if i == 2:
        box(ax, x0 + 84.63 * k, y, 100 * k, h, 'limite', label='+ 100')
text(ax, x0, 4, 'trait orange : centimes retirés, 0,63', 'varie', 's', ha='left')
save(fig, '10-001')
