import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 1, 25, 86, 42, 'resultat', fill=False, dash=True, lw=0.7)
text(ax, 44, 63, r'valent dans tout module ($\mathbb{Z}^2$)', 'resultat', 's', weight='bold')
rows = [(48, r'$0\,v=\mathbf{0}$', r'$0\times(4,7)=(0,0)$'),
        (37, r'$\alpha\mathbf{0}=\mathbf{0}$', r'$5\times(0,0)=(0,0)$'),
        (26.5, r'$(-1)\,v=-v$', r'$(-1)(4,7)=(-4,-7)$')]
for y, a, b in rows:
    box(ax, 4, y, 26, 8.5, 'resultat', label=a, size='s')
    box(ax, 33, y, 51, 8.5, 'sujet', label=b, size='s')
box(ax, 1, 2, 86, 18, 'fixe', fill=False, dash=True, lw=0.7)
box(ax, 4, 6, 26, 8.5, 'fixe', label=r'$\alpha v=\mathbf{0}$', size='s', dash=True)
text(ax, 58, 10, 'demande de diviser :', 'fixe', 's')
text(ax, 58, 5, 'seulement sur un corps', 'fixe', 's', weight='bold')
save(fig, '58-112')
