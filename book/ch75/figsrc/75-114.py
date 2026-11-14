import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def mat(x, y, a, role):
    box(ax, x, y, 18, 14, role)
    text(ax, x + 9, y + 7, f'{a}  0\n0  1', role, 'l')
text(ax, 20, 56, r'$GL_{2}(\mathbb{F}_{3})$', 'sujet', 'm')
text(ax, 72, 56, r'$\mathbb{F}_{3}^{*}$', 'resultat', 'm')
mat(10, 33, 1, 'resultat'); mat(10, 10, 2, 'sujet')
disc(ax, 72, 40, 5, 'resultat', label='1', size='l'); disc(ax, 72, 17, 5, 'sujet', label='2', size='l')
arrow(ax, (30, 40), (66, 40), 'varie'); arrow(ax, (30, 17), (66, 17), 'varie')
text(ax, 48, 43.5, 'det', 'varie', 's'); text(ax, 48, 20.5, 'det', 'varie', 's')
text(ax, 20, 50, 'noyau : det = 1', 'resultat', 's')
save(fig, '75-114')
