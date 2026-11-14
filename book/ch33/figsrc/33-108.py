import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
R = 17; cy = 34
def arc(cx, a0, a1, r=R, n=50): return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
def pt(cx, a, r=R): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
for cx, title, a, b in ((22, r'$\arctan(\tan\,108°)$', 108, -72), (66, r'$\arcsin(\cos\,225°)$', 225, -45)):
    line(ax, arc(cx, 90, 270), 'fixe', lw=0.6); line(ax, arc(cx, -90, 90), 'resultat', lw=2.2)
    line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.5); line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.5)
    A, B = pt(cx, a), pt(cx, b)
    arrow(ax, (A[0] + (B[0] - A[0]) * 0.1, A[1] + (B[1] - A[1]) * 0.1), (A[0] + (B[0] - A[0]) * 0.9, A[1] + (B[1] - A[1]) * 0.9), 'varie')
    disc(ax, A[0], A[1], 1.7, 'sujet'); disc(ax, B[0], B[1], 1.7, 'resultat')
    ax.texts  # no-op
    pa, pb = pt(cx, a, R + 6.5), pt(cx, b, R + 6.5)
    text(ax, pa[0], pa[1], f'{a}°'.replace('-', '−'), 'sujet', 's'); text(ax, pb[0], pb[1], f'{b}°'.replace('-', '−'), 'resultat', 's')
    text(ax, cx, 60, title, 'encre', 's')
disc(ax, 8, 6, 1.5, 'sujet'); text(ax, 11, 6, 'angle donné', 'sujet', 's', ha='left')
disc(ax, 48, 6, 1.5, 'resultat'); text(ax, 51, 6, 'résultat', 'resultat', 's', ha='left')
save(fig, '33-108')
