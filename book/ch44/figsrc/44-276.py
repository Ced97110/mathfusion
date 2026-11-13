import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'$D_4$ agit sur les coloriages', 'sujet', 'm', weight='bold')
a = 14.0
for i in range(4):
    x = 4 + i * (a + 8)
    box(ax, x, 18, a, a, 'fixe', r=0.5)
    corners = [(x, 18), (x + a, 18), (x + a, 18 + a), (x, 18 + a)]
    for j, (cx, cy) in enumerate(corners):
        disc(ax, cx, cy, 2.0, 'sujet' if j == i else 'fixe')
    if i < 3: arrow(ax, (x + a + 1.5, 25), (x + a + 6.5, 25), 'varie')
brace(ax, 4, 4 + 3 * (a + 8) + a, 16, 'fixe', r'4 des 16 coloriages')
text(ax, 44, 4, 'un quart de tour change le coloriage', 'varie', 's')
save(fig, '44-276')
