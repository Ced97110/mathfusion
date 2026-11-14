import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
els = ['0', '1', r'$\alpha$', r'$\alpha+1$']
xs = [22, 38, 54, 70]
text(ax, 10, 51, 'élément', 'encre', 's')
text(ax, 10, 35, r'$x+x$', 'encre', 's')
for x, s in zip(xs, els):
    box(ax, x, 46, 14, 10, 'sujet', label=s)
    box(ax, x, 30, 14, 10, 'resultat', label='0')
    arrow(ax, (x + 7, 46), (x + 7, 40.5), 'varie')
text(ax, 53, 23, '2 termes annulent tout : p = 2', 'resultat', 's')
box(ax, 22, 6, 62, 10, 'limite', label=r'un seul terme : $1\neq0$', size='s')
save(fig, '67-035')
