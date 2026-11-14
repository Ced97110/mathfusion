import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
y0 = 22
D = {'4':(22,y0),'12':(8,y0+22),'20':(36,y0+22),'60':(22,y0+44)}
line(ax, [D['4'], D['12']], 'varie', lw=2.0); line(ax, [D['20'], D['60']], 'varie', lw=2.0)
line(ax, [D['4'], D['20']], 'fixe'); line(ax, [D['12'], D['60']], 'fixe')
for k,(x,yy) in D.items(): disc(ax, x, yy, 4.5, {'4':'fixe','60':'fixe','12':'sujet','20':'autre'}[k], label=k)
text(ax, 22, 74, 'diviseurs : implication vraie', 'resultat', 's')
text(ax, 22, 11, r'isomorphes : $\times3$ chacun', 'varie', 's')
P = {'0':(66,y0),'u':(54,y0+14),'v':(54,y0+30),'1':(66,y0+44),'w':(78,y0+22)}
line(ax, [P['0'],P['u']], 'limite', lw=2.0); line(ax, [P['u'],P['v']], 'limite', lw=2.0)
line(ax, [P['v'],P['1']], 'resultat', lw=2.0); line(ax, [P['w'],P['1']], 'resultat', lw=2.0)
line(ax, [P['0'],P['w']], 'fixe')
for k,(x,yy) in P.items(): disc(ax, x, yy, 3.6, {'0':'fixe','1':'fixe','u':'fixe','v':'sujet','w':'autre'}[k], label=k)
text(ax, 66, 74, 'pentagone : implication fausse', 'limite', 's')
text(ax, 66, 11, r'ici 1 recouvre $v$ et $w$', 'resultat', 's')
text(ax, 66, 5, r'mais $v$ ne recouvre pas 0', 'limite', 's')
for _p in ax.patches:
    if isinstance(_p, Circle): _p.set_zorder(3.5)
save(fig, '79-180')
