import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
X = lambda v: 26 + v * 4.5
yb, yp = 58, 44
for y, role, lab in ((yb, 'sujet', 'multiples de 4'), (yp, 'autre', 'multiples de 6')):
    text(ax, 2, y, lab, role, 's', ha='left')
    ax.plot([X(0), X(12)], [y, y], color=COL[role], lw=0.6, zorder=1)
for v in (4, 8):
    disc(ax, X(v), yb, 2.6, 'sujet', label=str(v), size='s')
disc(ax, X(6), yp, 2.6, 'autre', label='6', size='s')
for y in (yb, yp):
    disc(ax, X(12), y, 2.6, 'resultat', label='12', size='s')
line(ax, [(X(12), yb - 2.8), (X(12), yp + 2.8)], 'resultat', dash=True)
text(ax, X(12) - 2.5, (yb + yp) / 2, 'PPCM = 12', 'resultat', 's', ha='right')
text(ax, 44, 36, 'dénominateur commun : 12', 'resultat', 'm', weight='bold')
# barre de 12 cases
cw, x0, y0 = 5.5, 11, 14
for i in range(12):
    role = 'sujet' if i < 3 else ('autre' if i < 5 else 'fixe')
    box(ax, x0 + i * cw, y0, cw, 7, role, r=0.3, lw=0.6)
brace(ax, x0, x0 + 3 * cw, y0 + 7.8, 'sujet', r'$\frac{1}{4}=\frac{3}{12}$', down=False)
brace(ax, x0 + 3 * cw, x0 + 5 * cw, y0 + 7.8, 'autre', r'$\frac{1}{6}=\frac{2}{12}$', down=False)
brace(ax, x0, x0 + 5 * cw, y0 - 0.8, 'resultat', r'$\frac{5}{12}$', down=True, size='m')
text(ax, 62, y0 - 4.5, 'l’unité : 12 cases', 'fixe', 's')
save(fig, '05-175')
