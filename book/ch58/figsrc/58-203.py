import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
# A = (2 1 ; 1 3) : la colonne 1 est η(e_1) = (2, 1), la colonne 2 est η(e_2) = (1, 3)
cw, ch = 10, 9
mx, my = 24, 18
text(ax, 13, my + 9.5, r'$A =$', 'encre', 'l', weight='bold')
cols = [('2', '1', 'sujet', r'$\eta(e_1)$', '(2, 1)'), ('1', '3', 'varie', r'$\eta(e_2)$', '(1, 3)')]
for k, (a, b, role, head, full) in enumerate(cols):
    x = mx + k * 13
    box(ax, x, my + 10, cw, ch, role, label=a, size='m', r=0.5)
    box(ax, x, my, cw, ch, role, label=b, size='m', r=0.5)
    text(ax, x + cw / 2, 43, head, role, 'm')
    arrow(ax, (x + cw / 2, 40), (x + cw / 2, my + 20.5), role, lw=1.0)
    text(ax, x + cw / 2, 10, full, role, 'm')
for xx, d in [(mx - 2.2, 1), (mx + 13 + cw + 2.2, -1)]:
    line(ax, [(xx + d * 1.6, my - 1.2), (xx, my - 1.2), (xx, my + 20.2), (xx + d * 1.6, my + 20.2)], 'encre', lw=1.0)
text(ax, 70, my + 9.5, '2 lignes,\n2 colonnes', 'fixe', 's')
save(fig, '58-203')
