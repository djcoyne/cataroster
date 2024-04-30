# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:59:50 2024

@author: CoyneDa
"""

import players as p
import pandas as pd

roster=pd.DataFrame(columns=['Name','Role','Class','Spec'])
raidbuffs = pd.read_csv('raidbuffs.csv', names=['Buff'])

playerlist = []
Raph = p.Player('Raph')
Dave = p.Player('Dave')
Alan = p.Player('Alan')
Tara = p.Player('Tara')
Chelsea = p.Player('Chelsea')

Raph.add_character('Thurdead','Death Knight','Blood', role='tank')
Dave.add_character('Gwendolock','Warlock','Affliction')
Dave.add_character('Gwenance','Priest','Discipline')
Alan.add_character('Knotadellon','Druid','Restoration')
Tara.add_character('Maureensy','Warlock','Destruction')
Chelsea.add_character('Kittn','Shaman','Elemental')



r = []
r.append(Raph.charlist[0])
r.append(Dave.charlist[0])
r.append(Alan.charlist[0])
r.append(Tara.charlist[0])
r.append(Chelsea.charlist[0])

playerlist.append(Raph)
playerlist.append(Dave)
playerlist.append(Alan)
playerlist.append(Tara)
playerlist.append(Chelsea)


availbuffs = []
for x in r:
    roster.loc[len(roster.index)] =[x.n, x.a.r, x.c, x.s]
    availbuffs.extend(x.a.buffs)
    print(x.n)
    
availbuffs = set(availbuffs)
missbuffs = pd.concat([raidbuffs,pd.DataFrame(availbuffs, columns=['Buff'])]).drop_duplicates(keep=False)

print("Your raid is missing:")
print(missbuffs.to_string(index=False, header=False))
    
