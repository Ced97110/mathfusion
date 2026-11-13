import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
fig,ax=canvas(64)
text(ax,44,57,'3/4 = 6/8 = 9/12','sujet','l')
for cx,n,d,r in ((20,'3','4','sujet'),(68,'6','8','autre')):
    text(ax,cx,42,n,r,'l'); text(ax,cx,30,d,r,'l'); line(ax,[(cx-4,36),(cx+4,36)],r)
arrow(ax,(26,41),(62,31.5),'varie'); arrow(ax,(26,31),(62,40.5),'autre')
text(ax,26,20,'3 × 8 = 24','varie','m'); text(ax,62,20,'4 × 6 = 24','autre','m')
text(ax,44,10,'24 = 24 : égales','resultat','m')
save(fig,'25-038')
