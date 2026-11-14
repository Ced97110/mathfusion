import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def panel(y, vals, c, res):
    f = numberline(ax, 4, 50, y, c - 4, c + 4, 1, labels=True, arrow_right=False, every=2)
    for v in vals:
        disc(ax, f(v), y, 1.5, 'sujet'); text(ax, f(v), y + 5, str(v), 'sujet', 's')
    disc(ax, f(c), y, 2.2, 'autre')
    text(ax, f(c), y + 10, r'$c$ = %d' % c, 'autre', 'm', weight='bold')
    text(ax, 56, y, r'4 $\times$ $c$ = %s' % res, 'resultat', 'm', ha='left')
panel(40, (48, 49, 51, 52), 50, '200')
panel(12, (98, 99, 101, 102), 100, '400')
text(ax, 44, 57, r'un seul nom $c$ pour deux valeurs', 'autre', 'm')
save(fig, '10-011')
