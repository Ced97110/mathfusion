import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
items = [('2', r'$\det g$', 'varie'), ('1', r'$\det h$', 'sujet'), ('1/2', r'$\det g^{-1}$', 'varie')]
x = 3
for k, (n, nm, role) in enumerate(items):
    box(ax, x, 22, 16, 11, role, label=n, size='l'); text(ax, x+8, 18, nm, role, 's')
    if k < 2: text(ax, x+19.5, 27.5, r'$\times$', 'encre', 'l')
    x += 23
text(ax, 72, 27.5, '=', 'encre', 'l'); box(ax, 76, 22, 10, 11, 'resultat', label='1', size='l')
text(ax, 44, 46, r'$g^{-1}$, puis $h$, puis $g$', 'encre', 'm')
text(ax, 44, 9, r'reste dans $SL_n(F)$ : $\det = 1$', 'resultat', 'm')
save(fig, '73-037')
