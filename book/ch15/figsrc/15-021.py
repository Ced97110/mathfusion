import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
labs = [r'$3x^4$', r'$6x^2$', r'$5x$', r'$8$']
for i, s in enumerate(labs):
    x = 5 + i * 21
    box(ax, x, 26, 15, 11, 'sujet', label=s)
    text(ax, x + 7.5, 20, f'{i+1}', 'sujet', 'm')
    if i < 3: text(ax, x + 18, 31.5, '+', 'varie', 'l')
brace(ax, 5, 83, 15, 'resultat', 'quatre termes', size='m')
text(ax, 44, 46, 'quatre morceaux', 'fixe', 's')
save(fig, '15-021')
