import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, 'fini : on finit de compter', 'sujet', 's')
labs = ['rien', 'échange', 'tout sur 1', 'tout sur 2']
for i, l in enumerate(labs):
    box(ax, 3 + i * 21, 46, 19, 12, 'sujet', label=str(i + 1), size='m')
    text(ax, 12.5 + i * 21, 41, l, 'sujet', 's')
brace(ax, 3, 82, 36, 'sujet', '4 éléments', down=True)
text(ax, 44, 28, 'infini : jamais fini', 'autre', 's')
f = numberline(ax, 6, 56, 14, 0, 5, 1, role='autre')
text(ax, 77, 14, '…', 'autre', 'l')
save(fig, '44-088')
