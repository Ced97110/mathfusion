import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$(x-1)(x-2)(x-3)$', 'sujet', 'm')
box(ax, 2, 24, 84, 34, 'fixe')
text(ax, 10, 52, 'ℚ', 'fixe', 'l')
for i, v in enumerate((1, 2, 3)):
    x = 24 + 20 * i
    disc(ax, x, 41, 5, 'resultat', label=str(v), size='m')
    text(ax, x, 31, rf'$x-{v}$', 'sujet', 's')
text(ax, 44, 16, r'$E=\mathbb{Q}$', 'resultat', 'l', weight='bold')
text(ax, 44, 8, r'$[E:\mathbb{Q}]=1$ : rien à ajouter', 'resultat', 's')
save(fig, '62-152')
