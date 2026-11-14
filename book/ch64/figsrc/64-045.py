import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
x0 = 8; cw = 3.0
text(ax, 8, 62, r'$S_4$ : 24 files', 'encre', 'm', ha='left')
for i in range(24):
    box(ax, x0 + i * cw, 46, cw, 10, 'sujet' if i < 12 else 'fixe', r=0.2, lw=0.3)
brace(ax, x0, x0 + 12 * cw, 44, 'sujet', label=r'$A_4$ : 12 paires', down=True)
brace(ax, x0 + 12 * cw, x0 + 24 * cw, 44, 'fixe', label='12 impaires', down=True)
text(ax, 8, 31, r'$S_5$ : 120 files', 'encre', 'm', ha='left')
box(ax, x0, 15, 36, 11, 'sujet', label=r'$A_5$ : 60', size='m')
box(ax, x0 + 36, 15, 36, 11, 'fixe', label='60', size='m')
text(ax, 44, 6, r'$A_n$ : la moitié de $S_n$, $n!/2$', 'resultat', 'm', weight='bold')
save(fig, '64-045')
