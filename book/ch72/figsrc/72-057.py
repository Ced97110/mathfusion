import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [12, 32, 52, 72]; cy = 30; h = 5.5
def sq(cx, k, role):
    a = math.radians(90 * k)
    pts = [(cx + h * (math.cos(a) * px - math.sin(a) * py), cy + h * (math.sin(a) * px + math.cos(a) * py)) for px, py in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    poly(ax, pts, role)
    mx, my = pts[0]; px_, py_ = pts[1]
    disc(ax, mx + (pts[2][0] - mx) * 0.22, my + (pts[2][1] - my) * 0.22, 1.5, 'varie')
for k, x in enumerate(xs):
    sq(x, k, 'resultat' if k == 3 else 'sujet')
text(ax, xs[0], 18, 'départ', 'sujet', 's'); text(ax, xs[1], 18, '1/4 de tour', 'sujet', 's')
text(ax, xs[3], 18, '3/4 de tour', 'resultat', 's')
arrow(ax, (xs[0] + 3, cy + 8), (xs[1] - 3, cy + 8), 'varie', curve=-0.5)
arrow(ax, (xs[1] + 3, cy + 8), (xs[3] - 3, cy + 8), 'varie', curve=-0.35)
text(ax, 22, 48, '1/4 de tour', 'varie', 's'); text(ax, 52, 52, 'puis demi-tour', 'varie', 's')
arrow(ax, (xs[1] - 3, cy - 8), (xs[0] + 3, cy - 8), 'fixe', curve=-0.5)
text(ax, 22, 10, 'défaire', 'fixe', 's')
text(ax, 62, 8, 'la mesure est conservée', 'resultat', 's')
save(fig, '72-057')
