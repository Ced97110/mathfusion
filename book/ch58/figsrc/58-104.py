import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 4, 58, 80, 9, 'sujet', label=r'$(2f+5g)(x)=2\,\sin x+5x^2$', size='s')
text(ax, 44, 52, 'au point $x=1$', 'encre', 's')
u = 9.0; x0 = 8; y0 = 28; hb = 10
w1, w2 = 1.68 * u, 5 * u
box(ax, x0, y0, w1, hb, 'sujet', label='1,68', size='s')
box(ax, x0 + w1, y0, w2, hb, 'autre', label='5', size='s')
brace(ax, x0, x0 + w1, y0 + hb, 'sujet', label=r'$2\sin 1$', down=False, depth=1.2)
brace(ax, x0 + w1, x0 + w1 + w2, y0 + hb, 'autre', label=r'$5\times1^2$', down=False, depth=1.2)
brace(ax, x0, x0 + w1 + w2, y0, 'resultat', label=r'$\approx 6{,}68$', down=True, depth=1.6)
text(ax, 44, 6, 'au point $x=0$ : $0+0=0$', 'fixe', 's')
save(fig, '58-104')
