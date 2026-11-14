import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-036 : point (50 ; 86,60) = un endroit ; vecteur ⟨50 ; 86,60⟩ = un déplacement qui peut partir de n'importe où
fig, ax = canvas(72)
s = 0.28
dx, dy = 50 * s, 86.6 * s
# --- gauche : le point ---
O1 = (10, 14)
arrow(ax, O1, (38, O1[1]), 'fixe', lw=0.6); arrow(ax, O1, (O1[0], 56), 'fixe', lw=0.6)
Q = (O1[0] + dx, O1[1] + dy)
line(ax, [O1, (Q[0], O1[1])], 'fixe', dash=True); line(ax, [(Q[0], O1[1]), Q], 'fixe', dash=True)
disc(ax, Q[0], Q[1], 1.6, 'autre')
text(ax, 22, 63, 'point', 'autre', 'm', weight='bold')
text(ax, Q[0] + 3, Q[1] + 4, '(50 ; 86,60)', 'autre', 's', ha='left')
text(ax, 22, 7, 'un endroit', 'autre', 's')
text(ax, O1[0] - 3, O1[1] - 3.5, '$O$', 'encre', 's')
line(ax, [(44, 5), (44, 68)], 'fixe', lw=0.5, dash=True)
# --- droite : le même déplacement, deux départs ---
A1 = (52, 14); A2 = (70, 14)
arrow(ax, A1, (A1[0] + dx, A1[1] + dy), 'sujet', lw=1.6)
arrow(ax, A2, (A2[0] + dx, A2[1] + dy), 'sujet', lw=1.6)
disc(ax, A1[0], A1[1], 0.9, 'encre'); disc(ax, A2[0], A2[1], 0.9, 'encre')
text(ax, 66, 63, 'vecteur', 'sujet', 'm', weight='bold')
text(ax, 66, 56, r'$\langle$50 ; 86,60$\rangle$', 'sujet', 's')
text(ax, 66, 7, 'un déplacement', 'sujet', 's')
text(ax, 66, 47, 'même flèche,', 'fixe', 's')
text(ax, 66, 42.5, 'deux départs', 'fixe', 's')
save(fig, '41-036')
