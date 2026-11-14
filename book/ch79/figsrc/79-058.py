import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(90)
text(ax, 44, 85, 'Le signe 0 : le plus petit élément', 'encre', 'm', weight='bold')
text(ax, 44, 79, 'ce n’est pas le nombre zéro', 'fixe', 's')
for cx, t, o, lab in ((22, 'diviseurs de 60', 'les 11 autres', '1'), (66, 'parties de 3 stylos', 'les 7 autres', r'$\emptyset$')):
    text(ax, cx, 69, t, 'fixe', 's')
    box(ax, cx - 18, 46, 36, 12, 'fixe', label=o)
    arrow(ax, (cx, 27.5), (cx, 45.5), 'fixe')
    text(ax, cx + 11, 36, r'$\leq$ chacun', 'fixe', 's')
    N(ax, cx, 22, lab, 'sujet', 5, 'l')
text(ax, 22, 10, r'$0=1$', 'sujet', 'l'); text(ax, 66, 10, r'$0=\emptyset$', 'sujet', 'l')
save(fig, '79-058')
