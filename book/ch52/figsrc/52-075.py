import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
for y, rep, name in ((52, 7, r'$7+I$'), (24, 3, r'$3+I$')):
    f = numberline(ax, 22, 76, y, -1, 11, step=4, arrow_right=False)
    text(ax, 8, y, name, 'sujet', 'm')
    for v in (-1, 3, 7, 11):
        disc(ax, f(v), y, 1.8, 'varie' if v == rep else 'sujet')
text(ax, 44, 38, '=', 'resultat', 'xl')
text(ax, 44, 66, 'mêmes éléments', 'resultat', 's')
text(ax, 44, 7, r'7 − 3 = 4 $\in I$ : même classe', 'resultat', 's')
save(fig, '52-075')
