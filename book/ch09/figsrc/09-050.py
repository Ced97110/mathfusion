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
fig, ax = canvas(50)
frac(ax, 20, 28, '3', '4', 'sujet'); frac(ax, 62, 28, '6', '8', 'autre'); eq(ax, 41, 28)
arrow(ax, (25, 35), (57, 35), 'varie', curve=-0.3); text(ax, 41, 43.5, r'$\times 2$', 'varie', 'm')
arrow(ax, (25, 21), (57, 21), 'varie', curve=0.3); text(ax, 41, 13, r'$\times 2$', 'varie', 'm')
text(ax, 20, 11, '0,75', 'resultat', 'm'); text(ax, 62, 11, '0,75', 'resultat', 'm')
save(fig, '09-050')
