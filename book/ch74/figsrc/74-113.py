import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cy = 36; L = 14; R = 13
def pt(cx, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arcp(cx, r, a0, a1, n=40): return [pt(cx, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
for cx, a, hd, bt, n in [(22, 45, 'miroirs à 45°', 'quart de tour (ordre 4)', 4), (66, 36, 'miroirs à 36°', 'ordre 5 : 5 × 72° = 360°', 5)]:
    t = 360 / n
    line(ax, arcp(cx, R, 0, 360, 90), 'fixe', lw=0.6, dash=True)
    for k in range(n):
        p = pt(cx, R, k * t); disc(ax, p[0], p[1], 0.9, 'resultat')
    line(ax, [pt(cx, -L, 0), pt(cx, L, 0)], 'sujet', lw=1.3)
    line(ax, [pt(cx, -L, a), pt(cx, L, a)], 'sujet', lw=1.3)
    line(ax, arcp(cx, 6, 0, a), 'varie', lw=1.0)
    q = pt(cx, 9.8, a / 2); text(ax, q[0], q[1], f'{a}°', 'varie', 's')
    pts = arcp(cx, R, 0, 2 * a); line(ax, pts, 'resultat', lw=1.6); arrow(ax, pts[-4], pts[-1], 'resultat', lw=1.6)
    q = pt(cx, 18.5, a); text(ax, q[0], q[1], f'{2 * a}°', 'resultat', 's')
    text(ax, cx, 62, hd, 'sujet', 'm')
    text(ax, cx, 12, bt, 'resultat', 's')
save(fig, '74-113')
