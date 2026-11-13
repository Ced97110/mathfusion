import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
def square(ytop, tl, tr, bl, br, op, lab):
    box(ax, 2, ytop, 34, 12, 'fixe', label=tl, size='s')
    box(ax, 52, ytop, 34, 12, 'fixe', label=tr, size='s')
    box(ax, 2, ytop - 20, 34, 12, 'fixe', label=bl, size='s')
    box(ax, 52, ytop - 20, 34, 12, 'resultat', label=br, size='s')
    arrow(ax, (36.5, ytop + 6), (51.5, ytop + 6), 'varie')
    arrow(ax, (36.5, ytop - 14), (51.5, ytop - 14), 'varie')
    arrow(ax, (19, ytop - 0.5), (19, ytop - 7.5), 'sujet')
    arrow(ax, (69, ytop - 0.5), (69, ytop - 7.5), 'sujet')
    text(ax, 44, ytop + 9.5, op, 'varie', 's')
    text(ax, 14.5, ytop - 4, lab, 'sujet', 's')
text(ax, 44, 94, '$T(v+w)=Tv+Tw$', 'encre', 'm')
square(76, '$v$ = (2 ; 1)\n$w$ = (−1 ; 2)', '$v+w$ = (1 ; 3)',
       '$Tv$ = (−1 ; 2)\n$Tw$ = (−2 ; −1)', '(−3 ; 1)', 'additionner', '$T$')
text(ax, 44, 47, '$T(av)=a(Tv)$, avec $a$ = 3', 'encre', 'm')
square(26, '$v$ = (2 ; 1)', '3$v$ = (6 ; 3)', '$Tv$ = (−1 ; 2)', '(−3 ; 6)', '× 3', '$T$')
save(fig, '57-096')
