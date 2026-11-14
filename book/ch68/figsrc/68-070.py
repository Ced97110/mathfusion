import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
PT = 16
adv = 0.636 * PT * 25.4 / 72
fig, ax = canvas(66)
xc = 32
text(ax, 44, 60, r'$w(x)$ : nombre de 1', 'sujet', 'm')
for y, w in [(46, '10101'), (30, '00011'), (14, '00000')]:
    for i, b in enumerate(w):
        cx = xc + (i - 2) * adv
        if b == '1':
            poly(ax, [(cx - 1.7, y - 3), (cx + 1.7, y - 3), (cx + 1.7, y + 3), (cx - 1.7, y + 3)], 'sujet')
    text(ax, xc, y, w, 'encre', PT)
    text(ax, 68, y, rf'$w={w.count("1")}$', 'resultat', 'l')
    arrow(ax, (52, y), (60, y), 'fixe')
save(fig, '68-070')
