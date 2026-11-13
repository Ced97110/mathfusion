import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import re
nb=lambda s: re.sub(r'(?<=\d) (?=\d)', ' ', s)

fig,ax=canvas(66)
line(ax,[(10,52),(18,60)],'encre',lw=1.4); line(ax,[(10,60),(18,52)],'encre',lw=1.4)
line(ax,[(70,52),(78,60)],'encre',lw=1.4)
import math
line(ax,[(78-8*t+0.8*math.sin(math.pi*t),52+8*t) for t in [i/6 for i in range(7)]][::-1] if False else [(70+8*t+0.8*math.sin(math.pi*t),60-8*t) for t in [i/6 for i in range(7)]],'encre',lw=1.4)
text(ax,14,48,'signe fois','encre','s'); text(ax,74,48,'lettre x','encre','s')
text(ax,44,56,'se ressemblent','limite','s')
text(ax,20,32,r'3 $\times$ $x$','limite','l'); text(ax,22,25,'× ou x ? lecture douteuse','limite','s')
arrow(ax,(36,32),(52,32),'varie'); text(ax,44,36,'on enlève ×','varie','s')
text(ax,66,32,r'$\mathbf{3}x$','sujet','l'); text(ax,66,25,'trois fois x','sujet','s')
text(ax,44,12,'3 × 5 : sans lettre, clair','fixe','s')
save(fig,'03-026')
