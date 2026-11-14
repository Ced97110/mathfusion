import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
names = [r'$e$', '(123)', '(132)']
w, pitch, x0 = 13, 14, 2.5
def cells(y, nk, named):
    for i in range(6):
        lab = names[i] if (i < 3 and i < named) else None
        box(ax, x0 + i * pitch, y, w, 8, 'sujet' if i < nk else 'fixe', label=lab, size='s')
# bloc 1 : K = {e}
text(ax, 2, 58, r'$K=\{e\}$ : 6 classes', 'varie', 's', ha='left', weight='bold')
text(ax, 86, 58, 'non abélien', 'limite', 's', ha='right', weight='bold')
cells(46, 1, 1)
box(ax, x0 - 1, 44.5, w + 2, 11, 'varie', fill=False, dash=True)
# bloc 2 : K = permutations paires
text(ax, 2, 34, r'$K$ = paires : 2 classes', 'varie', 's', ha='left', weight='bold')
text(ax, 86, 34, 'abélien', 'resultat', 's', ha='right', weight='bold')
cells(22, 3, 3)
box(ax, x0 - 1, 20.5, 3 * pitch - 1 + 2, 11, 'varie', fill=False, dash=True)
box(ax, x0 + 3 * pitch - 1, 20.5, 3 * pitch - 1 + 2, 11, 'fixe', fill=False, dash=True)
text(ax, x0 + 1.5 * pitch - 0.5, 16.5, 'classe de $K$', 'varie', 's')
text(ax, x0 + 4.5 * pitch - 0.5, 16.5, 'autre classe', 'fixe', 's')
text(ax, 44, 5, r'$G/K$ abélien $\Rightarrow$ $K\supset G^{\prime}$', 'sujet', 's', weight='bold')
save(fig, '64-064')
