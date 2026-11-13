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
frac(ax, 20, 48, '3', '4', 'sujet'); eq(ax, 43, 48); frac(ax, 66, 48, 'x', '8', 'sujet', nrole='varie')
box(ax, 62.5, 49.4, 7, 5.6, 'varie', fill=False, dash=True); text(ax, 66, 62, 'inconnu noté x', 'varie', 's')
arrow(ax, (44, 36), (44, 27), 'varie'); text(ax, 48, 31.5, 'remplacer x par 6', 'varie', 's', ha='left')
frac(ax, 20, 16, '3', '4', 'sujet'); eq(ax, 43, 16, 'resultat'); frac(ax, 66, 16, '6', '8', 'sujet', nrole='resultat')
save(fig, '09-057')
