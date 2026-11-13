import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,2,60,'Temps 1 : les divisions','fixe','m',ha='left')
nums=['2 415','945','525','420','105','0']
bw,gap,x0=11,3.2,3
xs=[x0+i*(bw+gap) for i in range(6)]
for i,(x,n) in enumerate(zip(xs,nums)):
    role='resultat' if n=='105' else ('sujet' if i<2 else 'varie')
    box(ax,x,40,bw,9,role,label=n)
    if i<5: arrow(ax,(x+bw,44.5),(x+bw+gap,44.5),'fixe')
brace(ax,xs[2],xs[5]+bw,50,'varie','restes',down=False)
c=xs[4]+bw/2
text(ax,c,37,'PGCD','resultat','s')
arrow(ax,(c,34.5),(c,21.5),'resultat')
text(ax,2,30,'Temps 2 : la remontée','varie','m',ha='left')
box(ax,2,11,84,10,'resultat',label='105 = 945 × (−5) + 2 415 × 2',size='l')
save(fig,'05-146')
