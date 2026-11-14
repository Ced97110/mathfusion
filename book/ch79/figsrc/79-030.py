import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, '≤ veut dire : divise', 'fixe', 's')
for cx, head, a, b, c, ok in [(22, '4 et 12', '4 ≤ 12 : oui', '4 ≠ 12 : oui', '4 < 12 : vrai', True), (66, '4 et 4', '4 ≤ 4 : oui', '4 ≠ 4 : non', '4 < 4 : faux', False)]:
    text(ax, cx, 58, head, 'sujet', 'm', weight='bold')
    box(ax, cx - 17, 44, 34, 8, 'resultat', label=a, size='s'); text(ax, cx, 41, 'et', 'fixe', 's')
    box(ax, cx - 17, 30, 34, 8, 'resultat' if ok else 'limite', label=b, size='s')
    arrow(ax, (cx, 30), (cx, 21.5), 'fixe')
    box(ax, cx - 17, 12, 34, 9, 'resultat' if ok else 'limite', label=c, size='s', weight='bold')
save(fig, '79-030')
