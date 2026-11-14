import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$d=3$ : le code corrige $t=1$ erreur', 'sujet', 's')
rows = [(40, '100', '1 erreur (000 envoyé)', 1, 2, 'resultat', 'corrigé'),
        (14, '110', '2 erreurs (000 envoyé)', 2, 1, 'limite', 'se trompe')]
for y, w, head, da, db, role, verdict in rows:
    text(ax, 44, y + 11, head, 'varie', 's')
    box(ax, 2, y - 5, 20, 10, 'varie', label=f'reçu {w}')
    arrow(ax, (23, y), (27, y), 'fixe')
    chosen = 0 if da < db else 1
    box(ax, 28, y - 5, 20, 10, role if chosen == 0 else 'fixe', label=f'à 000 : {da}', size='s')
    box(ax, 50, y - 5, 20, 10, role if chosen == 1 else 'fixe', label=f'à 111 : {db}', size='s')
    text(ax, 78, y, verdict, role, 's')
save(fig, '68-081')
