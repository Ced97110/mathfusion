import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
y, h = 36, 10
box(ax, 1, y, 10, h, 'sujet', label='sac', size='s')
for x, nm in ((16, r'$\eta$ ($A$)'), (35, r'$\rho$ ($C$)'), (54, r'$\tau$ ($D$)')):
    box(ax, x, y, 14, h, 'varie', label=nm, size='s')
box(ax, 73, y, 14, h, 'sujet', label='image', size='s')
for a, b in ((11, 16), (30, 35), (49, 54), (68, 73)):
    arrow(ax, (a + 0.3, y + h / 2), (b - 0.3, y + h / 2), 'fixe')
brace(ax, 16, 49, y - 1.5, 'fixe', label=r'$D(CA)$ : on groupe η, ρ', down=True, size='s')
brace(ax, 35, 68, y - 11.5, 'fixe', label=r'$(DC)A$ : on groupe ρ, τ', down=True, size='s')
text(ax, 44, 12, r'$(DC)A=D(CA)$', 'resultat', 'l', weight='bold')
text(ax, 44, 5, 'mêmes actions, même ordre', 'resultat', 's')
save(fig, '58-219')
