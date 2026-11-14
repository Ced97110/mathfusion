import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def items_on(ax, cx, y0, items, gap=1.0):
    tot = sum(i[2] for i in items) + gap * (len(items) - 1); x = cx - tot / 2; pos = []
    for role, label, w, h, *rest in items:
        shape = rest[0] if rest else 'box'; dash = rest[1] if len(rest) > 1 else False
        if shape == 'disc':
            disc(ax, x + w / 2, y0 + w / 2, w / 2, role, label=label, size='s'); top = y0 + w
        else:
            box(ax, x, y0, w, h, role, label=label, size='m', dash=dash); top = y0 + h
        pos.append((x + w / 2, top)); x += w + gap
    return pos

def balance(ax, cx, yb, L, R, half=28, beam='fixe', pivot='fixe', plate='fixe', lwb=2.2):
    poly(ax, [(cx - 5, yb - 13), (cx + 5, yb - 13), (cx, yb)], pivot)
    line(ax, [(cx - half, yb), (cx + half, yb)], beam, lw=lwb)
    out = []
    for sx, its in ((cx - half, L), (cx + half, R)):
        line(ax, [(sx, yb), (sx, yb + 3)], plate, lw=1.2)
        line(ax, [(sx - 10, yb + 3), (sx + 10, yb + 3)], plate, lw=1.6)
        out.append(items_on(ax, sx, yb + 3.8, its))
    return out

fig, ax = canvas(98)
cx = 44
text(ax, 44, 93, r'$x + 3 = 7$', 'sujet', 'l')
balance(ax, cx, 70, [('sujet', r'$x$', 8, 8, 'box', True), ('fixe', '3', 7, 7)], [('fixe', '7', 9, 9)])
arrow(ax, (44, 54), (44, 40), 'varie')
text(ax, 62, 47, 'retirer 3 des deux côtés', 'varie', 's', ha='center')
balance(ax, cx, 20, [('sujet', r'$x$', 8, 8, 'box', True)], [('resultat', '4', 8, 8)])
text(ax, 44, 3.5, r'$x = 4$', 'resultat', 'l')
save(fig, '16-009')
