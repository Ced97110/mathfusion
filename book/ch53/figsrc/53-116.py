import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$17^{27}$ modulo 55', 'encre', 'm')
text(ax, 4, 48, 'Méthode naïve : 26 multiplications', 'fixe', 's', ha='left')
for i in range(26):
    box(ax, 4 + i * 3.1, 38, 2.6, 6, 'fixe', r=0.2, lw=0.5)
text(ax, 4, 28, 'Carrés successifs : 7 multiplications', 'sujet', 's', ha='left')
for i in range(7):
    role = 'varie' if i < 4 else 'resultat'
    box(ax, 4 + i * 11, 14, 9, 9, role, r=0.3)
text(ax, 4 + 2 * 11 - 1, 8, '4 carrés', 'varie', 's')
text(ax, 4 + 5 * 11 + 3, 8, '3 produits', 'resultat', 's')
save(fig, '53-116')
