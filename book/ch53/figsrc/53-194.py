import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
# 26 multiplications une à une
text(ax, 44, 64, 'multiplier un à un : 26', 'fixe', 's')
for i in range(26):
    ax.add_patch(Rectangle((2 + 3.2 * i, 52), 2.9, 7, ec=COL['fixe'], fc=FILL['fixe'], lw=0.6, zorder=2))
text(ax, 44, 43, '27 = 11011 en binaire', 'sujet', 'm')
# carrés successifs : 4 carrés puis 3 produits
for i in range(7):
    role = 'varie' if i < 4 else 'resultat'
    box(ax, 2 + 11.9 * i, 18, 10.2, 10, role, label=r'$x^2$' if i < 4 else r'$\times$')
brace(ax, 2, 2 + 3 * 11.9 + 10.2, 18, 'varie', label='4 carrés')
brace(ax, 2 + 4 * 11.9, 2 + 6 * 11.9 + 10.2, 18, 'resultat', label='3 produits')
text(ax, 44, 34, '7 au lieu de 26', 'resultat', 'm')
save(fig, '53-194')
