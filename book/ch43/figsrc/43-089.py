import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
groups = [(1, [1, 4]), (2, [2, 5]), (0, [3, 6])]; xs = [16, 44, 72]
for (c, els), x in zip(groups, xs):
    box(ax, x - 12, 20, 24, 24, 'sujet')
    for k, n in enumerate(els): disc(ax, x - 5.5 + k * 11, 32, 3.4, 'sujet', label=str(n))
    text(ax, x, 49, r'$f^{-1}(%d)$' % c, 'sujet', 'm')
    text(ax, x, 14, r'$\bar{%d}$' % els[0], 'autre', 'l')
text(ax, 44, 57, 'fibres non vides', 'sujet', 's')
text(ax, 44, 6, 'blocs de ' + r'$S/E_f$' + ' : mêmes ensembles', 'autre', 's')
save(fig, '43-089')
