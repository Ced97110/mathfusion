import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(70)
disc(ax, 20, 52, 12, 'fixe'); ring(ax, 20, 52, 12, 'fixe', 1.0)
arrow(ax, (8, 52), (32, 52), 'sujet', lw=1.5, both=True)
text(ax, 20, 56, r'$d$ = 7 pouces', 'sujet', 's')
text(ax, 62, 56, r'$C$ = $d$ $\times$ $\pi$', 'encre', 'm')
box(ax, 4, 6, 38, 28, 'limite')
text(ax, 23, 28, r'7 $\times$ 3,14159…', 'limite', 'm')
text(ax, 23, 20, 'chiffres sans fin', 'limite', 's')
text(ax, 23, 12, 'valeur approchée', 'limite', 's')
box(ax, 46, 6, 38, 28, 'resultat')
text(ax, 65, 28, r'$C$ = 7$\pi$ pouces', 'resultat', 'm', weight='bold')
text(ax, 65, 20, '2 caractères', 'resultat', 's')
text(ax, 65, 12, 'exact', 'resultat', 's')
save(fig, '11-094')
