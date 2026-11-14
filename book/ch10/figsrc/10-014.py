import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0 = 4; k = 72 / 200
text(ax, x0, 50, '48 + 49 + 51 + 52 = 200', 'sujet', 'm', ha='left')
x = x0
for v in (48, 49, 51, 52):
    box(ax, x, 36, v * k, 9, 'sujet', label=str(v), lw=0.7); x += v * k
text(ax, x0, 28, r'4 $\times$ 50 = 200', 'autre', 'm', ha='left')
for i in range(4):
    box(ax, x0 + i * 50 * k, 14, 50 * k, 9, 'autre', label='50', lw=0.7)
for xe in (x0, x0 + 200 * k): line(ax, [(xe, 10), (xe, 46)], 'resultat', dash=True)
text(ax, x0 + 100 * k, 6, 'même longueur : 200', 'resultat', 'm')
save(fig, '10-014')
