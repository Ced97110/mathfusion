import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
rows = [(r'$x+y=5$', r'$y=5-x$', 'isoler', 'sujet', 'sujet'),
        (r'$2x+y=8$', r'$2x+(5-x)=8$', 'remplacer y', 'autre', 'autre'),
        (r'$2x+(5-x)=8$', r'$x=3$', 'résoudre', 'autre', 'resultat'),
        (r'$y=5-x$', r'$y=2$', 'avec x = 3', 'sujet', 'resultat')]
for i, (a, b, lab, r1, r2) in enumerate(rows):
    yb = 84 - i * 24
    box(ax, 2, yb, 32, 11, r1, label=a); box(ax, 54, yb, 32, 11, r2, label=b)
    arrow(ax, (34, yb + 5.5), (54, yb + 5.5), 'varie'); text(ax, 44, yb + 9, lab, 'varie', 's')
text(ax, 44, 4, r'$3+2=5$ et $2\times3+2=8$', 'resultat', 's')
save(fig, '24-037')
