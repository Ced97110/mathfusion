import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def plus(x, y): line(ax, [(x - 1.6, y), (x + 1.6, y)], 'encre', 1.0); line(ax, [(x, y - 1.6), (x, y + 1.6)], 'encre', 1.0)
def eq(x, y): line(ax, [(x - 1.6, y + 0.9), (x + 1.6, y + 0.9)], 'encre', 1.0); line(ax, [(x - 1.6, y - 0.9), (x + 1.6, y - 0.9)], 'encre', 1.0)
def chips(y, a, b, c, ra, rb, rc, note=None):
    xs = [20, 44, 68]
    for x, v, r in zip([20, 44, 68], [a, b, c], [ra, rb, rc]):
        pass
    disc(ax, 14, y, 5, ra, label=a, size='m'); plus(26, y); disc(ax, 38, y, 5, rb, label=b, size='m')
    eq(51, y); disc(ax, 64, y, 5, rc, label=c, size='m')
    if note: text(ax, 78, y, note, 'fixe', 's')
text(ax, 44, 66, 'heures de $\\mathbb{Z}/12\\mathbb{Z}$'.replace('\\\\', '\\'), 'encre', 's') if False else text(ax, 44, 66, r'heures de $\mathbb{Z}/12\mathbb{Z}$', 'encre', 's')
chips(54, '4', '5', '9', 'varie', 'resultat', 'sujet')
chips(36, '7', '11', '6', 'varie', 'resultat', 'sujet', note='(18)')
text(ax, 44, 22, r'couleurs : $\mathbb{Z}/3\mathbb{Z}$', 'encre', 's')
chips(10, '1', '2', '0', 'varie', 'resultat', 'sujet')
save(fig, '48-175')
