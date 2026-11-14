import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
labs = [r'$\sqrt[3]{2}$', r'$j\sqrt[3]{2}$', r'$j^2\sqrt[3]{2}$']
def panel(cx, cy, present, roles, head):
    n = 90
    pts = [(cx + 11 * math.cos(math.radians(t)), cy + 11 * math.sin(math.radians(t))) for t in range(0, 361, 5)]
    line(ax, pts, 'fixe', lw=0.5)
    for k in range(3):
        a = math.radians(120 * k)
        x, y = cx + 11 * math.cos(a), cy + 11 * math.sin(a)
        disc(ax, x, y, 2.2, roles[k], fill=present[k])
        text(ax, cx + 18 * math.cos(a), cy + 18 * math.sin(a), labs[k], roles[k], 's')
    text(ax, cx, 62, head, 'encre', 'm')
panel(16, 34, (True, False, False), ('sujet', 'fixe', 'fixe'), 'tour de départ')
panel(62, 34, (True, True, True), ('sujet', 'varie', 'varie'), 'tour normale')
arrow(ax, (36, 34), (48, 34), 'varie')
text(ax, 42, 40, '+ images', 'varie', 's')
save(fig, '64-163')
