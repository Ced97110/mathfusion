import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 55, r'non $a = 1 + a$', 'sujet', 'l')
for y, a, ra, b, rb, lab in ((30, '1 : vrai', 'resultat', '0 : faux', 'limite', r'$1 + 1 = 0$'),
                             (8, '0 : faux', 'limite', '1 : vrai', 'resultat', r'$1 + 0 = 1$')):
    box(ax, 4, y, 22, 12, ra, label=a); box(ax, 62, y, 22, 12, rb, label=b)
    arrow(ax, (26, y + 6), (62, y + 6), 'varie'); text(ax, 44, y + 10.5, lab, 'varie', 's')
save(fig, '80-327')
