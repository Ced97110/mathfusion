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
fig, ax = canvas(66)
text(ax, 44, 59, r'$x = \frac{80}{16} = 5$', 'resultat', 'xl')
arrow(ax, (44, 52), (44, 44), 'varie'); text(ax, 48, 48, 'remplacer x par 5', 'varie', 's', ha='left')
frac(ax, 22, 36, '5', '4', 'sujet', nrole='resultat'); eq(ax, 44, 36); frac(ax, 66, 36, '20', '16', 'sujet', hw=6)
arrow(ax, (44, 27), (44, 22), 'varie')
box(ax, 4, 8, 34, 9, 'varie', label=r'$5\times 16 = 80$'); box(ax, 50, 8, 34, 9, 'autre', label=r'$4\times 20 = 80$')
eq(ax, 44, 12.5, 'resultat')
save(fig, '09-061')
