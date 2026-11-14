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

fig, ax = canvas(74)
a = r'$a$'; b = r'$b$'
text(ax, 44, 69, r'$a$ ouvert, $b$ fermé', 'encre', 'm')
y1, y2 = 49, 20
# circuit a ou b
x0 = 22
line(ax, [(x0 - 12, y1), (x0, y1)], 'fixe'); line(ax, [(x0, y1 - 7), (x0, y1 + 7)], 'fixe'); line(ax, [(x0 + 20, y1 - 7), (x0 + 20, y1 + 7)], 'fixe')
for (lab, st), yy in (((a, False), y1 + 7), ((b, True), y1 - 7)):
    line(ax, [(x0, yy), (x0 + 5.5, yy)], 'fixe'); line(ax, [(x0 + 14.5, yy), (x0 + 20, yy)], 'fixe'); sw(ax, x0 + 5.5, yy, lab, st)
line(ax, [(x0 + 20, y1), (x0 + 40, y1)], 'fixe'); lamp(ax, x0 + 43.2, y1, True)
text(ax, 80, y1, 'allumée', 'resultat', 's')
text(ax, 10, y1 + 14, r'$a\vee b$', 'sujet', 'm')
# circuit a seul
line(ax, [(x0 - 12, y2), (x0 + 5.5, y2 - 0)], 'fixe'); sw(ax, x0 + 5.5, y2, a, False)
line(ax, [(x0 + 14.5, y2), (x0 + 40, y2)], 'fixe'); lamp(ax, x0 + 43.2, y2, False)
text(ax, 80, y2, 'éteinte', 'fixe', 's')
text(ax, 10, y2 + 8, r'$a$ seul', 'autre', 'm')
save(fig, '80-462')
