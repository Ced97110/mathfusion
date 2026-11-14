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
frac(ax, 11, 48, '3', '4', 'sujet'); eq(ax, 22, 48, 'resultat'); frac(ax, 33, 48, '6', '8', 'autre')
frac(ax, 55, 48, '3', '4', 'sujet'); ne(ax, 66, 48); frac(ax, 77, 48, '6', '9', 'autre')
box(ax, 5, 24, 34, 8, 'varie', label=r'$3\times 8 = 24$'); box(ax, 5, 13, 34, 8, 'autre', label=r'$4\times 6 = 24$')
box(ax, 49, 24, 34, 8, 'varie', label=r'$3\times 9 = 27$'); box(ax, 49, 13, 34, 8, 'autre', label=r'$4\times 6 = 24$')
text(ax, 22, 6, 'produits égaux : vrai', 'resultat', 's'); text(ax, 66, 6, 'produits différents : faux', 'limite', 's')
save(fig, '09-056')
