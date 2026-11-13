import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u, y0 = 2.5, 22
for cx, wd, ht, role, a, b, c in [(14, 5, 3, 'sujet', '3 sur 5', '3 ÷ 5 = 0,6', 'resultat'),
                                 (44, 10, 6, 'sujet', '6 sur 10', '6 ÷ 10 = 0,6', 'resultat'),
                                 (76, 5, 6, 'limite', '6 sur 5', '6 ÷ 5 = 1,2', 'limite')]:
    box(ax, cx - wd * u / 2, y0, wd * u, ht * u, role, r=0.3)
    text(ax, cx, y0 - 4, a, role, 's')
    text(ax, cx, y0 - 10, b, c, 's')
text(ax, 29, y0 + 4, '=', 'resultat', 'l', weight='bold')
text(ax, 60, y0 + 4, '≠', 'limite', 'l', weight='bold')
text(ax, 29, 46, 'même forme', 'resultat', 's'); text(ax, 76, 46, 'forme changée', 'limite', 's')
save(fig, '09-009')
