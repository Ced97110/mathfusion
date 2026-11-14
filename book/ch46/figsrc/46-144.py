import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
r = 10; cy = 25
def P(cx, d): return (cx + r * math.cos(math.radians(d)), cy + r * math.sin(math.radians(d)))
steps = [(15, 'départ', r'$z$ et $w$ : module 1', 'sujet'), (44, 'étape clé', r'$w^{-1}=\mathrm{cis}(-\psi)$', 'varie'),
         (73, 'arrivée', r'$\mathrm{cis}(\theta-\psi)$', 'resultat')]
for cx, t, f, role in steps:
    text(ax, cx, 47, t, role, 'm', weight='bold'); disc(ax, cx, cy, r, role)
    text(ax, cx, 9, f, role, 's')
def pt(cx, d, role, lab, dx, dy, ha='left'):
    x, y = P(cx, d); line(ax, [(cx, cy), (x, y)], role, lw=0.6); disc(ax, x, y, 1.0, role); text(ax, x + dx, y + dy, lab, role, 's', ha=ha)
pt(15, 90, 'sujet', r'$z$', 0, 3, 'center'); pt(15, 30, 'autre', r'$w$', 1.6, 0)
pt(44, 30, 'autre', r'$w$', 1.6, 0); pt(44, -30, 'varie', r'$w^{-1}$', 1.6, 0)
pt(73, 60, 'resultat', r'$zw^{-1}$', 0, 3.4, 'center')
arrow(ax, (26.5, cy), (32.5, cy), 'fixe'); arrow(ax, (55.5, cy), (61.5, cy), 'fixe')
text(ax, 73, 2.5, 'module 1 × 1 = 1', 'resultat', 's')
save(fig, '46-144')
