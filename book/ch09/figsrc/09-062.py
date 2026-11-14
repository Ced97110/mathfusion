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
fig, ax = canvas(60)
steps = [('écrire avec une lettre', r'$\frac{x}{4}=\frac{20}{16}$', 'sujet'), ('produit en croix', r'$16\times x = 4\times 20$', 'varie'),
         ('diviser', r'$x = 80\div 16 = 5$', 'varie'), ('vérifier', r'$5\times 16 = 4\times 20$', 'resultat')]
for i, (n, f, r) in enumerate(steps):
    y = 51 - 13 * i
    box(ax, 14, y - 5.5, 72, 11, r, fill=True)
    disc(ax, 7, y, 3.6, r, label=str(i + 1), size='m')
    text(ax, 17, y, n, r, 's', ha='left'); text(ax, 83, y, f, r, 's', ha='right')
    if i < 3: arrow(ax, (7, y - 4), (7, y - 8.7), 'fixe')
save(fig, '09-062')
