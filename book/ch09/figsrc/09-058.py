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
frac(ax, 22, 62, 'x', '4', 'sujet', nrole='varie', hw=5); eq(ax, 44, 62); frac(ax, 66, 62, '20', '16', 'sujet', hw=6)
arrow(ax, (44, 53), (44, 46), 'varie'); text(ax, 48, 49.5, 'produit en croix', 'varie', 's', ha='left')
text(ax, 44, 40, r'$16\times x = 4\times 20 = 80$', 'sujet', 'l')
arrow(ax, (44, 34), (44, 27), 'varie'); text(ax, 48, 30.5, 'diviser par 16', 'varie', 's', ha='left')
box(ax, 14, 10, 60, 11, 'resultat', label=r'$x = 80 \div 16 = 5$', size='l')
save(fig, '09-058')
