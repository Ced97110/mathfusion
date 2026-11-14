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
fig, ax = canvas(56)
cx = [16, 44, 72]
for c, t, r in zip(cx, ['facteur connu', 'facteur manquant', 'produit'], ['sujet', 'varie', 'resultat']): text(ax, c, 50, t, r, 's')
for y, (a, p) in zip([36, 23, 10], [('16', '80'), ('12', '60'), ('7', '56')]):
    box(ax, 6, y - 4.5, 20, 9, 'sujet', label=a, size='l'); box(ax, 34, y - 4.5, 20, 9, 'varie', label='?', size='l')
    box(ax, 62, y - 4.5, 20, 9, 'resultat', label=p, size='l'); times(ax, 30, y); eq(ax, 58, y)
save(fig, '09-060')
