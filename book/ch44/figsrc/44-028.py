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
fig, ax = canvas(60)
text(ax, 44, 54, 'garde 3, échange 1 et 2', 'encre', 'm')

P0 = tri_pts(22, 28, 26)
for _a in [(1,3,2), (3,2,1)]: axis_of(ax, P0, _a, 'fixe', lw=0.7)
P = tri(ax, 22, 28, 26, (1,2,3), roles={1: 'sujet', 2: 'sujet', 3: 'sujet'}, fill_role='sujet')
axis_of(ax, P, (2,1,3), label='axe')
tri(ax, 66, 28, 26, (2,1,3), roles={3: 'fixe', 1: "varie", 2: "varie"}, fill_role='resultat')
arrow(ax, (37, 28), (51, 28), 'varie', lw=1.2); text(ax, 44, 34, r'$\tau_3$', 'varie', 'l')
text(ax, 44, 6, 'un retournement par sommet', 'resultat', 's')
save(fig, '44-028')
