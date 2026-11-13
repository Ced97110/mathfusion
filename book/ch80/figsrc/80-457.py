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

fig, ax = canvas(56); yc = 24
a = r'$a$'; b = r'$b$'; bp = r"$b'$"
X = [6, 30, 54]
specs = [((a, False), (b, False)), ((a, False), (bp, True)), ((a, False), (b, False))]
line(ax, [(2, yc), (2.5, yc)], 'fixe')
for i, (t, u) in enumerate(specs): blk(ax, X[i], yc, t, u, 'bloc %d' % (i + 1))
line(ax, [(77.5, yc), (79.8, yc)], 'fixe'); lamp(ax, 83, yc, False)
text(ax, 82, yc - 7, 'éteinte', 'fixe', 's')
text(ax, 44, 51, r'ligne 1 : $a$ et $b$ ouverts', 'encre', 'm')
text(ax, 44, 5, 'bloc 1 coupé : rien ne passe', 'limite', 's')
save(fig, '80-457')
