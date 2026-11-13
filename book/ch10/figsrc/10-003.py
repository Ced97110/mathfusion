import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0 = 4; u = 6.0
text(ax, x0, 48, r'attendu : 50 $\times$ 10 = 500', 'sujet', 'm', ha='left')
box(ax, x0, 36, u, 8, 'sujet')
text(ax, x0, 28, 'annoncé : 5 760', 'limite', 'm', ha='left')
for i in range(11):
    box(ax, x0 + i * u, 16, u, 8, 'sujet', lw=0.6, r=0.3)
box(ax, x0 + 11 * u, 16, 5760 / 500 * u - 11 * u, 8, 'limite', lw=0.6, r=0.3)
brace(ax, x0, x0 + 11 * u, 15, 'sujet', 'plus de 11 fois 500', down=True)
save(fig, '10-003')
