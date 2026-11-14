import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 2, 64, 84, 10, 'fixe', label='message clair : ALGEBRE')
word = [('A', 0), ('L', 11), ('G', 6), ('E', 4), ('B', 1), ('R', 17), ('E', 4)]
for k, (ch, p) in enumerate(word):
    c = (p + 3) % 26
    out = chr(ord('A') + c)
    x = 2.75 + 12 * k
    box(ax, x, 26, 10.5, 30, 'sujet', label=f'{ch}\n{p}\n+3\n{c}\n{out}')
    arrow(ax, (x + 5.25, 63.5), (x + 5.25, 57), 'fixe', lw=0.8)
    arrow(ax, (x + 5.25, 25.5), (x + 5.25, 18), 'varie', lw=0.8)
box(ax, 2, 6, 84, 10, 'resultat', label='message chiffré : DOJHEUH')
text(ax, 44, 2, 'aucun résultat au-dessus de 25', 'encre', 's')
save(fig, '53-019')
