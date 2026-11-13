import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def strip(y, n, k):
    w = 72.0 / n
    for i in range(n):
        r = 'sujet' if i < k else 'fixe'
        ax.add_patch(Rectangle((8 + i * w, y), w, 6, ec=COL[r], fc=FILL[r], lw=0.25 if n == 100 else 0.5, zorder=2))
text(ax, 44, 58, '20 questions : 7 réussies', 'sujet', 'm')
strip(48, 20, 7)
text(ax, 44, 39, '= même part du test', 'resultat', 'm')
strip(27, 100, 35)
text(ax, 44, 21, '100 questions : 35 réussies', 'sujet', 'm')
box(ax, 14, 4, 28, 10, 'resultat', label=r'$\frac{7}{20}=\frac{35}{100}$')
box(ax, 50, 4, 24, 10, 'resultat', label='35 %')
text(ax, 46, 9, '=', 'encre', 'm')
save(fig, '09-066')
