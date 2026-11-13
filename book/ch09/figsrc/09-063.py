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
box(ax, 3, 33, 82, 9, 'sujet'); box(ax, 3, 16, 82, 9, 'autre')
text(ax, 20, 37.5, '30 miles', 'sujet', 'm'); text(ax, 68, 37.5, '? miles', 'sujet', 'm')
text(ax, 20, 20.5, '2 gallons', 'autre', 'm'); text(ax, 68, 20.5, '5 gallons', 'autre', 'm')
line(ax, [(8, 29), (32, 29)], 'encre', lw=1.0); line(ax, [(56, 29), (80, 29)], 'encre', lw=1.0); eq(ax, 44, 29)
text(ax, 44, 8, 'même unité au même étage', 'resultat', 'm')
save(fig, '09-063')
