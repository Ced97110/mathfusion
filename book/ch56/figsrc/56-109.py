import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ideals = ['(48)', '(24)', '(12)', '(6)', '(3)', '(3)', '(3)']
xs = [3 + 12 * i for i in range(7)]
box(ax, 3, 52, 82, 9, 'resultat', label=r'$I$ = réunion = ($d$) = (3)', size='m')
for i, (x, d) in enumerate(zip(xs, ideals)):
    box(ax, x, 24, 10, 12, 'varie' if i < 4 else 'resultat', label=rf'$I_{i + 1}$' + '\n' + d, size='s')
cx = xs[4] + 5
arrow(ax, (cx, 52), (cx, 37), 'sujet')
text(ax, 73, 44, r'$d$ apparaît au rang $N$', 'sujet', 's')
brace(ax, xs[4], xs[6] + 10, 22, 'resultat', label=r'$n \geq N$ : $I_n = I$')
save(fig, '56-109')
