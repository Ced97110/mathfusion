import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

T = math.tan(math.radians(64))
fig, ax = canvas(72)
A = (46, 10); B = (66, 10); S = (66, 10 + 20 * T)
line(ax, [A, B], 'sujet', lw=1.6); line(ax, [B, S], 'resultat', lw=1.6); line(ax, [A, S], 'fixe', dash=True)
line(ax, [(63, 10), (63, 13), (66, 13)], 'fixe', lw=0.7)
arc(ax, A, 6, 0, 64, 'sujet')
text(ax, 57, 16, '64°', 'sujet', 's')
text(ax, 56, 5, '10 m', 'sujet', 'm')
text(ax, 68, 35, '20,5 m', 'resultat', 'm', ha='left')
box(ax, 3, 30, 33, 26, 'autre')
line(ax, [(3, 45), (36, 45)], 'autre', lw=0.6); line(ax, [(19.5, 30), (19.5, 56)], 'autre', lw=0.6)
text(ax, 11.5, 50.5, 'angle', 'autre', 's'); text(ax, 28, 50.5, 'rapport', 'autre', 's')
text(ax, 11.5, 37.5, '64°', 'autre', 'm'); text(ax, 28, 37.5, '2,05', 'autre', 'm', weight='bold')
text(ax, 19.5, 62, 'table déjà calculée', 'autre', 's')
text(ax, 62, 64, '10 × 2,05 = 20,5', 'resultat', 'm')
arrow(ax, (36, 44), (50, 60), 'autre', curve=-0.2)
save(fig, '25-011')
