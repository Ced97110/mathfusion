import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
labs = [r'$G_1$', r'$G_2$', r'$\cdots$', r'$G_n$']
for i, l in enumerate(labs): box(ax, 3 + 20 * i, 50, 17, 10, 'fixe' if i == 2 else 'sujet', label=l)
brace(ax, 3, 80, 48, 'sujet', label=r'liste de $n$ cases')
text(ax, 44, 34, r'exemple : $n=3$ interrupteurs', 'encre', 's')
for i, v in enumerate('011'): box(ax, 21 + 16 * i, 19, 14, 10, 'sujet', label=v)
text(ax, 44, 8, r'$2\times2\times2$ = 8 états', 'resultat')
save(fig, '45-166')
