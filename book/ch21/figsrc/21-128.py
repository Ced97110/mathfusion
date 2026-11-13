import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'valeur interdite : $a=4$', 'limite', 's')
cs = [20, 46, 72]
top = [r'$\frac{4a}{a-4}$', r'$2$', r'$\frac{16}{a-4}$']
bot = [r'$4a$', r'$2(a-4)$', r'$16$']
for c, t, b in zip(cs, top, bot):
    box(ax, c - 11, 36, 22, 16, 'sujet', label=t, size='m')
    arrow(ax, (c, 35), (c, 22), 'varie')
    text(ax, c - 10, 29, r'$\times(a-4)$', 'varie', 's')
    box(ax, c - 11, 8, 22, 13, 'resultat', label=b, size='m')
text(ax, 33, 44, '=', 'encre', 'm'); text(ax, 59, 44, '+', 'encre', 'm')
save(fig, '21-128')
