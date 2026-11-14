import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
def bk(cx, cy, w, h, role):
    for sgn in (-1, 1):
        xx = cx + sgn * w
        line(ax, [(xx - sgn * 1.5, cy + h), (xx, cy + h), (xx, cy - h), (xx - sgn * 1.5, cy - h)], role, lw=0.9)
text(ax, 22, 71, 'A', 'sujet', 'l', weight='bold')
text(ax, 66, 71, 'A′', 'autre', 'l', weight='bold')
text(ax, 22, 61, '2  1\n0  2', 'sujet', 'l'); bk(22, 61, 7, 5, 'sujet')
text(ax, 66, 61, '2  0\n0  2', 'autre', 'l'); bk(66, 61, 7, 5, 'autre')
text(ax, 44, 49, 'polynôme caractéristique', 'encre', 's')
box(ax, 5, 36, 34, 10, 'sujet', label='(λ − 2)²', size='m')
text(ax, 44, 41, '=', 'resultat', 'l', weight='bold')
box(ax, 49, 36, 34, 10, 'autre', label='(λ − 2)²', size='m')
text(ax, 44, 29, 'diviseurs élémentaires', 'encre', 's')
box(ax, 5, 16, 34, 10, 'sujet', label='(λ − 2)²', size='m')
text(ax, 44, 21, '≠', 'varie', 'l', weight='bold')
box(ax, 49, 16, 34, 10, 'autre', label='λ − 2 ,  λ − 2', size='m')
text(ax, 44, 6, 'listes ≠ : non semblables', 'encre', 's')
save(fig, '60-188')
