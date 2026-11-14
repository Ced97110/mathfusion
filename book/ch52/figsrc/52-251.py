import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
line(ax, [(44, 12), (44, 78)], 'fixe', dash=True)
def tree(ox, head, leaves, mid, root, wm, wr):
    text(ax, ox + 21.5, 83, head, 'encre', 's')
    xs = [ox + 1, ox + 15, ox + 29]
    for x, s in zip(xs, leaves):
        box(ax, x, 66, 13.5, 8, 'sujet', label=s, size='s')
    c1 = (xs[0] + xs[1] + 13.5) / 2
    box(ax, c1 - wm / 2, 44, wm, 8, 'varie', label=mid, size='s')
    c2 = (c1 + xs[2] + 6.75) / 2
    box(ax, c2 - wr / 2, 18, wr, 8, 'resultat', label=root, size='s')
    arrow(ax, (xs[0] + 6.75, 66), (c1 - 3, 52), 'varie')
    arrow(ax, (xs[1] + 6.75, 66), (c1 + 3, 52), 'varie')
    arrow(ax, (c1, 44), (c2 - 3, 26), 'varie')
    arrow(ax, (xs[2] + 6.75, 66), (c2 + 4, 26), 'varie')
tree(0, 'ordre : 3, 4, 5', ['2 par 3', '0 par 4', '1 par 5'], '8 par 12', '56 par 60', 24, 26)
tree(44.5, 'ordre : 3, 5, 4', ['2 par 3', '1 par 5', '0 par 4'], '11 par 15', '56 par 60', 26, 26)
save(fig, '52-251')
