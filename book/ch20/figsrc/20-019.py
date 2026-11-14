import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
S = 8; X0 = 5; Y0 = 6; XM = -2; YM = -1.5
P = lambda x, y: (X0 + (x - XM) * S, Y0 + (y - YM) * S)
def frame():
    line(ax, [P(-2, -1.5), P(4, -1.5), P(4, 5), P(-2, 5), P(-2, -1.5)], "fixe", lw=0.5)
    line(ax, [P(-2, 0), P(4, 0)], "fixe"); line(ax, [P(0, -1.5), P(0, 5)], "fixe")
    text(ax, *P(3.7, 0.5), "x", "fixe"); text(ax, *P(0.4, 4.6), "y", "fixe")
def zone_haut(role): poly(ax, [P(-2, -1), P(4, 5), P(-2, 5)], role)
def zone_bas(role): poly(ax, [P(-2, -1.5), P(4, -1.5), P(4, 5), P(-2, -1)], role)
def droite(): line(ax, [P(-2, -1), P(4, 5)], "sujet", lw=1.1, dash=True)

zone_haut('sujet'); zone_bas('autre'); frame(); droite()
text(ax, *P(-1.0, 3.6), 'haut', 'sujet')
text(ax, *P(2.6, -0.9), 'bas', 'autre')
for (a, b, r) in [(0, 3, 'sujet'), (0, -1, 'autre')]:
    x, y = P(a, b)
    disc(ax, x, y, 1.3, r)
    line(ax, [(x, y), (54, y)], 'fixe', lw=0.5, dash=True)
    text(ax, 56, y, f'({a}, {str(b).replace("-", "−")})', r, 'm', ha='left')
text(ax, 56, P(0, 4)[1], 'deux morceaux', 'encre', 's', ha='left')
text(ax, 56, P(0, 1)[1] + 3, 'la droite', 'sujet', 's', ha='left')
save(fig, '20-019')
