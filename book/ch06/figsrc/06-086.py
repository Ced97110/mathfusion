import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
y1, y2 = 55, 22
f1 = numberline(ax, 8, 80, y1, 0, 1, step=1/6, labels=False, arrow_right=False)
f2 = numberline(ax, 8, 80, y2, 0, 1, step=1/12, labels=False, arrow_right=False)
text(ax, 44, 70, 'bas 6 : rien entre eux', 'limite', 's')
text(ax, 44, 40, 'bas 12 : une fraction entre eux', 'resultat', 's')
for f, y, pts in ((f1, y1, ((2/6, r'$2/6$', 'sujet'), (3/6, r'$3/6$', 'autre'))),
                  (f2, y2, ((4/12, r'$4/12$', 'sujet'), (6/12, r'$6/12$', 'autre')))):
    for v, s, r in pts:
        disc(ax, f(v), y, 1.4, r); text(ax, f(v), y + 7, s, r, 's')
disc(ax, f2(5/12), y2, 1.6, 'resultat')
text(ax, f2(5/12), 13, r'$5/12$', 'resultat', 'm')
save(fig, '06-086')
