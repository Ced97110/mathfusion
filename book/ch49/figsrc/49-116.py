import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
parts = [(r'$g$', 'varie', 'élément g'), (r'$x$', 'sujet', 'élément x'), (r'$g^{-1}$', 'varie', 'inverse de g')]
xs = [16, 44, 72]
for (s, role, lab), x in zip(parts, xs):
    box(ax, x - 11, 38, 22, 14, role, label=s, size='l')
    text(ax, x, 33, lab, role, 's')
arrow(ax, (44, 27), (44, 19), 'encre')
text(ax, 62, 23, 's’écrit', 'encre', 's')
text(ax, 44, 9, r'${}^{g}x$', 'resultat', 'xl')
text(ax, 74, 9, 'x conjugué par g', 'resultat', 's')
save(fig, '49-116')
