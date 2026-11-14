import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 62, 'plan : 2 vecteurs', 'fixe', 'm')
text(ax, 65, 62, 'ℤ/4 ⊕ ℤ/2 : 2 morceaux', 'fixe', 'm')
line(ax, [(44, 14), (44, 58)], 'fixe', dash=True)
o = (22, 32)
for (dx, dy), role, lab, (lx, ly) in (((14, 2), 'sujet', 'e₁', (39, 33)), ((3, 12), 'sujet', 'e₂', (25, 47)),
                                      ((10, 10), 'autre', 'f₁', (35, 45)), ((-8, 8), 'autre', 'f₂', (11, 43))):
    arrow(ax, o, (o[0] + dx, o[1] + dy), role, lw=1.2)
    text(ax, lx, ly, lab, role, 's')
box(ax, 48, 38, 20, 9, 'sujet', label='ℤ/4')
box(ax, 70, 38, 14, 9, 'sujet', label='ℤ/2')
box(ax, 48, 22, 20, 9, 'autre', label='ℤ/4')
box(ax, 70, 22, 14, 9, 'autre', label='ℤ/2')
text(ax, 44, 8, '2 = 2 : même nombre', 'resultat', 'm')
save(fig, '60-070')
