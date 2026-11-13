import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
rows = [(40, 'racines distinctes', 'sujet', '3', 'resultat', '6'),
        (12, 'racine répétée au 1er étage', 'varie', '1', 'varie', '2')]
for y, title, role, a, rrole, res in rows:
    text(ax, 44, y + 17, title, role, 's')
    box(ax, 2, y, 26, 11, role, label=a + ' choix')
    text(ax, 33, y + 5.5, r'$\times$', 'encre', 'l')
    box(ax, 38, y, 26, 11, 'fixe', label='2 choix')
    text(ax, 69, y + 5.5, '=', 'encre', 'l')
    box(ax, 74, y, 12, 11, rrole, label=res)
save(fig, '62-072')
