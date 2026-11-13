import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
ideals = ['(48)', '(24)', '(12)', '(6)', '(3)', '(3)', '(3)', '(3)']
xs = [2.75 + 10.5 * i for i in range(8)]
for i, (x, d) in enumerate(zip(xs, ideals)):
    box(ax, x, 30, 9, 14, 'varie' if i < 4 else 'resultat', label=rf'$I_{i + 1}$' + '\n' + d, size='s')
brace(ax, xs[0], xs[3] + 9, 46, 'varie', label='ça change', down=False)
brace(ax, xs[4], xs[7] + 9, 28, 'resultat', label=r'$n \geq N$ : $I_n$ ne change plus')
cx = xs[4] + 4.5
text(ax, cx, 62, r'$N = 5$', 'sujet', 'm')
arrow(ax, (cx, 59), (cx, 45), 'sujet')
save(fig, '56-106')
