import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, r'$E=\mathbb{Q}(\sqrt{2}),\ F=\mathbb{Q}$', 'fixe', 'm')
box(ax, 2, 32, 84, 32, 'sujet')
text(ax, 44, 58, r'$\mathrm{Gal}(E/F)$', 'sujet', 'l')
box(ax, 6, 36, 36, 14, 'fixe', label=r'$1$ : ne change rien')
box(ax, 46, 36, 36, 14, 'varie', label=r'$\sigma:\sqrt{2}\mapsto-\sqrt{2}$')
box(ax, 2, 4, 84, 18, 'fixe', label=r'si $E=F=\mathbb{Q}$ : $\{1\}$ seul')
save(fig, '63-032')
