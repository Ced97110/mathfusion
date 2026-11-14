import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 9, 38, r'$|\mathrm{Gal}|$', 'sujet', 's')
text(ax, 9, 20, r'$[E:\mathbb{Q}]$', 'autre', 's')
text(ax, 31, 58, r'$\mathbb{Q}(\sqrt{2})$, $x^2-2$', 'resultat', 's')
text(ax, 69, 58, r'$\mathbb{Q}(r)$, $x^3-2$', 'limite', 's')
# panneau A : 2 et 2
for k in range(2):
    box(ax, 20 + k * 11, 32, 9, 12, 'sujet')
    box(ax, 20 + k * 11, 14, 9, 12, 'autre', label=[r'$1$', r'$\sqrt{2}$'][k], size='s')
# panneau B : 1 et 3
box(ax, 54, 32, 9, 12, 'sujet')
for k in range(3):
    box(ax, 54 + k * 11, 14, 9, 12, 'autre', label=[r'$1$', r'$r$', r'$r^2$'][k], size='s')
text(ax, 31, 6, r'$2=2$', 'resultat', 'm')
text(ax, 71, 6, r'$1\neq3$', 'limite', 'm')
text(ax, 69, 52, r'$r$ : racine cubique de 2', 'fixe', 's')
save(fig, '63-083')
