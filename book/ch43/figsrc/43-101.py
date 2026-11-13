import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(110)
def row(ytitle, title, boxes, imgs, links, verdict, role):
    text(ax, 44, ytitle, title, 'encre', 's')
    yb, yi = ytitle - 13, ytitle - 30
    for cx, w, lab in boxes:
        box(ax, cx - w / 2, yb - 5, w, 10, 'sujet', label=lab)
    for cx, lab in imgs:
        disc(ax, cx, yi, 4, role, label=lab)
    for b, i in links:
        arrow(ax, (boxes[b][0], yb - 5), (imgs[i][0] + (boxes[b][0] - imgs[i][0]) * 0.15, yi + 4), 'varie' if role == 'resultat' else 'limite')
    text(ax, 44, yi - 12, verdict, role, 's')
row(104, r'$E = E_f$ : même reste', [(21, 24, r'$\{3,\ 15\}$'), (61, 24, r'$\{4,\ 16\}$')], [(21, '3'), (61, '4')], [(0, 0), (1, 1)], r'$g$ injective', 'resultat')
line(ax, [(3, 57), (85, 57)], 'fixe', lw=0.5, dash=True)
row(52, r'$E$ = égalité (classes seules)', [(11, 16, '{3}'), (31, 16, '{15}'), (51, 16, '{4}'), (71, 16, '{16}')], [(21, '3'), (61, '4')], [(0, 0), (1, 0), (2, 1), (3, 1)], r'$g$ non injective', 'limite')
save(fig, '43-101')
