import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 17, 65, 'congruence', 'varie', 's'); text(ax, 68, 65, 'sous-groupe', 'sujet', 's')
text(ax, 42, 65, 'un pour un', 'resultat', 's')
def row(y, lab, role, vals):
    box(ax, 3, y - 9, 28, 18, 'varie', label=lab, size='s')
    arrow(ax, (32.5, y), (49.5, y), 'resultat', both=True, lw=1.4)
    box(ax, 51, y - 9, 34, 18, role)
    text(ax, 68, y, vals, role, 's')
row(52, 'même reste\nmodulo 3', 'sujet', r'$\{0,\,3,\,6,\,9,\,\ldots\}$')
row(18, 'même reste\nmodulo 5', 'autre', r'$\{0,\,5,\,10,\,15,\,\ldots\}$')
text(ax, 17, 35, r'$\neq$', 'limite', 'l'); text(ax, 68, 35, r'$\neq$', 'limite', 'l')
save(fig, '47-140')
