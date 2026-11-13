import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# η ↦ A : une application, un tableau, et la somme se fait colonne par colonne
box(ax, 2, 46, 32, 14, 'sujet', label='application η', size='m')
box(ax, 54, 46, 32, 14, 'autre', label='tableau A', size='m')
arrow(ax, (35, 55), (53, 55), 'resultat', lw=1.3, both=True)
text(ax, 44, 50, 'bijection', 'resultat', 's', weight='bold')
text(ax, 44, 39, 'et la somme est respectée :', 'encre', 's')
# colonnes de deux applications et de leur somme
def tab(x, c1, c2, role):
    box(ax, x, 18, 11, 9, role, label=c1, size='s', r=0.5)
    box(ax, x + 12, 18, 11, 9, role, label=c2, size='s', r=0.5)
tab(2, '(2, 1)', '(1, 3)', 'sujet')
text(ax, 28.5, 22.5, '+', 'encre', 'm')
tab(32, '(1, 0)', '(0, 1)', 'autre')
text(ax, 58.5, 22.5, '=', 'encre', 'm')
tab(62, '(3, 1)', '(1, 4)', 'resultat')
text(ax, 44, 8, 'colonne par colonne', 'varie', 's')
save(fig, '58-208')
