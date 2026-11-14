import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, '« tous les premiers sont impairs »', 'sujet', 'm')
xs = [3, 5, 7, 11, 13]
for i, v in enumerate(xs):
    disc(ax, 12 + i * 11, 40, 4.2, 'resultat', label=str(v), size='m')
text(ax, 39, 31, '5 essais : tous réussissent', 'resultat', 's')
disc(ax, 74, 40, 4.2, 'limite', label='2', size='m')
text(ax, 74, 31, '2 : pair', 'limite', 's')
box(ax, 4, 6, 80, 13, 'fixe', dash=True, label='des essais ne prouvent rien', size='m')
save(fig, '42-085')
