import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(74)
r = 17
for cxp, step, role, title, sub in [(22, 45, 'sujet', r'$\mathrm{cis}\,45°$', '8 points : primitive'),
                                    (66, 90, 'autre', r'$\mathrm{cis}\,90°$', '4 points seulement')]:
    cyp = 38
    disc(ax, cxp, cyp, r, 'fixe', fill=False, lw=0.6)
    allp = [(cxp + r * math.cos(math.radians(45 * k)), cyp + r * math.sin(math.radians(45 * k))) for k in range(8)]
    used = [(cxp + r * math.cos(math.radians(step * k)), cyp + r * math.sin(math.radians(step * k))) for k in range(360 // step)]
    poly(ax, used, role, fill=False, lw=1.0)
    for p in allp:
        disc(ax, p[0], p[1], 1.3, 'fixe', fill=True, lw=0.6)
    for p in used:
        disc(ax, p[0], p[1], 1.5, role)
    text(ax, cxp, 66, title, role, 'm')
    text(ax, cxp, 10, sub, 'resultat' if role == 'sujet' else 'autre', 's')
text(ax, 44, 70, '', 'encre', 's')
text(ax, 4, 3, r'$n=8$ : 8 points sur le cercle', 'fixe', 's', ha='left')
save(fig, '39-108')
