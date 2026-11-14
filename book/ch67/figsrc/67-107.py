import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
f = numberline(ax, 8, 80, 82, 0, 12, 1, labels=False, arrow_right=False)
for v in (0, 4, 8, 12): text(ax, f(v), 76, str(v), 'sujet', 's')
text(ax, f(6), 76, '6', 'autre', 's', weight='bold')
disc(ax, f(6), 82, 1.8, 'autre')
for a in (0, 4, 8): arrow(ax, (f(a), 84), (f(a + 4), 84), 'sujet', curve=-0.55)
text(ax, 44, 96, r'multiples de 4 : $4k$', 'sujet', 's')
box(ax, 6, 56, 76, 12, 'limite', label=r'$4k=6$ : aucun entier $k$, donc pas dedans', size='s')
cy, R, d = 34, 15, 7
cl, cr = 44 - d, 44 + d
th = math.acos(d / R)
arc_l = [(cl + R * math.cos(t), cy + R * math.sin(t)) for t in [(-th + 2 * th * i / 20) for i in range(21)]]
arc_r = [(cr + R * math.cos(t), cy + R * math.sin(t)) for t in [(math.pi - th + 2 * th * i / 20) for i in range(21)]]
poly(ax, arc_l + arc_r, 'resultat')
ax.add_patch(Circle((cl, cy), R, ec=COL['sujet'], fc='none', lw=0.9, zorder=3))
ax.add_patch(Circle((cr, cy), R, ec=COL['autre'], fc='none', lw=0.9, zorder=3))
text(ax, cl - 8, cy, r'$\mathbb{F}_{p^4}$', 'sujet', 'm')
text(ax, cr + 8, cy, r'$\mathbb{F}_{p^6}$', 'autre', 'm')
text(ax, 44, cy, r'$\mathbb{F}_{p^2}$', 'resultat', 'm')
text(ax, 44, 10, r'en commun : exposant $2=$ PGCD$(4,6)$', 'resultat', 's')
save(fig, '67-107')
