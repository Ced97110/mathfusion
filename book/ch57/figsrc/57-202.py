import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, r'même plan, même $v=(2\,;\,0{,}8)$', 'encre', 'm')
text(ax, 53, 50, r'$x^2+1$', 'encre', 's')
text(ax, 75, 50, r'$(x-1)^2$', 'encre', 's')
text(ax, 17, 38, 'quart de tour T', 'sujet', 's')
text(ax, 17, 16, 'cisaillement S', 'autre', 's')
cells = [(53, 33, '(0 ; 0)', 'resultat'), (75, 33, '(1,6 ; −4)', 'limite'),
         (53, 11, '(5,6 ; 1,6)', 'limite'), (75, 11, '(0 ; 0)', 'resultat')]
for cx, cy, t, r in cells:
    box(ax, cx - 10.5, cy, 21, 10, r, label=t, size='s')
text(ax, 44, 4, 'vert : annule v ; rouge : non', 'fixe', 's')
save(fig, '57-202')
