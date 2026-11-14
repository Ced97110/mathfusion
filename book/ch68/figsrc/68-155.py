import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
word = '0011011'
circles = {'A': [4, 5, 6, 7], 'B': [2, 3, 6, 7], 'C': [1, 3, 5, 7]}
w, h, x0 = 8, 6.5, 12
text(ax, 44, 76, r'mot reçu $r$ = 0011011', 'encre', 'm')
for p in range(1, 8):
    text(ax, x0 + (p - 0.5) * w, 66, str(p), 'fixe', 's')
syn = []
for i, (name, pos) in enumerate(circles.items()):
    y = 52 - i * h
    text(ax, 6, y + h / 2, name, 'sujet', 'm')
    for p in range(1, 8):
        x = x0 + (p - 1) * w
        if p in pos:
            box(ax, x, y, w, h, 'sujet', label=word[p - 1])
        else:
            ax.add_patch(Rectangle((x, y), w, h, ec=COL['fixe'], fc=FILL['fixe'], lw=0.6, zorder=2))
    s = sum(int(word[p - 1]) for p in pos)
    syn.append(s % 2)
    text(ax, x0 + 7 * w + 2, y + h / 2, rf'${s} \to {s % 2}$', 'varie', 's', ha='left')
text(ax, 44, 26, 'cercle impair : 1, pair : 0', 'encre', 's')
text(ax, 44, 16, rf'$Hr = ({syn[0]}, {syn[1]}, {syn[2]})$', 'resultat', 'l')
save(fig, '68-155')
