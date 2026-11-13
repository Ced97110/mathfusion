import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# 41-041 : i = ⟨1 ; 0⟩ = un pas de longueur 1 vers l'est ; le vent de 50 vers l'est = 50 pas (50 cases de 1,4 mm)
fig, ax = canvas(62)
c = 1.4
x0 = 8; y0 = 44
for k in range(50):
    role = 'sujet' if k == 0 else 'varie'
    ax.add_patch(Rectangle((x0 + k * c, y0), c, 4.0, ec=COL[role], fc=FILL[role], lw=0.35, zorder=2))
brace(ax, x0, x0 + 50 * c, y0 + 5, 'varie', label='50 pas vers l’est', down=False)
# zoom sur le premier pas
line(ax, [(x0, y0), (10, 26)], 'sujet', lw=0.5, dash=True)
line(ax, [(x0 + c, y0), (10 + 16, 26)], 'sujet', lw=0.5, dash=True)
arrow(ax, (10, 24), (26, 24), 'sujet', lw=2.2)
line(ax, [(10, 22), (10, 26)], 'sujet', lw=1.0); line(ax, [(26, 22), (26, 26)], 'sujet', lw=1.0)
text(ax, 18, 18.5, 'longueur 1', 'sujet', 's')
text(ax, 18, 30.5, '$i$', 'sujet', 'l', weight='bold')
text(ax, 60, 30, r'$i = \langle$1 ; 0$\rangle$', 'sujet', 'm')
text(ax, 60, 24, 'un pas vers l’est', 'sujet', 's')
text(ax, 44, 8, '50 pas = 50 fois $i$', 'varie', 'm')
save(fig, '41-041')
