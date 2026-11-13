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
frac(ax, 22, 32, '3', '4', 'sujet'); frac(ax, 66, 32, '6', '8', 'autre'); eq(ax, 44, 32)
text(ax, 22, 45, 'premier rapport', 'sujet', 's'); text(ax, 66, 45, 'second rapport', 'autre', 's')
brace(ax, 16, 28, 24, 'sujet', label='3 est à 4'); brace(ax, 60, 72, 24, 'autre', label='6 est à 8')
line(ax, [(44, 29), (44, 22)], 'varie'); text(ax, 44, 19.5, 'comme', 'varie', 's')
save(fig, '09-049')
