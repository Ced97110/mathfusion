import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, s, role, w=7.5, h=5.5):
    text(ax, cx, cy, s, role, "m")
    for g in (-1, 1):
        x = cx + g * w
        line(ax, [(x - g * 1.2, cy + h), (x, cy + h), (x, cy - h), (x - g * 1.2, cy - h)], role)

fig, ax = canvas(66)
y = 54
mat(ax, 14, y, '1   8\n0   1', 'sujet'); text(ax, 26, y, r'$\times$', 'encre', 'l')
mat(ax, 38, y, '1   −2\n0    1', 'varie'); text(ax, 50, y, '=', 'encre', 'l')
mat(ax, 64, y, '1   6\n0   1', 'resultat')
f = numberline(ax, 12, 72, 18, 0, 8, 1, every=2, arrow_right=False)
arrow(ax, (f(0), 21), (f(8), 21), 'sujet', curve=-0.35)
arrow(ax, (f(8), 21), (f(6), 21), 'varie', curve=0.6)
disc(ax, f(6), 18, 1.3, 'resultat')
text(ax, f(4), 36, 'pente 8', 'sujet', 's'); text(ax, f(7) + 2, 31, '−2', 'varie', 's')
text(ax, 44, 40, 'les pentes s’ajoutent : 8 + (−2) = 6', 'resultat', 's')
save(fig, '73-163')
