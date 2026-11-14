import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
s, x0, y0 = 44, 3, 6
C = lambda u, v: (x0 + u*s, y0 + v*s)
text(ax, x0 + s/2, 53, '8 traits dans le carreau', 'encre', 'm')
H_ = [((0,0),(1,0)), ((0,.5),(1,.5)), ((0,1),(1,1))]
V_ = [((0,0),(0,1)), ((.5,0),(.5,1)), ((1,0),(1,1))]
for grp, role in [(H_, 'sujet'), (V_, 'varie'), ([((0,0),(1,1))], 'resultat'), ([((0,1),(1,0))], 'autre')]:
    for a, b in grp: line(ax, [C(*a), C(*b)], role, lw=1.4)
lx = 53
for k, (lab, role) in enumerate([('horizontale : 3', 'sujet'), ('verticale : 3', 'varie'), ('diagonale : 1', 'resultat'), ('diagonale : 1', 'autre')]):
    y = 40 - k*8.5
    line(ax, [(lx, y), (lx+6, y)], role, lw=1.4)
    text(ax, lx+8, y, lab, role, 's', ha='left')
text(ax, 70, 6, '4 directions', 'encre', 'm')
save(fig, '74-169')
