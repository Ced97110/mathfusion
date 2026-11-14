import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# mêmes nombres, deux écritures : colonnes (livre) ou lignes (Jacobson)
cw, ch = 9, 7
text(ax, 17, 59, 'le livre : colonnes', 'encre', 's', weight='bold')
text(ax, 71, 59, 'Jacobson : lignes', 'encre', 's', weight='bold')
for cy, name, vals, role in [(42, 'sac (5, 4)', ('5', '4'), 'sujet'), (20, 'image de $e_1$', ('2', '1'), 'autre')]:
    text(ax, 44, cy, name, role, 's')
    # livre : en colonne
    for k, v in enumerate(vals):
        box(ax, 12.5, cy + 0.6 - k * (ch + 1) + (ch + 1) / 2, cw, ch, role, label=v, size='m', r=0.5)
    # Jacobson : en ligne
    for k, v in enumerate(vals):
        box(ax, 61.5 + k * (cw + 1), cy - ch / 2, cw, ch, role, label=v, size='m', r=0.5)
box(ax, 14, 2, 60, 8, 'resultat', label='mêmes nombres, rangés autrement', size='s', r=0.5)
save(fig, '58-199')
