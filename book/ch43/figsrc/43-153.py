import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 40, 61, 'couples qui font −2', 'encre', 'm')
f = numberline(ax, 6, 58, 14, 0, 4, 1, True, 'fixe', False)
for (a, b), y, lab in [((1, 3), 28, r'$(1,\,3)$'), ((2, 4), 38, r'$(2,\,4)$'), ((0, 2), 48, r'$(0,\,2)$')]:
    disc(ax, f(b), y, 1.4, 'sujet'); arrow(ax, (f(b), y), (f(a), y), 'sujet')
    text(ax, 64, y, lab, 'sujet', 'm', ha='left')
    line(ax, [(f(b), 14), (f(b), y)], 'fixe', lw=0.4, dash=True)
text(ax, 40, 3.5, r'$1+4=3+2$', 'resultat', 'm')
save(fig, '43-153')
