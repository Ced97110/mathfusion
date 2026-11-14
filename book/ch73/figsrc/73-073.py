import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 2, 4, 84, 64, 'fixe'); text(ax, 44, 62, r'matrices inversibles ($2\times 2$)', 'fixe', 's')
box(ax, 6, 8, 48, 46, 'sujet'); text(ax, 30, 49.5, r'$O(n)$ : $A^{-1}=A^{t}$', 'sujet', 's', weight='bold')
for y, s in [(40, 'identité'), (28, 'quart de tour'), (16, 'miroir')]:
    disc(ax, 12, y, 1.6, 'sujet'); text(ax, 16, y, s, 'sujet', 's', ha='left')
disc(ax, 70, 30, 1.6, 'limite'); text(ax, 70, 24.5, 'cisaillement', 'limite', 's')
text(ax, 70, 35.5, r'$A^{-1}\neq A^{t}$', 'limite', 's')
save(fig, '73-073')
