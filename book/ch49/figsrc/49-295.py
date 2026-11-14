import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 22, 72, 'un groupe : 12 éléments', 'sujet', 's')
for i in range(12):
    r, c = divmod(i, 4)
    x = 8 + c * 9; y = 58 - r * 9
    sub = i < 4
    disc(ax, x, y, 3.2, 'varie' if sub else 'sujet', fill=True)
text(ax, 22, 28, '4 éléments en sous-groupe ?', 'varie', 's')
text(ax, 22, 22, '(la question)', 'varie', 's')
arrow(ax, (42, 52), (50, 52), 'varie')
text(ax, 46, 56, 'agit', 'varie', 's')
box(ax, 51, 40, 34, 26, 'autre')
text(ax, 68, 61, 'ensembles :', 'autre', 's')
text(ax, 68, 53, 'sous-groupes', 'autre', 's')
text(ax, 68, 46, 'classes latérales', 'autre', 's')
arrow(ax, (68, 38), (68, 28), 'resultat')
box(ax, 49, 12, 38, 15, 'resultat', label='preuves de Sylow', size='m')
text(ax, 68, 5, '(chapitre 50)', 'resultat', 's')
save(fig, '49-295')
