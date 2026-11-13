import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

fig, ax = canvas(74)
O = (14, 12)
arrow(ax, O, (84, 12), 'fixe', lw=0.9); arrow(ax, O, (14, 66), 'fixe', lw=0.9)
for x, s in [(44, '20'), (74, '40')]:
    line(ax, [(x, 11), (x, 13)], 'fixe', lw=0.8); text(ax, x, 8, s, 'fixe', 's')
text(ax, 60, 3.5, 'distance (m)', 'fixe', 's'); text(ax, 16, 69, 'hauteur (m)', 'fixe', 's', ha='left')
line(ax, [O, (74, 52.3)], 'resultat', dash=True, lw=1.0)
ys = lambda t: 32.1 + (48 - 32.1) * t
line(ax, [(44 + 30 * t / 20, ys(t / 20)) for t in range(21)], 'limite', dash=True, lw=1.0)
disc(ax, 44, 32.1, 1.4, 'sujet'); disc(ax, 74, 52.3, 1.4, 'resultat'); disc(ax, 74, 48, 1.4, 'limite')
text(ax, 44, 38, '16,78 m', 'sujet', 's')
text(ax, 77, 52.8, '33,56', 'resultat', 's', ha='left'); text(ax, 77, 47.5, '30 ?', 'limite', 's', ha='left')
text(ax, 42, 60, 'si le rapport est constant', 'resultat', 's')
text(ax, 66, 34, 'rien ne l’interdit', 'limite', 's')
save(fig, '25-014')
