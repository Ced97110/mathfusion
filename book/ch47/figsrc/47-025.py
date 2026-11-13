import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pt(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def sq(ax, cx, cy, s, role='fixe'):
    poly(ax, [(cx-s, cy-s), (cx+s, cy-s), (cx+s, cy+s), (cx-s, cy+s)], role)
def grid(ax, x0, y0, cw, ch, gap, rows, cols, roles):
    cells = []
    for i in range(rows):
        for j in range(cols):
            x = x0 + j*(cw+gap); y = y0 + (rows-1-i)*(ch+gap)
            box(ax, x, y, cw, ch, roles[i], r=0.6)
            cells.append((x, y))
    return cells

fig, ax = canvas(72)
parts = [(8, r'$G x = \{$', 'sujet'), (36, r'$\alpha(x)$', 'sujet'), (51, r'$\mid$', 'fixe'), (67, r'$\alpha \in G$', 'varie'), (80, r'$\}$', 'sujet')]
for x, t, r in parts: text(ax, x, 62, t, r, 'l')
text(ax, 36, 50, "l'image de x", 'sujet', 's')
text(ax, 51, 54, 'tels que', 'fixe', 's')
text(ax, 67, 50, 'chaque α de G', 'varie', 's')
brace(ax, 28, 44, 57, 'sujet', down=True, depth=1.2)
brace(ax, 58, 76, 57, 'varie', down=True, depth=1.2)
text(ax, 44, 40, 'sur le cas de l\'horloge', 'fixe', 's')
box(ax, 2, 12, 16, 12, 'sujet', label=r'$x = 1$', size='s')
box(ax, 28, 12, 32, 12, 'varie', label='+0, +3, +6, +9', size='s')
box(ax, 68, 12, 18, 12, 'resultat', label='{1, 4, 7, 10}', size='s')
arrow(ax, (18.8, 18), (27.2, 18), 'fixe'); arrow(ax, (60.8, 18), (67.2, 18), 'fixe')
text(ax, 10, 29, '1. choisir', 'sujet', 's'); text(ax, 44, 29, '2. appliquer chaque', 'varie', 's'); text(ax, 77, 29, '3. rassembler', 'resultat', 's')
save(fig, '47-025')
