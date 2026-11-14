import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cx = [56, 76]
text(ax, cx[0], 62, 'exposant de 2', 'fixe', 's')
text(ax, cx[1], 62, 'exposant de 3', 'fixe', 's')
rows = [(46, '$12$', ['2', '1'], 'sujet', 'sujet'), (33, '$18$', ['1', '2'], 'sujet', 'sujet'),
        (16, 'PGCD $=6$ (min)', ['1', '1'], 'resultat', 'resultat'),
        (3, 'PPCM $=36$ (max)', ['2', '2'], 'autre', 'autre')]
for y, name, vals, role, lrole in rows:
    text(ax, 3, y + 5, name, lrole, 'm', ha='left')
    for x, v in zip(cx, vals):
        box(ax, x - 8, y, 16, 10, role, label=f'${v}$', size='l')
line(ax, [(3, 28), (85, 28)], 'fixe', dash=True)
save(fig, '56-080')
