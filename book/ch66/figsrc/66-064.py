import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
xs = [4, 33, 62]
top = [r'$2^2$', r'$3$', r'$5$']
calc = [r'$2^{2-1}=2$', r'$3^{0}\times 2=2$', r'$5^{0}\times 4=4$']
res = ['2', '2', '4']
roles = ['sujet', 'autre', 'autre']
for x, a, c, r, ro in zip(xs, top, calc, res, roles):
    box(ax, x, 60, 22, 10, ro, label=a, size='l')
    arrow(ax, (x + 11, 60), (x + 11, 47), 'varie')
    text(ax, x + 11, 42, c, 'varie', 's')
    arrow(ax, (x + 11, 38), (x + 11, 29), 'varie')
    box(ax, x, 18, 22, 10, 'varie', label=r, size='l')
text(ax, 29.5, 23, r'$\times$', 'encre', 'l')
text(ax, 58.5, 23, r'$\times$', 'encre', 'l')
box(ax, 22, 2, 44, 10, 'resultat', label=r'$\varphi(60)=16$', size='l')
arrow(ax, (44, 18), (44, 12.2), 'varie')
save(fig, '66-064')
