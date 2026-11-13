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
fig, ax = canvas(68)
text(ax, 22, 62, '6', 'sujet', 'xl'); text(ax, 66, 62, '6', 'sujet', 'xl'); eq(ax, 44, 62)
arrow(ax, (22, 57), (22, 43), 'varie'); arrow(ax, (66, 57), (66, 43), 'varie'); text(ax, 44, 50, r'$\times 2$ des deux côtés', 'varie', 's')
text(ax, 22, 38, '12', 'resultat', 'xl'); text(ax, 66, 38, '12', 'resultat', 'xl'); eq(ax, 44, 38, 'resultat')
line(ax, [(4, 30), (84, 30)], 'fixe', dash=True)
text(ax, 22, 24, '6', 'sujet', 'xl'); text(ax, 66, 24, '6', 'sujet', 'xl'); eq(ax, 44, 24)
arrow(ax, (22, 19), (22, 11), 'varie'); arrow(ax, (66, 19), (66, 11), 'limite')
text(ax, 31, 15, r'$\times 2$', 'varie', 's'); text(ax, 75, 15, r'$\times 3$', 'limite', 's')
text(ax, 22, 6, '12', 'varie', 'xl'); text(ax, 66, 6, '18', 'limite', 'xl'); ne(ax, 44, 6)
save(fig, '09-053')
