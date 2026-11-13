import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
x0, y0, d = 22, 16, 14
for i in range(3):
    for j in range(3):
        role = 'limite' if (i, j) == (0, 0) else 'resultat'
        disc(ax, x0 + i * d, y0 + j * d, 3.0, role)
line(ax, [(x0 - 2.2, y0 - 2.2), (x0 + 2.2, y0 + 2.2)], 'limite', lw=1.2)
line(ax, [(x0 - 2.2, y0 + 2.2), (x0 + 2.2, y0 - 2.2)], 'limite', lw=1.2)
text(ax, x0 + d, 66, r'$q^n=9$ vecteurs', 'sujet', 'm')
text(ax, 8, 8, 'le vecteur nul est exclu', 'limite', 's', ha='left')
text(ax, 72, y0 + 2 * d + 2, '8 restent', 'resultat', 's')
text(ax, 72, y0 + d, r'$q^n-1=8$', 'resultat', 'l')
save(fig, '75-106')
