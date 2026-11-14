import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 4, 26, 12, 12, 'resultat', label='A\n0')
text(ax, 24, 32, '…', 'fixe', 'l')
labs = ['X\n23', 'Y\n24', 'Z\n25']
for k, lab in enumerate(labs):
    box(ax, 32 + k * 14, 26, 12, 12, 'sujet' if k == 0 else 'fixe', label=lab)
box(ax, 74, 26, 12, 12, 'limite', dash=True, label='26')
arrow(ax, (38, 25.5), (79, 25.5), 'varie', curve=0.3, lw=1.3)
text(ax, 58, 14, '23 + 3 = 26', 'varie', 'm')
text(ax, 77, 18, 'pas de case 26', 'limite', 's')
arrow(ax, (80, 38.5), (10, 38.5), 'resultat', curve=0.35, lw=1.3)
text(ax, 45, 54, '26 compte pour 0', 'resultat', 'm')
save(fig, '53-015')
