import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cw, gap, x0, y0 = 5, 3, 11, 34
text(ax, 44, 57, r'$|G|=12$', 'encre', 'l')
for g in range(3):
    gx = x0 + g * (4 * cw + gap)
    for c in range(4):
        box(ax, gx + c * cw, y0, cw, 6, 'sujet', r=0.5, lw=0.6)
    brace(ax, gx, gx + 4 * cw, y0, 'sujet', r'$p^m=4$' if g == 0 else '4')
xe = x0 + 3 * 4 * cw + 2 * gap
brace(ax, x0, xe, y0 + 6, 'resultat', r'$q=12/4=3$ parts', down=False)
save(fig, '50-034')
