import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 62, 'somme sur les 4 sous-cartes', 'fixe', 's')
cols = [11, 33, 55, 77]
heads = ['aucune effacée', 'A|B effacée', 'B|C effacée', 'les deux']
shapes = [[(5, 0), (5, 0), (5, 0)], [(11, 1), (5, 0)], [(5, 0), (11, 1)], [(17, 1)]]
terms = [(r'$+k^3$', 'sujet'), (r'$-k^2$', 'varie'), (r'$-k^2$', 'varie'), (r'$+k$', 'sujet')]
for c, h, sh, (t, role) in zip(cols, heads, shapes, terms):
    text(ax, c, 52, h, 'fixe', 's')
    tot = sum(w for w, _ in sh) + (len(sh) - 1) * 1; x = c - tot / 2
    for w, m in sh: box(ax, x, 36, w, 8, 'varie' if m else 'sujet', r=0.5); x += w + 1
    text(ax, c, 26, t, role, 'l')
text(ax, 44, 10, r'$k=2$ : 8 − 4 − 4 + 2 = 2', 'resultat', 'm')
save(fig, '80-382')
