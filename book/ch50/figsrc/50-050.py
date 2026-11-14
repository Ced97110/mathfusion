import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
X0, CW, CH = 24.0, 7.0, 6.0
def cells(y, members, role):
    for i in range(8):
        on = i in members
        box(ax, X0 + i * CW, y, CW - 0.6, CH, role if on else 'fixe', fill=on, r=0.5, lw=0.7)
rows = [(14, {0, 4}, 'sujet', r'$\{0, 4\}$', r'contenu dans $\{0, 2, 4, 6\}$'),
        (32, {0, 2, 4, 6}, 'sujet', r'$\{0, 2, 4, 6\}$', "contenu dans l'horloge"),
        (50, set(range(8)), 'resultat', 'horloge à 8 h', 'rien de plus grand : maximal')]
for y, mem, role, name, verdict in rows:
    cells(y, mem, role)
    text(ax, 3, y + CH / 2, name, 'encre', 's', ha='left')
    text(ax, X0 + 4 * CW - 0.3, y + CH + 3.2, verdict, 'fixe' if role == 'sujet' else role, 's')
    if y < 50: arrow(ax, (84, y + CH + 0.5), (84, y + 17.5), 'fixe')
for i in range(8):
    text(ax, X0 + i * CW + (CW - 0.6) / 2, 10, str(i), 'fixe', 's')
save(fig, '50-050')
