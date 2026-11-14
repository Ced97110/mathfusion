import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
x0, y0, cw, ch = 34, 20, 16, 12
cells = [['1', r'$\sqrt{3}$'], [r'$\sqrt{2}$', r'$\sqrt{6}$']]
rh = ['1', r'$\sqrt{2}$']; chd = ['1', r'$\sqrt{3}$']
for r in range(2):
    yy = y0 + (1 - r) * ch
    text(ax, x0 - 4, yy + ch / 2, rh[r], 'sujet', 'l')
    for c in range(2):
        box(ax, x0 + c * cw + 0.5, yy + 0.5, cw - 1, ch - 1, 'resultat', label=cells[r][c], size='l')
for c in range(2):
    text(ax, x0 + c * cw + cw / 2, y0 + 2 * ch + 3, chd[c], 'varie', 'l')
text(ax, x0 + cw, y0 + 2 * ch + 9, r'base de $L$ sur $E$', 'varie', 's')
text(ax, 13, y0 + ch, r'base de $E$', 'sujet', 's')
brace(ax, x0, x0 + 2 * cw, y0 - 1, 'resultat', label=r'base de $L$ sur $K$')
text(ax, 44, 5, r'$(1,\ \sqrt{2},\ \sqrt{3},\ \sqrt{6})$', 'resultat', 'm')
text(ax, 77, y0 + ch, '4 produits', 'resultat', 's')
save(fig, '77-113')
