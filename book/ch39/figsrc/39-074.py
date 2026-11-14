import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
c = (30, 68); s = 11.0
def P(r, d): return (c[0] + s * r * math.cos(math.radians(d)), c[1] + s * r * math.sin(math.radians(d)))
def arc(r, d0, d1, n=40): return [P(r, d0 + (d1 - d0) * i / n) for i in range(n + 1)]
arrow(ax, (c[0] - 27, c[1]), (c[0] + 30, c[1]), 'fixe', lw=0.7)
arrow(ax, (c[0], c[1] - 24), (c[0], c[1] + 27), 'fixe', lw=0.7)
text(ax, c[0] + 32, c[1] + 3, 'Re', 'fixe', 's'); text(ax, c[0] + 4, c[1] + 28, 'Im', 'fixe', 's')
# z : √3 at 315°, w : √6 at 405° = 45°, q : √(1/2) at 270°
rz, rw, rq = math.sqrt(3), math.sqrt(6), math.sqrt(0.5)
arrow(ax, c, P(rz, 315), 'sujet', lw=1.2)
arrow(ax, c, P(rw, 45), 'autre', lw=1.2)
arrow(ax, c, P(rq, 270), 'resultat', lw=1.6)
line(ax, arc(0.9, 0, -90), 'varie')
text(ax, P(rz, 315)[0] + 1.5, P(rz, 315)[1] - 3.2, 'z : angle 315°', 'sujet', 's', ha='left')
text(ax, P(rw, 45)[0] + 1.5, P(rw, 45)[1] + 3, 'w : angle 405°', 'autre', 's', ha='left')
text(ax, c[0] - 2.5, c[1] - 9, 'q : 270°', 'resultat', 's', ha='right')
text(ax, c[0] + 15, c[1] - 3, '−90°', 'varie', 's')
box(ax, 4, 28, 80, 9, 'fixe', label='module : √3 ÷ √6 = √(1/2) ≈ 0,71', size='s')
box(ax, 4, 17, 80, 9, 'fixe', label='angle : 315° − 405° = −90°, soit 270°', size='s')
box(ax, 4, 3, 80, 11, 'resultat', label='cis 270° = 0 − i , donc q = −(√2/2) i', size='s')
save(fig, '39-074')
