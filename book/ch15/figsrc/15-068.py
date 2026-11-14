import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
for cx, expr, e, tot, dash in [(22, r'$4x^{2}y^{5}$', ('2', '5'), r'$2+5=7$', False), (66, r'$5xy$', ('1', '1'), r'$1+1=2$', True)]:
    text(ax, cx, 63, expr, 'encre', 'xl')
    box(ax, cx - 14, 40, 12, 9, 'sujet', dash=dash, label=e[0], size='l')
    box(ax, cx + 2, 40, 12, 9, 'autre', dash=dash, label=e[1], size='l')
    arrow(ax, (cx - 8, 58), (cx - 8, 50), 'sujet'); arrow(ax, (cx + 8, 58), (cx + 8, 50), 'autre')
    arrow(ax, (cx, 39), (cx, 31), 'resultat')
    box(ax, cx - 14, 20, 28, 10, 'resultat', label=tot, size='m')
text(ax, 22, 13, 'degré 7', 'resultat', 'm'); text(ax, 66, 13, 'degré 2', 'resultat', 'm')
text(ax, 44, 5, 'exposant caché = 1 (tirets)', 'fixe', 's')
save(fig, '15-068')
