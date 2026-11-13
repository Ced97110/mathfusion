import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-042 : j = ⟨0 ; 1⟩ = un pas de longueur 1 vers le nord, perpendiculaire à i ; le vent de 86,60 vers le nord = 86,60 j
fig, ax = canvas(78)
s = 0.5                       # barre de 86,60 pas : 0,5 mm par pas
x0 = 12; y0 = 8
H = 86.6 * s
ax.add_patch(Rectangle((x0 - 1.8, y0), 3.6, H, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
for k in range(0, 9):         # un repère tous les 10 pas
    yy = y0 + 10 * k * s
    line(ax, [(x0 - 1.8, yy), (x0 + 1.8, yy)], 'varie', lw=0.6)
text(ax, x0 + 4, y0 + H / 2, '86,60 pas', 'varie', 's', ha='left')
text(ax, x0 + 4, y0 + H / 2 - 5, 'vers le nord', 'varie', 's', ha='left')
text(ax, x0, y0 + H + 4, '86,60 $j$', 'varie', 'm')
# i et j agrandis, perpendiculaires (longueur 1 = 16 mm)
O = (52, 22); L = 16
arrow(ax, O, (O[0] + L, O[1]), 'fixe', lw=1.8)
arrow(ax, O, (O[0], O[1] + L), 'sujet', lw=2.2)
d = 2.2
line(ax, [(O[0] + d, O[1]), (O[0] + d, O[1] + d), (O[0], O[1] + d)], 'fixe', lw=0.6)
text(ax, O[0] + L + 3, O[1], '$i$', 'fixe', 'm', ha='left')
text(ax, O[0], O[1] + L + 3.5, '$j$', 'sujet', 'l', weight='bold')
text(ax, 70, 52, r'$j = \langle$0 ; 1$\rangle$', 'sujet', 'm')
text(ax, 70, 46, 'un pas vers le nord', 'sujet', 's')
text(ax, 66, 12, 'perpendiculaire à $i$', 'fixe', 's')
save(fig, '41-042')
