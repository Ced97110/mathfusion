import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(70)
h = 40; hw = h * math.tan(math.radians(30)); ax_, ay = 44, 58; by = 18
poly(ax, [(ax_, ay), (ax_ - hw, by), (ax_, by)], 'sujet')
poly(ax, [(ax_, ay), (ax_ + hw, by), (ax_, by)], 'sujet')
line(ax, [(ax_, ay), (ax_, by)], 'fixe')
text(ax, ax_ - 7.5, ay - 26, 'A = 30°', 'sujet', 's'); text(ax, ax_ + 7.5, ay - 26, 'B = 30°', 'sujet', 's')
text(ax, ax_ - hw / 2, by - 3.5, r'$x$', 'sujet', 'm'); text(ax, ax_ + hw / 2, by - 3.5, r'$y$', 'sujet', 'm')
text(ax, 44, 8, r'$x=y$ : 2 triangles identiques', 'resultat', 'm')
save(fig, '34-148')
