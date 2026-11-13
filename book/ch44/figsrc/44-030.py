import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tri_pts(cx, cy, s):
    h = s * math.sqrt(3) / 2
    return [(cx, cy + 2 * h / 3), (cx - s / 2, cy - h / 3), (cx + s / 2, cy - h / 3)]
def tri(ax, cx, cy, s, arr, roles=None, lab=True, fill_role='fixe', show=(1, 2, 3), r=2.3, outline=None):
    """arr = numeros aux places (haut, bas gauche, bas droite)."""
    P = tri_pts(cx, cy, s)
    poly(ax, P, outline or fill_role)
    ax.patches[-1].set_facecolor(FILL[fill_role])
    for p, n in zip(P, arr):
        if n not in show: continue
        role = (roles or {}).get(n, 'sujet' if n == 1 else 'fixe')
        disc(ax, p[0], p[1], r, role, fill=(lab or n != 3), label=str(n) if lab else None, size='s')
    return P
def sq(ax, cx, cy, a, arr, show=(1, 2), lab=True, fill_role='fixe', r=2.2, outline=None):
    """arr = numeros aux places (haut droite, haut gauche, bas gauche, bas droite)."""
    h = a / 2
    poly(ax, [(cx - h, cy - h), (cx + h, cy - h), (cx + h, cy + h), (cx - h, cy + h)], outline or fill_role)
    ax.patches[-1].set_facecolor(FILL[fill_role])
    pos = [(cx + h, cy + h), (cx - h, cy + h), (cx - h, cy - h), (cx + h, cy - h)]
    for p, n in zip(pos, arr):
        if n in show:
            disc(ax, p[0], p[1], r, 'sujet' if n == 1 else 'fixe', label=str(n) if lab else None, size='s')
def axis_of(ax, P, arr, role='varie', dash=True, lw=1.0, label=None):
    i = [k for k in range(3) if arr[k] == k + 1][0]
    a = P[i]; b = ((P[(i+1)%3][0] + P[(i+2)%3][0]) / 2, (P[(i+1)%3][1] + P[(i+2)%3][1]) / 2)
    L = math.hypot(b[0]-a[0], b[1]-a[1]); d = ((b[0]-a[0])/L, (b[1]-a[1])/L)
    line(ax, [(a[0]-2.5*d[0], a[1]-2.5*d[1]), (b[0]+3*d[0], b[1]+3*d[1])], role, lw=lw, dash=dash)
    if label: text(ax, b[0]+7*d[0], b[1]+7*d[1], label, role, 's')
def cut(p, q, d):
    vx, vy = q[0]-p[0], q[1]-p[1]; L = math.hypot(vx, vy)
    return (p[0]+vx/L*d, p[1]+vy/L*d)
fig, ax = canvas(78)
text(ax, 44, 72, r'nombre de mouvements = coins $\times$ 2', 'resultat', 'm')
for x, n, name, eq in [(15, 3, 'triangle', r'$3 \times 2 = 6$'), (44, 4, 'carré', r'$4 \times 2 = 8$'), (73, 6, 'hexagone', r'$6 \times 2 = 12$')]:
    a0 = 90 if n != 4 else 45
    pts = [(x + 10 * math.cos(math.radians(a0 + 360 * k / n)), 54 + 10 * math.sin(math.radians(a0 + 360 * k / n))) for k in range(n)]
    poly(ax, pts, 'sujet')
    for p in pts: disc(ax, p[0], p[1], 1.5, 'varie')
    text(ax, x, 39, name, 'fixe', 's')
    g = 4.2; x00 = x - n * g / 2 + 0.3
    for k in range(n):
        for m in range(2):
            box(ax, x00 + k * g + m * 1.9, 29, 1.6, 4.5, 'varie', r=0.2, lw=0.5)
    text(ax, x, 25, '2 par coin', 'varie', 's')
    text(ax, x, 15, eq, 'encre', 'm')
text(ax, 44, 5, 'chaque trait orange = 1 mouvement', 'varie', 's')
save(fig, '44-030')
