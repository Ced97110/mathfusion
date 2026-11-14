import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$3x+2x=5x$', 'sujet', 'l')
def case(yt, w, lab):
    text(ax, 9, yt + 11, lab, 'encre', 's', ha='left')
    for i in range(5):
        box(ax, 9 + w * i, yt, w, 5, 'sujet' if i < 3 else 'varie'); box(ax, 9 + w * i, yt - 8, w, 5, 'sujet')
    line(ax, [(9 + 5 * w, yt - 8), (9 + 5 * w, yt + 5)], 'resultat', dash=True)
case(48, 4, 'x = 2 : 10 cm et 10 cm'); case(24, 14, 'x = 7 : 35 cm et 35 cm')
text(ax, 44, 6, 'même fin pour tout x', 'resultat', 'm')
save(fig, '15-011')
