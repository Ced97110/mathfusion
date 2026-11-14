import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
nums = ['540', '270', '135', '45', '15', '5']
divs = ['2', '2', '3', '3', '3']
xs = [8 + 14 * i for i in range(6)]
for i, (x, n) in enumerate(zip(xs, nums)):
    text(ax, x, 36, n, 'resultat' if i == 5 else 'sujet', 'l', weight='bold')
for i, d in enumerate(divs):
    role = 'varie' if d == '2' else 'autre'
    arrow(ax, (xs[i] + 5, 36), (xs[i + 1] - 5, 36), role)
    text(ax, (xs[i] + xs[i + 1]) / 2, 41, rf'$\div{d}$', role, 's')
brace(ax, xs[0] + 5, xs[2] - 5, 30, 'varie', label=r'$2^2$')
brace(ax, xs[2] + 5, xs[5] - 5, 30, 'autre', label=r'$3^3$')
text(ax, 44, 8, r'$540=2^2\times3^3\times5$', 'encre', 'l', weight='bold')
save(fig, '60-229')
