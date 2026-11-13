import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
box(ax,14,64,60,11,'sujet',label=r'reste de $7^{100}$ par 12',size='s')
box(ax,2,24,30,22,'limite',dash=True,label='écrire\n85 chiffres\n: trop long',size='s')
arrow(ax,(26,64),(17,47),'limite',curve=0.1)
ys=[47,33,19,5]
labs=['PGCD(7, 12) = 1',r'$\varphi(12)=4$',r'$100=4\times25$','reste 1']
rl=['sujet','sujet','sujet','resultat']
for y,l,r in zip(ys,labs,rl): box(ax,40,y,46,9,r,label=l,size='s')
arrow(ax,(63,64),(63,56.5),'sujet')
for a,b in zip(ys[:-1],ys[1:]): arrow(ax,(63,a),(63,b+9+0.5),'sujet')
save(fig,'52-226')
