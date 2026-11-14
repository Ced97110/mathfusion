import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lens(cx1, cx2, cy, r):
    a = math.acos((cx2 - cx1) / (2 * r)); n = 24
    right = [(cx1 + r * math.cos(-a + 2 * a * i / n), cy + r * math.sin(-a + 2 * a * i / n)) for i in range(n + 1)]
    left = [(cx2 + r * math.cos(math.pi - a + 2 * a * i / n), cy + r * math.sin(math.pi - a + 2 * a * i / n)) for i in range(n + 1)]
    return right + left
fig, ax = canvas(74)
text(ax, 44, 69, r'$A \cup B$', 'sujet', 'xl'); text(ax, 44, 62, 'lu « A union B »', 'sujet', 's')
disc(ax, 33, 40, 16, 'sujet'); disc(ax, 55, 40, 16, 'sujet')
poly(ax, lens(33, 55, 40, 16), 'sujet')
text(ax, 24, 40, 'gourde', 'sujet', 's'); text(ax, 44, 40, 'carte', 'sujet', 's'); text(ax, 65, 40, 'lampe', 'sujet', 's')
text(ax, 24, 53, r'$A$', 'fixe', 'm'); text(ax, 64, 53, r'$B$', 'fixe', 'm')
text(ax, 44, 17, r'$x \in A \cup B$', 'sujet', 'l')
text(ax, 44, 9, r'dans $A$, ou dans $B$, ou les deux', 'resultat', 's')
save(fig, '42-112')
