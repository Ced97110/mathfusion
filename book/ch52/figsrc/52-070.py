import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def row(y, a, op, b, r, note, ra):
    box(ax, 3, y, 18, 12, ra, label=a, size='l'); text(ax, 28, y + 6, op, 'encre', 'l')
    box(ax, 35, y, 18, 12, 'fixe', label=b, size='l'); text(ax, 60, y + 6, '=', 'encre', 'l')
    box(ax, 67, y, 18, 12, 'resultat', label=r, size='l')
    text(ax, 44, y - 4.5, note, ra, 's')
row(40, r'$\bar{0}$', '+', r'$\bar{3}$', r'$\bar{3}$', 'zéro : ne change rien', 'sujet')
row(12, r'$\bar{1}$', r'$\times$', r'$\bar{3}$', r'$\bar{3}$', 'unité : ne change rien', 'sujet')
text(ax, 44, 61, r'$\bar{0}=0+I=I$ : multiples de 4', 'sujet', 's')
save(fig, '52-070')
