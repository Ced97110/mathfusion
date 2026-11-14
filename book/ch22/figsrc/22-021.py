import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [(8, 'sujet', r'$d$', 'le côté'), (36, 'varie', r'$\approx$', 'environ égal à'), (60, 'fixe', '1,414', 'valeur proche')]
for x, r, lab, expl in xs:
    wd = 20 if lab != '1,414' else 22
    box(ax, x, 36, wd, 14, r, label=lab, size='l')
    arrow(ax, (x + wd / 2, 36), (x + wd / 2, 29), r)
    text(ax, x + wd / 2, 25, expl, r, 's')
box(ax, 8, 4, 28, 10, 'limite', label=r'$d = 1{,}414$', size='m')
text(ax, 60, 11.5, 'faux :', 'limite', 's')
text(ax, 60, 6.5, r'$1{,}414^2 \neq 2$', 'limite', 's')
save(fig, '22-021')
