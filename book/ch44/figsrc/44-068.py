import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = [('fixe', 'monoïde', True, True), ('sujet', 'semi-groupe', True, False), ('fixe', 'soustraction', False, False)]
xs = [42, 58, 75]
box(ax, 47.5, 8, 21, 50, 'sujet', fill=True, lw=1.4)
for x, (role, nm, a, b) in zip(xs, cols):
    text(ax, x, 53, nm, role, 's', weight='bold' if role == 'sujet' else 'normal')
    for j, v in enumerate((a, b)):
        text(ax, x, 38 - j * 14, '✓' if v else '✗', 'resultat' if v else 'limite', 'xl')
text(ax, 2, 38, 'parenthèses', 'fixe', 's', ha='left'); text(ax, 2, 34, 'sans effet', 'fixe', 's', ha='left')
text(ax, 2, 24, 'un neutre', 'fixe', 's', ha='left')
text(ax, 58, 4, '1, 2, 3… avec +', 'sujet', 's')
save(fig, '44-068')
