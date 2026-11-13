import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, 'sans le 0, on lirait 156', 'fixe', 's')
for i, d in enumerate('1056'):
    box(ax, 13 + i * 16, 38, 14, 11, 'varie' if d == '0' else 'sujet', label=d, size='l')
text(ax, 13 + 16 + 7, 33, '0 centaine', 'varie', 's')
labs = [r'$2x^3$', r'$0x^2$', r'$-4x$', r'$1$']
for i, s in enumerate(labs):
    box(ax, 3 + i * 21, 12, 19, 11, 'varie' if i == 1 else 'sujet', label=s, size='m')
text(ax, 3 + 21 + 9.5, 7, 'coefficient 0 écrit', 'varie', 's')
text(ax, 44, 28, 'même idée pour un polynôme', 'fixe', 's')
save(fig, '21-116')
