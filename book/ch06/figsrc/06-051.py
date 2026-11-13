import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cs, x0 = 5, 8
for g in range(2):
    for i in range(5):
        box(ax, x0 + (g * 5 + i) * cs, 40, cs, cs, 'sujet', r=0.2)
brace(ax, x0 + 0.5, x0 + 5 * cs - 0.5, 40, 'sujet', label='5')
brace(ax, x0 + 5 * cs + 0.5, x0 + 10 * cs - 0.5, 40, 'sujet', label='5')
text(ax, x0 + 5 * cs, 57, r'$2\times5$ : prendre 5, 2 fois', 'encre', 'm')
text(ax, x0 + 10 * cs + 6, 43, '= 10', 'resultat', 'l', ha='left', weight='bold')
for i in range(12):
    box(ax, x0 + i * cs, 8, cs, cs, 'varie' if i < 4 else 'fixe', r=0.2)
text(ax, x0 + 6 * cs, 25, r'$\frac{1}{3}\times12$ : prendre $\frac{1}{3}$ de 12', 'encre', 'm')
text(ax, x0 + 12 * cs + 3, 11, '= 4', 'resultat', 'l', ha='left', weight='bold')
save(fig, '06-051')
