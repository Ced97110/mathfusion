import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, r'$5 \mid 60$ : « 5 divise 60 »', 'resultat', 'l')
f = numberline(ax, 8, 78, 52, 0, 70, step=5, labels=False, arrow_right=False, role='sujet')
disc(ax, f(60), 52, 1.9, 'resultat')
text(ax, f(60), 59, r'$60 = 5 \times 12$', 'resultat', 's')
text(ax, 44, 38, r'$7 \nmid 60$ : « 7 ne divise pas 60 »', 'limite', 'l')
g = numberline(ax, 8, 78, 18, 0, 70, step=7, labels=False, arrow_right=False, role='autre')
for v in (56, 63):
    text(ax, g(v), 12.6, str(v), 'autre', 's')
disc(ax, g(60), 18, 1.9, 'limite')
text(ax, g(60), 24, '60', 'limite', 's')
save(fig, '50-054')
