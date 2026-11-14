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
fig, ax = canvas(72)
frac(ax, 22, 64, '3', '4', 'sujet'); frac(ax, 66, 64, '6', '8', 'sujet'); eq(ax, 44, 64)
arrow(ax, (22, 55), (22, 45), 'varie'); arrow(ax, (66, 55), (66, 45), 'varie')
text(ax, 44, 50, r'$\times\,(4\times 8)$', 'varie', 's')
box(ax, 3, 31, 39, 12, 'varie', label=r'$\frac{3}{4}\times 32 = 24$'); box(ax, 46, 31, 39, 12, 'varie', label=r'$\frac{6}{8}\times 32 = 24$')
arrow(ax, (44, 29), (44, 20), 'varie'); text(ax, 62, 24.5, 'simplifier', 'varie', 's')
box(ax, 14, 6, 60, 12, 'resultat', label=r'$3\times 8 = 6\times 4$')
save(fig, '09-054')
