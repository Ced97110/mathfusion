import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
PT = 17
adv = 0.636 * PT * 25.4 / 72
fig, ax = canvas(62)
xc = 46
rows = [(46, '0011001', r'$x$', 'sujet'), (30, '0000100', r'$+\ e$', 'varie'), (12, '0011101', r'$=\ x+e$', 'resultat')]
for y, w, lab, role in rows:
    text(ax, xc, y, w, role, PT)
    text(ax, 26, y, lab, role, 'm', ha='right')
line(ax, [(28, 21), (64, 21)], 'fixe')
cx = xc + (4 - 3) * adv
poly(ax, [(cx - adv / 2 - 0.4, 6), (cx + adv / 2 + 0.4, 6), (cx + adv / 2 + 0.4, 52), (cx - adv / 2 - 0.4, 52)], 'varie', fill=False, lw=1.0)
text(ax, cx, 57, 'position 5', 'varie', 's')
text(ax, 75, 30, 'seul ce bit\nchange', 'varie', 's')
save(fig, '68-066')
