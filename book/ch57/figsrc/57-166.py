import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = numberline(ax, 6, 78, 30, 0, 15, labels=False, arrow_right=False)
for v in range(16):
    if v % 3 == 0:
        disc(ax, f(v), 30, 1.8, 'resultat'); text(ax, f(v), 24, str(v), 'resultat', 's')
for a, b in [(3, 9), (6, 9)]:
    arrow(ax, (f(a), 33), (f(b) - (0.6 if a == 3 else -0.6), 33.6), 'varie', lw=1.0, curve=-0.45)
text(ax, f(6), 48, '3 + 6 = 9', 'varie', 's')
arrow(ax, (f(3), 27), (f(15), 27), 'sujet', lw=1.0, curve=0.35)
text(ax, f(9), 11.5, '3 × 5 = 15', 'sujet', 's')
text(ax, 44, 60, 'coefficients qui tuent x', 'resultat', 's', weight='bold')
text(ax, 44, 55, '3 et 6 tuent x ; 9 et 15 aussi', 'encre', 's')
text(ax, 44, 3, 'somme et multiple restent dans l’ensemble', 'resultat', 's')
save(fig, '57-166')
