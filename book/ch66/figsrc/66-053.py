import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 59, '4 racines primitives', 'sujet', 's')
labs = [r'$\zeta$', r'$\zeta^2$', r'$\zeta^3$', r'$\zeta^4$']
for i, l in enumerate(labs):
    y = 48 - i * 11
    disc(ax, 8, y, 3.0, 'sujet')
    text(ax, 14, y, l, 'sujet', 'm', ha='left')
    arrow(ax, (26, y), (50, 27 + (y - 31.5) * 0.35), 'sujet', lw=0.8)
box(ax, 51, 18, 35, 20, 'resultat', label=r'$\Phi_5$', size='xl')
text(ax, 68.5, 12, 'un seul polynôme', 'resultat', 's')
text(ax, 68.5, 7.5, 'de degré 4', 'resultat', 's')
text(ax, 68.5, 44, '5 côtés', 'fixe', 's')
save(fig, '66-053')
