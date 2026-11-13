import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, R = 28, 46, 22
def pt(a, r=R): return (ox + r * math.cos(math.radians(a)), oy + r * math.sin(math.radians(a)))
def arc(a0, a1, r, role):
    n = 24; pts = [pt(a0 + (a1 - a0) * i / n, r) for i in range(n + 1)]
    line(ax, pts, role, lw=1.6); arrow(ax, pts[-2], pts[-1], role, lw=1.6)
for a, role in ((0, 'fixe'), (30, 'sujet'), (80, 'resultat')):
    line(ax, [(ox, oy), pt(a)], role, lw=1.2)
arc(0, 30, 13, 'sujet'); arc(30, 80, 17, 'varie')
disc(ax, ox, oy, 1.3, 'encre'); text(ax, ox - 3, oy - 3, r'$O$', 'encre', 's')
text(ax, 56, 50, '30°', 'sujet', 'm', ha='left'); text(ax, 40, 64, '+ 50°', 'varie', 'm', ha='left')
text(ax, 62, 62, '= 80°', 'resultat', 'l', ha='left')
f = numberline(ax, 10, 78, 20, -30, 80, step=10, labels=False, arrow_right=False)
for v, role, lab in ((-30, 'autre', '−30'), (0, 'fixe', '0'), (30, 'sujet', '30'), (80, 'resultat', '80')):
    disc(ax, f(v), 20, 1.6, role); text(ax, f(v), 14, lab, role, 's')
arrow(ax, (f(0), 24), (f(30), 24), 'sujet', curve=-0.4); arrow(ax, (f(30), 24), (f(80), 24), 'varie', curve=-0.4)
arrow(ax, (f(30), 17), (f(-30), 17), 'autre', curve=-0.3)
text(ax, f(-30) + 2, 29, 'neutre : 0', 'fixe', 's', ha='left'); text(ax, f(50), 8, 'défaire 30 : −30', 'autre', 's')
save(fig, '44-132')
