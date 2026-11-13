import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def make(code, sides, concl=None, target=None):
    x0 = 4.0
    ext = max(sum(t[1] for t in sd['terms'] if len(t) < 3 or t[2] == '+') for sd in sides)
    s = 66.0 / ext
    def has_sub(sd): return any((len(t) > 2 and t[2] == '-') or t[1] == 0 for t in sd['terms'])
    H = 5 + sum(4.5 + 7 + (9 if has_sub(sd) else 0) + 3 for sd in sides) + (7 if concl else 0)
    fig, ax = canvas(H)
    y = H - 3
    rows = []
    for k, sd in enumerate(sides):
        text(ax, x0, y - 2, sd['title'], 'encre', 's', ha='left')
        yb = y - 4.5 - 7
        cur = 0.0
        role = sd.get('role', 'sujet' if k == 0 else 'autre')
        for t in sd['terms']:
            lab, v = t[0], t[1]
            sign = t[2] if len(t) > 2 else '+'
            r = t[3] if len(t) > 3 else role
            xa = x0 + cur * s
            if v == 0:
                line(ax, [(xa, yb - 1), (xa, yb + 8)], 'varie', lw=1.2)
                text(ax, xa + 1.2, yb - 4, lab, 'varie', 's', ha='left')
            elif sign == '+':
                box(ax, xa, yb, v * s, 7, r); text(ax, xa + 1.8, yb + 3.5, lab, r, 's', ha='left')
                cur += v
            else:
                box(ax, xa - v * s, yb - 9, v * s, 7, 'varie', dash=True); text(ax, xa - v * s + 1.8, yb - 5.5, lab, 'varie', 's', ha='left')
                line(ax, [(xa, yb), (xa, yb - 2)], 'varie', lw=0.8, dash=True)
                cur -= v
        rows.append((yb, yb - (9 if has_sub(sd) else 0)))
        y = yb - (9 if has_sub(sd) else 0) - 3
    if target is not None:
        xt = x0 + target * s
        line(ax, [(xt, rows[0][0] + 8), (xt, rows[-1][0] - 1)], 'resultat', lw=1.0, dash=True)
    if concl:
        text(ax, 44, 3.5, concl, 'resultat', 'm', weight='bold')
    save(fig, code)

make('35-054', [dict(title='gauche : 0,866', terms=[('2 sin 60° sin 30°', 0.866)]), dict(title='droite : 0,866 − 0', terms=[('cos 30°', 0.866), ('− cos 90° = 0', 0)])], concl='même longueur : 0,866', target=0.866)
