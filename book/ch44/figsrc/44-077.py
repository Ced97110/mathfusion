import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def word(x, y, w, rl, s=6):
    for i, ch in enumerate(w): box(ax, x + i * s, y, s, s, rl, label=ch, size='m', r=0.5)
def empty(x, y): box(ax, x, y, 6, 6, 'fixe', fill=False, dash=True, r=0.5)
for y, left in [(32, True), (12, False)]:
    if left:
        word(6, y, 'ab', 'sujet'); text(ax, 22, y + 3, '+', 'encre', 'l'); empty(28, y)
    else:
        empty(6, y); text(ax, 20, y + 3, '+', 'encre', 'l'); word(26, y, 'ab', 'sujet')
    text(ax, 50, y + 3, '=', 'encre', 'l'); word(58, y, 'ab', 'resultat')
text(ax, 31, 26.5, 'mot vide', 'fixe', 's'); text(ax, 9, 6.5, 'mot vide', 'fixe', 's')
text(ax, 44, 48, '0 lettre : rien ne change', 'resultat', 's')
save(fig, '44-077')
