import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def bin_(x, wd, head, items):
    box(ax, x, 12, wd, 36, 'fixe', dash=True, fill=False)
    text(ax, x + wd / 2, 42, head, 'varie', 'xl', weight='bold')
    for i, (n, sci) in enumerate(items):
        xx = x + 3 + 25 * i
        box(ax, xx, 24, 22, 9, 'sujet', label=n, size='m')
        text(ax, xx + 11, 19, sci, 'sujet', 's')
bin_(3, 53, r'$10^3$', [('4 316', r'$4{,}316\times10^3$'), ('1 200', r'$1{,}2\times10^3$')])
bin_(60, 25, r'$10^4$', [('52 000', r'$5{,}2\times10^4$')])
text(ax, 29.5, 7, 'même ordre de grandeur', 'varie', 's'); text(ax, 72.5, 7, 'ordre suivant', 'varie', 's')
save(fig, '10-093')
