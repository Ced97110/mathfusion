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
def form(y, labs, roles, nums):
    xs = [3, 26, 49, 72]
    for i in range(4):
        box(ax, xs[i], y - 5, 14, 10, roles[i], label=labs[i], size='s' if nums is None else 'l')
    times(ax, 21.5, y); eq(ax, 44.5, y); times(ax, 67.5, y)
form(46, ['nombre', 'lettre', 'nombre', 'nombre'], ['sujet', 'varie', 'sujet', 'sujet'], None)
line(ax, [(4, 36), (84, 36)], 'fixe', dash=True)
form(26, ['16', 'x', '4', '20'], ['sujet', 'varie', 'sujet', 'sujet'], 1)
form(9, ['3', '8', '6', 'x'], ['sujet', 'sujet', 'sujet', 'varie'], 1)
save(fig, '09-059')
