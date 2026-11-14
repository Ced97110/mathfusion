import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
sizes = [4, 4, 4, 2, 1, 1]
roles = ['sujet', 'sujet', 'sujet', 'autre', 'resultat', 'resultat']
cw, gap, h, y = 4.2, 2.5, 6, 30
x = (88 - (16 * cw + 5 * gap)) / 2
spans = []
for n, r in zip(sizes, roles):
    for k in range(n):
        poly(ax, [(x + k * cw, y), (x + (k + 1) * cw, y), (x + (k + 1) * cw, y + h), (x + k * cw, y + h)], r)
    spans.append((x, x + n * cw))
    x += n * cw + gap
for (a, b), n in zip(spans, sizes):
    brace(ax, a, b, y - 1, 'fixe', label=str(n))
text(ax, (spans[4][0] + spans[4][1]) / 2, y + h + 3, r'$x$', 'resultat', 's')
text(ax, (spans[5][0] + spans[5][1]) / 2, y + h + 3, r'$x+1$', 'resultat', 's')
brace(ax, spans[0][0], spans[-1][1], 18, 'fixe', label='4 + 4 + 4 + 2 + 1 + 1 = 16')
text(ax, 44, 55, r'$x^{16}-x$ en 6 facteurs', 'encre', 'm')
text(ax, 44, 47, 'case : racine ; chiffre : degré', 'fixe', 's')
save(fig, '67-190')
