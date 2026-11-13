import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
s = 4
def sq(x, y, role): box(ax, x, y, s, s, role, r=0.3, lw=0.5)
text(ax, 12, 55, 'départ', 'fixe', 's')
for i in range(1, 5):
    for k in range(i): sq(4 + s * (i - 1), 20 + s * k, 'sujet')
text(ax, 12, 14, '1 + 2 + 3 + 4', 'sujet', 's')
arrow(ax, (21.5, 30), (30.5, 30), 'varie'); arrow(ax, (62, 30), (67, 30), 'varie')
box(ax, 31, 3, 30, 46, 'varie', fill=False)
text(ax, 46, 55, 'étape clé', 'fixe', 's')
for i in range(1, 5):
    x = 36 + s * (i - 1)
    for k in range(i): sq(x, 20 + s * k, 'sujet')
    for k in range(i, 5): sq(x, 20 + s * k, 'varie')
text(ax, 46, 44.5, 'copie identique', 'varie', 's')
brace(ax, 36, 52, 18, 'fixe', r'$n=4$')
text(ax, 56, 30, r'$n+1=5$', 'fixe', 's', rot=90)
text(ax, 44, 8, r'$4\times5=20$', 'fixe', 's')
text(ax, 76, 55, 'arrivée', 'fixe', 's')
box(ax, 68, 20, 16, 20, 'fixe', fill=False, dash=True, lw=0.6, r=0.3)
for i in range(1, 5):
    for k in range(i): sq(68 + s * (i - 1), 20 + s * k, 'sujet')
text(ax, 76, 14, '20 / 2 = 10', 'resultat', 's')
text(ax, 76, 8, r'$n(n+1)/2$', 'resultat', 's')
save(fig, '01-125')
