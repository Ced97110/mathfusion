import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
S = 2.5  # millimètres par unité
text(ax, 44, 85, r'$x=(2;1)$,   $y=(-1;2)$', 'sujet', 's')

def vec(ox, oy, vx, vy, role, lw=1.2):
    arrow(ax, (ox, oy), (ox + S * vx, oy + S * vy), role, lw=lw)

def panel(px, py, title):
    box(ax, px, py, 41, 36, 'fixe', fill=False, lw=0.6)
    text(ax, px + 1.5, py + 32, title, 'sujet', 's', ha='left', weight='bold')
    return py + 10

# règle 1 : doubler une somme
px, py = 2, 47
oy = panel(px, py, 'règle 1 : double d’une somme'); ox = px + 14
vec(ox, oy, 2, 6, 'resultat', 2.2)
vec(ox, oy, 2, 1, 'sujet')
vec(ox, oy, -1, 2, 'autre')
text(ax, ox + 8, oy + 1, '$x$', 'sujet', 's')
text(ax, ox - 4, oy + 6.5, '$y$', 'autre', 's')
text(ax, px + 39, py + 3.5, r'$2(x+y)=(2;6)$', 'resultat', 's', ha='right')

# règle 2 : multiplier par 2 + 3
px, py = 45, 47
oy = panel(px, py, 'règle 2 : multiplier par 2+3'); ox = px + 4
vec(ox, oy, 10, 5, 'resultat', 2.2)
vec(ox, oy, 2, 1, 'sujet')
text(ax, ox + 5.5, oy - 2.5, '$x$', 'sujet', 's')
text(ax, px + 39, py + 3.5, r'$(2+3)x=(10;5)$', 'resultat', 's', ha='right')

# règle 3 : par 3 puis par 2
px, py = 2, 8
oy = panel(px, py, 'règle 3 : par 3, puis par 2'); ox = px + 4
vec(ox, oy, 12, 6, 'resultat', 2.2)
vec(ox, oy, 6, 3, 'varie', 1.4)
text(ax, ox + 12, oy + 9, '$3x$', 'varie', 's')
text(ax, px + 39, py + 3.5, r'$2(3x)=6x=(12;6)$', 'resultat', 's', ha='right')

# règle 4 : multiplier par 1
px, py = 45, 8
oy = panel(px, py, 'règle 4 : multiplier par 1'); ox = px + 4
vec(ox, oy, 2, 1, 'resultat', 2.6)
vec(ox, oy, 2, 1, 'sujet', 1.0)
text(ax, px + 39, py + 3.5, r'$1x=x=(2;1)$', 'resultat', 's', ha='right')
save(fig, '57-088')
