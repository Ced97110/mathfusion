import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="encre", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(80)
k = 6.5
def stack(x0, y0, step):
    caps = {3: '3. adjacent en bas', 4: '4. diviser haut par bas'}
    text(ax, x0 + 2.5 * k, y0 + 2.4 * k + 7, caps[step], 'encre', 's')
    line(ax, [(x0, y0 + 14), (x0 + 16.5, y0 + 14)], 'varie', lw=2.4)
    line(ax, [(x0, y0 + 9), (x0 + 22, y0 + 9)], 'fixe', lw=0.8)
    line(ax, [(x0, y0 + 4), (x0 + 22, y0 + 4)], 'sujet', lw=2.4)
    text(ax, x0 + 19, y0 + 14, '3 opposé', 'varie', 's', ha='left')
    text(ax, x0 + 24, y0 + 4, '4 adjacent', 'sujet', 's', ha='left')
    if step == 4:
        text(ax, x0 + 2.5 * k, y0 - 6, r'$\tan A = 3 \div 4 = 0{,}75$', 'resultat', 'm', weight='bold')

def panel(x0, y0, step):
    if step >= 3:
        return stack(x0, y0, step)
    L = (x0, y0); R = (x0 + 5 * k, y0); P = (x0 + 3.2 * k, y0 + 2.4 * k)
    poly(ax, [L, R, P], 'fixe')
    u1 = (-0.8, -0.6); u2 = (0.6, -0.8)
    sq = [(P[0] + 2 * u1[0], P[1] + 2 * u1[1]), (P[0] + 2 * (u1[0] + u2[0]), P[1] + 2 * (u1[1] + u2[1])), (P[0] + 2 * u2[0], P[1] + 2 * u2[1])]
    line(ax, sq, 'fixe', lw=0.7)
    arc(ax, L, 6, 0, 36.87)
    text(ax, x0 - 2.5, y0 + 0.5, 'A', 'encre', 'm', weight='bold')
    legs = step >= 2
    line(ax, [L, P], 'sujet' if legs else 'fixe', lw=2.4 if legs else 1.2); line(ax, [P, R], 'varie' if legs else 'fixe', lw=2.4 if legs else 1.2)
    line(ax, [L, R], 'fixe', lw=1.0, dash=step >= 2)
    caps = {1: "1. choisir l'angle", 2: "2. écarter l'hypoténuse", 3: '3. adjacent en bas', 4: '4. diviser haut par bas'}
    text(ax, x0 + 2.5 * k, y0 + 2.4 * k + 7, caps[step], 'encre', 's')
    if step == 2:
        text(ax, x0 + 2.5 * k, y0 - 3.5, 'hypoténuse 5 : écartée', 'fixe', 's')
        text(ax, x0 + 1.6 * k - 3.5, y0 + 1.2 * k + 4, '4', 'sujet', 's', weight='bold')
        text(ax, x0 + 4.1 * k + 3, y0 + 1.2 * k + 2.5, '3', 'varie', 's', weight='bold')

panel(8, 50, 1); panel(50, 50, 2); panel(8, 12, 3); panel(50, 12, 4)
save(fig, '25-071')
