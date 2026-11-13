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

zone_haut('resultat'); zone_bas('limite'); frame(); droite()
pts = [(-1, 'faux', 'limite'), (0, 'faux', 'limite'), (1, 'faux : 1 = 1', 'limite'), (1.5, 'vrai', 'resultat'), (3, 'vrai', 'resultat')]
for (b, lab, r) in pts:
    x, y = P(0, b)
    line(ax, [(x, y), (54, y)], 'fixe', lw=0.5, dash=True)
    disc(ax, x, y, 1.2, r)
    text(ax, 56, y, f'(0, {str(b).replace("-", "−").replace(".", ",")}) {lab}', r, 's', ha='left')
text(ax, *P(-1.9, 4.2), 'haut : vrai', 'resultat', 's', ha='left')
text(ax, *P(1.0, -0.5), 'bas : faux', 'limite', 's', ha='left')
save(fig, '20-020')
