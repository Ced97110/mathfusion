import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cx, cy, R = 48, 46, 20
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, ls='--', zorder=1))
arrow(ax, (cx - 38, cy), (cx + R + 5, cy), 'fixe', lw=0.7)
def pt(k):
    a = math.radians(72 * k); return (cx + R * math.cos(a), cy + R * math.sin(a))
# paires conjuguées : (1,4) en bleu, (2,3) en violet
for ks, role in (((1, 4), 'sujet'), ((2, 3), 'autre')):
    sx = sum(pt(k)[0] - cx for k in ks) + cx
    for k in ks:
        line(ax, [(cx, cy), pt(k)], role)
        line(ax, [pt(k), (sx, cy)], role, dash=True, lw=0.7)
    disc(ax, sx, cy, 1.5, role)
for k, role in ((1, 'sujet'), (2, 'autre'), (3, 'autre'), (4, 'sujet')):
    x, y = pt(k); disc(ax, x, y, 1.6, role)
disc(ax, pt(0)[0], pt(0)[1], 1.4, 'fixe')
text(ax, pt(0)[0] + 3, pt(0)[1] + 3, '1', 'fixe', 's')
text(ax, pt(1)[0] + 3.5, pt(1)[1] + 2, r'$\omega$', 'sujet', 's')
text(ax, pt(4)[0] + 3.5, pt(4)[1] - 2, r'$\omega^4$', 'sujet', 's')
text(ax, pt(2)[0] - 4, pt(2)[1] + 2, r'$\omega^2$', 'autre', 's')
text(ax, pt(3)[0] - 4, pt(3)[1] - 2, r'$\omega^3$', 'autre', 's')
sx1 = cx + 2 * R * math.cos(math.radians(72)); sx2 = cx + 2 * R * math.cos(math.radians(144))
text(ax, sx1 + 1, cy + 4.5, r'$s$', 'sujet', 'l')
text(ax, sx2, cy + 4.5, r'$t$', 'autre', 'l')
text(ax, 22, 78, r'$s = \omega + \omega^4$', 'sujet', 'm')
text(ax, 66, 78, r'$t = \omega^2 + \omega^3$', 'autre', 'm')
text(ax, 44, 12, r'$\sigma_4$ fixe $s$ et $t$', 'resultat', 'm')
text(ax, 44, 5, r'$\sigma_2$ échange $s$ et $t$', 'varie', 'm')
save(fig, '63-167')
