import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
cx = [18, 42, 66]
w = 22
rows = [['3²', '3³', '3⁴'], ['1', '5²', '5⁴'], ['1', '7', '7³']]
ys = [68, 57, 46]
text(ax, 44, 86, 'lignes : premiers 3, 5, 7', 'sujet', 's')
for y, row in zip(ys, rows):
    for x, v in zip(cx, row):
        box(ax, x, y, w - 2, 8, 'fixe' if v == '1' else 'sujet', label=v)
prods = ['3²\n$d_1=9$', '3³×5²×7\n$d_2=4\\ 725$', '3⁴×5⁴×7³\n$d_3=17\\ 364\\ 375$']
for x, p in zip(cx, prods):
    arrow(ax, (x + (w - 2) / 2, 45), (x + (w - 2) / 2, 35), 'varie')
    box(ax, x - 1, 18, w, 16, 'resultat', label=p, size='s')
text(ax, 44, 8, r'$d_1$ divise $d_2$ divise $d_3$', 'resultat', 's')
save(fig, '60-093')
