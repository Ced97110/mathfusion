import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$\mathrm{Aut}(E)$ : un seul groupe', 'sujet', 'm', weight='bold')
xs = [14, 32, 50, 68]
names = [r'$\sigma$', '1', r'$\tau$', r'$\sigma\tau$']
roles = ['sujet', 'sujet', 'sujet', 'fixe']
for x, n, r in zip(xs, names, roles):
    disc(ax, x, 36, 5, r, label=n)
brace(ax, 27, 55, 43, 'resultat', label=r'$G(E/F)$ , $F=\mathbb{Q}(\sqrt{2})$', down=False)
brace(ax, 9, 37, 29, 'autre', label=r'$G(E/F)$ , $F=\mathbb{Q}(\sqrt{3})$', down=True)
text(ax, 44, 12, r'$F$ change : la partie change', 'fixe', 's')
save(fig, '63-049')
