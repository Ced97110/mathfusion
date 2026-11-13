import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
R = 16; Y = 38
cxs = (22, 66)
def pt(cx, k, r=R):
    a = math.radians(90 - 45 * k); return (cx + r * math.cos(a), Y + r * math.sin(a))
def chord(cx, a, b, role):
    p, q = pt(cx, a), pt(cx, b)
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    arrow(ax, (p[0] + 2.4 * ux, p[1] + 2.4 * uy), (q[0] - 2.4 * ux, q[1] - 2.4 * uy), role, lw=0.9)
for cx in cxs:
    ax.add_patch(Circle((cx, Y), R, ec=COL['fixe'], fc='none', lw=0.5, zorder=1, ls='--'))
seq = [(3 * j) % 8 for j in range(9)]
for a, b in zip(seq, seq[1:]): chord(cxs[0], a, b, 'varie')
for k in range(8):
    disc(ax, *pt(cxs[0], k), 1.5, 'sujet' if k == 0 else 'varie')
chord(cxs[1], 0, 4, 'varie'); chord(cxs[1], 4, 0, 'varie')
for k in range(8):
    on = k in (0, 4)
    disc(ax, *pt(cxs[1], k), 1.5, 'sujet' if k == 0 else ('varie' if on else 'fixe'))
text(ax, cxs[0], pt(cxs[0], 0)[1] + 4.5, '0', 'sujet', 's')
text(ax, cxs[1], pt(cxs[1], 0)[1] + 4.5, '0', 'sujet', 's')
text(ax, cxs[0], 64, 'avancer de 3', 'varie', 's')
text(ax, cxs[1], 64, 'avancer de 4', 'varie', 's')
text(ax, cxs[0], 14, 'retour après 8 pas', 'resultat', 's')
text(ax, cxs[1], 14, 'retour après 2 pas', 'resultat', 's')
text(ax, cxs[0], 7, 'ordre 8', 'resultat', 'l')
text(ax, cxs[1], 7, 'ordre 2', 'resultat', 'l')
save(fig, '39-137')
