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
fig, ax = canvas(52)
x0, bw = 30, 54
text(ax, 57, 46, 'total convenu : 100', 'resultat', 's')
box(ax, x0, 31, bw, 8, 'resultat', fill=False); box(ax, x0, 31, bw * 0.15, 8, 'varie')
text(ax, 2, 35, '15 pour 100', 'sujet', 's', ha='left')
text(ax, 57, 24, 'autre total possible : 1 000', 'fixe', 's')
box(ax, x0, 9, bw, 8, 'fixe', fill=False); box(ax, x0, 9, bw * 0.15, 8, 'varie')
text(ax, 2, 13, '150 pour 1 000', 'sujet', 's', ha='left')
save(fig, '09-064')
