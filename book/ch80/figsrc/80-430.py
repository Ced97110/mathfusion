import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def circuit(ax, y0, title, branches, lamp_on, link=False):
    ys = [y0 + 21, y0 + 8]; xl, xr = 8, 56; ym = (ys[0] + ys[1]) / 2
    rl = 'resultat' if lamp_on else 'fixe'
    text(ax, 3, y0 + 28.8, title, 'encre', 's', ha='left')
    for y, br in zip(ys, branches):
        ok = all((e[0] == 'w') or (e[0] == 's' and e[2]) for e in br)
        role = 'resultat' if ok else 'fixe'
        cxs = [32] if len(br) == 1 else [22, 44]
        prev = xl
        for cx, e in zip(cxs, br):
            if e[0] == 'w':
                l, r = cx - 7, cx + 7
                line(ax, [(prev, y), (l, y)], role); line(ax, [(l, y), (r, y)], role, lw=1.4)
                text(ax, cx, y + 3, e[1], role, 's')
            elif e[0] == 's':
                l, r = cx - 7, cx + 7
                line(ax, [(prev, y), (l, y)], role)
                end = (r, y) if e[2] else (cx + 5, y + 5.5)
                line(ax, [(l, y), end], role, lw=1.2)
                disc(ax, l, y, 0.7, role); disc(ax, r, y, 0.7, role)
                text(ax, cx, y - 3.3, e[1], role, 's')
            else:
                l, r = cx - 5, cx + 5
                line(ax, [(prev, y), (l, y)], role)
                box(ax, l, y - 3.5, 10, 7, 'fixe', label=e[1], size='s', dash=True)
            prev = r
        line(ax, [(prev, y), (xr, y)], role)
    if link: line(ax, [(36, ys[0]), (36, ys[1])], 'varie', dash=True)
    line(ax, [(xl, ys[0]), (xl, ys[1])], rl); line(ax, [(xr, ys[0]), (xr, ys[1])], rl)
    line(ax, [(3, ym), (xl, ym)], rl); line(ax, [(xr, ym), (63.8, ym)], rl)
    disc(ax, 68, ym, 4.2, rl)
    text(ax, 68, ym - 7.5, 'allumée' if lamp_on else 'éteinte', rl, 's')

fig, ax = canvas(68)
circuit(ax, 36, r"$a$ fermé (les deux)", [[('s', 'a', True)], [('s', 'a', True)]], True, link=True)
circuit(ax, 2, r"$a$ ouvert (les deux)", [[('s', 'a', False)], [('s', 'a', False)]], False, link=True)
save(fig, '80-430')
