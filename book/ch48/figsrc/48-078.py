import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 22, 22, 28, 'fixe'); text(ax, 13, 54, "entiers", 'fixe', 's')
for k in range(12): disc(ax, 6.5 + 5.5 * (k % 3), 27 + 6.5 * (k // 3), 1.7, 'fixe')
box(ax, 40, 22, 16, 28, 'sujet'); text(ax, 48, 54, "paquets", 'sujet', 's')
box(ax, 72, 22, 14, 28, 'resultat'); text(ax, 79, 54, "positions", 'resultat', 's')
for j in range(4):
    disc(ax, 48, 27 + 6.5 * j, 2.2, 'sujet'); disc(ax, 79, 27 + 6.5 * j, 2.2, 'resultat')
arrow(ax, (24, 36), (40, 36), 'varie', lw=1.4); text(ax, 32, 40, r"$\nu$ : sur", 'varie', 's')
arrow(ax, (56, 36), (72, 36), 'resultat', lw=1.4); text(ax, 64, 40, "injective", 'resultat', 's')
text(ax, 32, 30, "confond", 'varie', 's'); text(ax, 64, 30, "sans perte", 'resultat', 's')
arrow(ax, (13, 22), (79, 22), 'fixe', curve=0.25); text(ax, 46, 14, r"$f$", 'fixe', 'm')
save(fig, '48-078')
