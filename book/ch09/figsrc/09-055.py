import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, n, d, role='sujet', hw=4.5, size='l', nrole=None):
    text(ax, x, y + 3.8, n, nrole or role, size); text(ax, x, y - 3.8, d, role, size)
    line(ax, [(x - hw, y), (x + hw, y)], role, lw=1.0)
def eq(ax, x, y, role='encre', w=3.0):
    line(ax, [(x - w, y + 1), (x + w, y + 1)], role, lw=1.0); line(ax, [(x - w, y - 1), (x + w, y - 1)], role, lw=1.0)
def ne(ax, x, y, role='limite', w=3.0):
    eq(ax, x, y, role, w); line(ax, [(x - 1.2, y - 3), (x + 1.2, y + 3)], role, lw=1.0)
def times(ax, x, y, role='encre', a=1.3):
    line(ax, [(x - a, y - a), (x + a, y + a)], role, lw=1.0); line(ax, [(x - a, y + a), (x + a, y - a)], role, lw=1.0)
fig, ax = canvas(64)
def row(y, n, d, cut_den, mult, kept, res, nrole):
    frac(ax, 12, y, n, d, 'sujet')
    text(ax, 28, y, mult[0], 'varie', 'l'); text(ax, 42, y, mult[1], 'varie', 'l')
    return
y1, y2 = 48, 18
frac(ax, 12, y1, '3', '4', 'sujet'); text(ax, 27, y1, r'$\times\,4$', 'fixe', 'l'); text(ax, 41, y1, r'$\times\,8$', 'varie', 'l')
line(ax, [(9.8, y1 - 6.5), (14.2, y1 - 1.5)], 'varie'); line(ax, [(23.5, y1 - 1.8), (30.5, y1 + 1.8)], 'varie')
arrow(ax, (50, y1), (60, y1), 'varie'); text(ax, 73, y1, r'$3\times 8$', 'resultat', 'l')
frac(ax, 12, y2, '6', '8', 'sujet'); text(ax, 27, y2, r'$\times\,4$', 'varie', 'l'); text(ax, 41, y2, r'$\times\,8$', 'fixe', 'l')
line(ax, [(9.8, y2 - 6.5), (14.2, y2 - 1.5)], 'varie'); line(ax, [(37.5, y2 - 1.8), (44.5, y2 + 1.8)], 'varie')
arrow(ax, (50, y2), (60, y2), 'varie'); text(ax, 73, y2, r'$6\times 4$', 'resultat', 'l')
text(ax, 44, 59, 'on multiplie par 4 × 8', 'varie', 's'); text(ax, 44, 33, 'le trait barre ce qui se simplifie', 'varie', 's')
save(fig, '09-055')
