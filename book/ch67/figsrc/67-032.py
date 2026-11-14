import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
A = r'$\alpha$'
for x in (4, 26, 48):
    box(ax, x, 22, 14, 10, 'fixe', label=A)
for x in (22, 44):
    text(ax, x, 27, '+', 'encre', 'l')
text(ax, 67, 27, '=', 'encre', 'l')
box(ax, 72, 22, 14, 10, 'sujet', label=r'$3\alpha$')
brace(ax, 4, 62, 20, 'varie', label='3 termes')
text(ax, 44, 41, r'$n\alpha$ : somme de $n$ termes', 'sujet', 'm')
text(ax, 44, 6, r'ici $n=3$ : trois termes égaux à $\alpha$', 'varie', 's')
save(fig, '67-032')
