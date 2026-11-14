import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def sw(ax, x, y, lab, closed=None, w=9):
    role = 'resultat' if closed else ('fixe' if closed is False else 'sujet')
    for xx in (x, x + w): disc(ax, xx, y, 0.9, role)
    tip = (x + w, y) if closed else (x + w - 1.8, y + 4.2)
    line(ax, [(x, y), tip], role, lw=1.1)
    text(ax, x + w / 2, y + 7.0, lab, role, 'm')

def blk(ax, x0, yc, top, bot, name=None, known=True):
    line(ax, [(x0, yc - 7), (x0, yc + 7)], 'fixe'); line(ax, [(x0 + 20, yc - 7), (x0 + 20, yc + 7)], 'fixe')
    for (lab, st), yy in ((top, yc + 7), (bot, yc - 7)):
        line(ax, [(x0, yy), (x0 + 5.5, yy)], 'fixe'); line(ax, [(x0 + 14.5, yy), (x0 + 20, yy)], 'fixe')
        sw(ax, x0 + 5.5, yy, lab, st if known else None)
    line(ax, [(x0 - 3.5, yc), (x0, yc)], 'fixe'); line(ax, [(x0 + 20, yc), (x0 + 23.5, yc)], 'fixe')
    role = 'fixe'
    if known: role = 'resultat' if (top[1] or bot[1]) else 'limite'
    box(ax, x0 - 1.8, yc - 11, 23.6, 29, role, fill=False, lw=0.7, dash=True)
    if name: text(ax, x0 + 10, yc + 20.5, name, role, 's')
    return role

def lamp(ax, x, y, on):
    disc(ax, x, y, 3.2, 'resultat' if on else 'fixe')

fig, ax = canvas(62)
a = r'$a$'; b = r'$b$'; bp = r"$b'$"
text(ax, 44, 57, r"$a$ et $b$ ouverts, $b'$ fermé", 'encre', 'm')
xl, xr = 14, 62
ys = [42, 28, 14]
line(ax, [(xl, ys[0]), (xl, ys[2])], 'fixe'); line(ax, [(xr, ys[0]), (xr, ys[2])], 'fixe')
line(ax, [(4, ys[1]), (xl, ys[1])], 'fixe'); line(ax, [(xr, ys[1]), (xr + 8, ys[1])], 'fixe')
for (lab, st), yy in (((a, False), ys[0]), ((b, False), ys[1]), ((bp, True), ys[2])):
    line(ax, [(xl, yy), (xl + 11, yy)], 'fixe'); sw(ax, xl + 11, yy, lab, st); line(ax, [(xl + 20, yy), (xr, yy)], 'fixe')
lamp(ax, xr + 11.2, ys[1], True)
text(ax, 80, ys[1] + 7, 'allumée', 'resultat', 's')
text(ax, 44, 4, r"$a\vee b\vee b' = I$ : un fil", 'resultat', 's')
save(fig, '80-464')
