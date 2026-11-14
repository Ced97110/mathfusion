import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
O = (44, 34); ux, uy = 10.5, 9
X = lambda a: O[0] + ux * a
Y = lambda b: O[1] + uy * b
for a in range(-3, 4):
    for b in range(-2, 3):
        if b != 0:
            disc(ax, X(a), Y(b), 0.9, 'sujet')
        else:
            disc(ax, X(a), Y(b), 0.9, 'limite', fill=False)
line(ax, [(X(-3.7), O[1]), (X(3.7), O[1])], 'limite', dash=True, lw=1.0)
disc(ax, X(0), Y(2), 1.3, 'resultat')
t = text(ax, X(0) + 2.6, Y(2), '(0, 2) permis', 'resultat', 's', ha='left')
t.set_bbox(dict(fc='white', ec='none', pad=0.8))
text(ax, 44, O[1] + 4.5, 'b = 0 : ligne retirée', 'limite', 's')
text(ax, 44, 5, 'b ≠ 0 : points permis', 'sujet', 's')
save(fig, '54-015')
