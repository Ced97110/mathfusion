import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 30, 48, 28, 10, 'sujet', label=r'$n=60$', size='l')
xs = [8, 33, 58]
facs = [(r'$2^2$', 'sujet', 'puissance de 2', r'$e=2$'), (r'$3$', 'autre', 'premier impair', r'$p_2=3$'),
        (r'$5$', 'autre', 'premier impair', r'$p_3=5$')]
for x, (lab, role, nom, sym) in zip(xs, facs):
    box(ax, x, 22, 22, 11, role, label=lab, size='l')
    arrow(ax, (44, 48), (x + 11, 33.5), 'varie')
    text(ax, x + 11, 15.5, nom, role, 's')
    text(ax, x + 11, 9, sym, role, 's')
text(ax, 31, 27.5, r'$\times$', 'encre', 'l')
text(ax, 56, 27.5, r'$\times$', 'encre', 'l')
text(ax, 44, 2, r'$60=2^2\times 3\times 5$', 'encre', 'm')
save(fig, '66-063')
