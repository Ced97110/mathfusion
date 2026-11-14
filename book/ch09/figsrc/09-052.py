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
fig, ax = canvas(58)
frac(ax, 20, 46, '3', '4', 'sujet'); frac(ax, 68, 46, '6', '8', 'sujet')
arrow(ax, (24, 49), (64, 43), 'varie'); arrow(ax, (24, 43), (64, 49), 'autre')
eq(ax, 44, 46); ax.texts[-1:] 
box(ax, 4, 8, 34, 9, 'varie', label=r'$3\times 8 = 24$'); box(ax, 50, 8, 34, 9, 'autre', label=r'$4\times 6 = 24$')
eq(ax, 44, 12.5, 'resultat'); text(ax, 44, 20, 'produits égaux', 'resultat', 's')
save(fig, '09-052')
