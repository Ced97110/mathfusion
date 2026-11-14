import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [6, 28, 50, 72]; w = 14; y = 36; h = 12
for x, l, r in zip(xs, [r'$g^{-1}$', r'$h^{-1}$', r'$g$', r'$h$'], ['sujet', 'varie', 'sujet', 'varie']):
    box(ax, x, y, w, h, r, label=l, size='l')
brace(ax, xs[0], xs[3] + w, y + h + 3, 'encre', label=r'le commutateur $(g,h)$', down=False)
text(ax, 22, 21, r'$gh=hg$', 'encre', 'm')
arrow(ax, (22, 18), (22, 12.5), 'resultat')
text(ax, 22, 7, r'$(g,h)=e$', 'resultat', 'm', weight='bold')
text(ax, 66, 21, r'$gh\neq hg$', 'encre', 'm')
arrow(ax, (66, 18), (66, 12.5), 'varie')
text(ax, 66, 7, r'$(g,h)\neq e$', 'varie', 'm', weight='bold')
save(fig, '64-060')
