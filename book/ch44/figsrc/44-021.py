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
fig, ax = canvas(92)
for x, a in zip([16, 44, 72], [(1,2,3), (3,1,2), (2,3,1)]):
    tri(ax, x, 74, 20, a, show=(1,), fill_role='sujet')
brace(ax, 6, 82, 66, 'sujet', '3 places pour le sommet 1')
tri(ax, 18, 38, 20, (1,2,3), fill_role='resultat')
tri(ax, 46, 38, 20, (1,3,2), fill_role='resultat')
brace(ax, 8, 56, 30, 'resultat', '2 faces')
text(ax, 74, 38, r'$3 \times 2 = 6$', 'resultat', 'xl')
save(fig, '44-021')
