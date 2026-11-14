import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# f = x^3 - 3x + 2 ; f' = 3x^2 - 3 ; f = (x/3) f' + (-2x + 2) ; f' = (-3/2)(x+1)(-2x+2) + 0
xs = [2, 30, 60]; w = [24, 24, 26]
def row(y, a, b, c, ra, rb, rc):
    box(ax, 2, y, 24, 10, ra, label=a)
    text(ax, 28, y + 5, '÷', 'encre', 'l')
    box(ax, 31, y, 24, 10, rb, label=b)
    arrow(ax, (56.5, y + 5), (60, y + 5), 'varie')
    box(ax, 61, y, 25, 10, rc, label=c)
row(48, r'$x^3-3x+2$', r'$3x^2-3$', r'reste $-2x+2$', 'sujet', 'autre', 'varie')
row(28, r'$3x^2-3$', r'$-2x+2$', r'reste $0$', 'autre', 'varie', 'resultat')
arrow(ax, (43, 48), (14, 38.5), 'fixe', curve=0.0)
arrow(ax, (73.5, 48), (43, 38.5), 'fixe', curve=0.0)
arrow(ax, (43, 28), (43, 17), 'resultat')
box(ax, 18, 4, 50, 12, 'resultat', label=r'PGCD $=x-1\neq1$')
text(ax, 44, 61, 'divisions de coefficients', 'fixe', 's')
save(fig, '62-101')
