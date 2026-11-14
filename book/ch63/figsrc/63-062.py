import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
spec = [
    ('sujet', r'Départ : $f(\alpha)=0$', r'$f=x^2-2$ , $\alpha=\sqrt{2}$'),
    ('fixe', r'$0=\sigma(f(\alpha))$', r'$\sigma(\sqrt{2}\cdot\sqrt{2}-2)$'),
    ('varie', r'$\sigma(a_i)=a_i$ : $a_i\in F$', r'$\sigma(2)=2$ : 2 est dans $\mathbb{Q}$'),
    ('resultat', r'$=f(\sigma(\alpha))=0$', r'$(-\sqrt{2})^2-2=0$'),
]
arrows = [r'on applique $\sigma$', r'$\sigma$ respecte + et $\times$', 'on regroupe']
for i, (r, a, b) in enumerate(spec):
    y = 78 - 24 * i
    box(ax, 6, y, 76, 16, r)
    text(ax, 44, y + 11, a, r, 'm')
    text(ax, 44, y + 4.5, b, r, 's')
for i, t in enumerate(arrows):
    ytop = 78 - 24 * i
    arrow(ax, (30, ytop), (30, ytop - 8), 'fixe')
    text(ax, 34, ytop - 4, t, 'fixe', 's', ha='left')
text(ax, 44, 3, r'$\sigma$ injective : pas de fusion', 'fixe', 's')
save(fig, '63-062')
