import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(60)
f = numberline(ax, 14, 50, 12, 0, 2)
line(ax, [(f(0), 4), (f(0), 50)], 'sujet'); line(ax, [(f(1), 4), (f(1), 50)], 'autre')
text(ax, f(0), 54, 'x = 0', 'sujet', 's'); text(ax, f(1), 54, 'x = 1', 'autre', 's')
text(ax, f(0) - 3.2, 32, 'axe vertical', 'sujet', 's', rot=90)
text(ax, f(1) + 3.2, 32, 'tangente en A', 'autre', 's', rot=90)
text(ax, 70, 42, 'aucun point commun', 'limite', 's')
text(ax, 70, 34, 'x = 0 et x = 1', 'limite', 's')
text(ax, 70, 28, 'en même temps : impossible', 'limite', 's')
save(fig, '31-100')
