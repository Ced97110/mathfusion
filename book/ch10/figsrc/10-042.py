import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
f=numberline(ax,8,78,34,6,16,1,labels=False,arrow_right=False)
pts=[(7.5,'varie','7,5','150 ÷ 20','erreur −1,5',16),(10,'varie','10','150 ÷ 15','erreur +1',38),(15,'varie','15','150 ÷ 10','erreur +6',71)]
disc(ax,f(9),34,1.5,'sujet'); text(ax,f(9),29.5,'9','sujet','s')
for v,r,l,e,er,ex in pts:
    disc(ax,f(v),34,1.5,r); text(ax,f(v),29.5,l,r,'s'); text(ax,ex,40,e,r,'s'); text(ax,f(v),22,er,r,'s')
line(ax,[(f(9),36),(f(9),46)],'sujet',dash=True); text(ax,f(9),48,'exact : 153 ÷ 17 = 9','sujet','s')
arrow(ax,(14,17),(75,17),'varie'); text(ax,44,13,'le diviseur baisse','varie','s')
save(fig,'10-042')
