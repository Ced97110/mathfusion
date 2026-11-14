import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = ['1. discriminant : 1 + 4 = 5', '2. racines : (−1 ± √5)/2', '3. on garde + car c > 0', '4. c = y ÷ 2 = (√5 − 1)/4']
roles = ['fixe', 'fixe', 'resultat', 'sujet']
for i, (t, r) in enumerate(zip(rows, roles)):
    text(ax, 3, 58 - 6 * i, t, r, 'm', ha='left')
f = numberline(ax, 10, 76, 20, -2, 1, 1, arrow_right=False)
xm, xy, xc = f(-1.618), f(0.618), f(0.309)
disc(ax, xm, 20, 1.3, 'limite')
disc(ax, xy, 20, 1.3, 'resultat')
disc(ax, xc, 20, 1.3, 'sujet')
text(ax, xm, 26, '−1,618', 'limite', 's')
text(ax, 55, 30, 'c ≈ 0,309', 'sujet', 's')
text(ax, 72, 30, 'y ≈ 0,618', 'resultat', 's')
arrow(ax, (xy - 1, 23.5), (xc + 1, 23.5), 'varie')
text(ax, (xy + xc) / 2, 26.8, '÷ 2', 'varie', 's')
save(fig, '66-094')
