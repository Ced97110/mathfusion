import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 12, 46, 'a', 'sujet', 'xl', weight='bold'); text(ax, 15.5, 49, 'n', 'varie', 'l', weight='bold')
text(ax, 25, 46, '=', 'encre', 'xl')
labs = ['a', 'a', '…', 'a']
for i, l in enumerate(labs):
    x = 32 + i * 14
    box(ax, x - 5, 38, 10, 10, 'sujet' if l == 'a' else 'fixe', label=l, size='l')
    if i < 3: text(ax, x + 7, 43, '×', 'fixe', 'm')
brace(ax, 27, 83, 36, 'varie', 'n facteurs a')
text(ax, 44, 15, r'$2^{4}=2\times2\times2\times2$', 'sujet', 'm')
save(fig, '14-013')
