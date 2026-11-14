import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 4, 46, 34, 10, 'sujet', label='groupe abélien')
text(ax, 44, 51, '=', 'encre', 'l')
box(ax, 50, 46, 34, 10, 'sujet', label=r'$\mathbb{Z}$-module')
xs = [4, 26, 48]
for x in xs:
    box(ax, x, 22, 14, 10, 'sujet', label=r'$g$', size='l')
text(ax, 21, 27, '+', 'encre', 'l')
text(ax, 43, 27, '+', 'encre', 'l')
brace(ax, 4, 62, 20, 'varie', label='3 fois g : addition répétée')
text(ax, 68, 27, '=', 'encre', 'l')
box(ax, 72, 22, 14, 10, 'varie', label=r'$3g$', size='l')
save(fig, '60-094')
