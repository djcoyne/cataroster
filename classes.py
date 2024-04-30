""" This file contains the class and spec information for WoW Cata Classic
"""

""" 
Death Knights
"""
class DeathKnight:
  def __init__(self):
    self.c = 'C41E3A'
    self.buffs = ['+Strength and Agility','-20% Melee Attack Speed Debuff','-Casting Speed Debuff']

class DKBlood(DeathKnight):
  def __init__(self, role='tank'):
    super().__init__()
    self.r = role
    self.sb = ['+10% to Attack Power','-10% Physical Damage Dealt Debuff']
    self.buffs.extend(sb)

class DKFrost(DeathKnight):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+10% to Melee Attack Speed', '+4% Physical Damage Taken Debuff']
    self.buffs.extend(sb)

class DKUnholy(DeathKnight):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+8% All Magic Damage Taken Debuff']
    self.buffs.extend(sb)
  
"""
Druids
"""
class Druid:
  def __init__(self):
    self.c = 'FF7C0A'
    self.buffs = ['+5% to Strength, Agility, Intellect, and Stamina','-Armor Debuff','Combat Resurrection','Major Mana Replenishment']

class DrFeral(Druid):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+5% to Critical Strike Chance','+30% Bleed Damage Taken Debuff','-20% Melee Attack Speed Debuff','-10% Physical Damage Dealt Debuff']
    self.buffs.extend(sb)

class DrBalance(Druid):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+5% to Spell Haste','+8% All Magic Damage Taken Debuff']
    self.buffs.extend(sb)

class DrResto(Druid):
  def __init__(self, role='heal'):
    super().__init__()
    self.r = role
    self.sb = ['Replenishment']
    self.buffs.extend(sb)

"""
Hunters
"""
class Hunter:
  def __init__(self):
    self.c = 'AAD372'
    self.buffs = ['+Nature Resistance','-Healing Effectiveness Debuff']
    
class HBM(Hunter):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+3% to All Damage']
    self.buffs.extend(sb)

class HMarks(Hunter):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+10% to Attack Power']
    self.buffs.extend(sb)

class HSurv(Hunter):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+10% to Melee Attack Speed']
    self.buffs.extend(sb)

"""
Mages
"""
class Mage:
  def __init__(self):
    self.c = '3FC7EB'
    self.buffs = ['Bloodlust/Heroism/Time Warp','Minor Spell Power (6%)','+Max Mana']

class MArcane(Mage):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+3% to All Damage','-Casting Speed Debuff']
    self.buffs.extend(sb)   

class MFire(Mage):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+5% Critical Strike Chance for Spells Debuff']
    self.buffs.extend(sb)

class MFrost(Mage):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['Replenishment']
    self.buffs.extend(sb)

"""
Paladins
"""
class Paladin:
  def __init__(self):
    self.c = 'F48CBA'
    self.buffs = ['+10% to Attack Power','+5% to Strength, Agility, Intellect, and Stamina','+Armor','+Fire Resistance','+Frost Resistance','+Shadow Resistance','Spell Pushback Protection','Mana Per 5 (Mp5)','-20% Melee Attack Speed Debuff']

class PalProt(Paladin):
  def __init__(self, role='tank'):
    super().__init__()
    self.r = role
    self.sb = ['-10% Physical Damage Dealt Debuff']
    self.buffs.extend(sb)

class PalHoly(Paladin):
  def __init__(self, role='heal'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class PalRet(Paladin):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+3% to All Damage','Replenishment']
    self.buffs.extend(sb)

"""
Priests
"""
class Priest:
  def __init__(self):
    self.c = 'FFFFFF'
    self.buffs = ['+Stamina','+Shadow Resistance','Major Mana Replenishment']

class PrDisc(Priest):
  def __init__(self, role='heal'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class PrHoly(Priest):
  def __init__(self, role='heal'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class PrShadow(Priest):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+5% to Spell Haste','-Healing Effectiveness Debuff','Replenishment']
    self.buffs.extend(sb)

"""
Rogues
"""
class Rogue:
  def __init__(self):
    self.c = 'FFF468'
    self.buffs = ['-Armor Debuff','-Healing Effectiveness Debuff','-Casting Speed Debuff']

class RAss(Rogue):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+8% All Magic Damage Taken Debuff']
    self.buffs.extend(sb)

class RCombat(Rogue):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+4% Physical Damage Taken Debuff']
    self.buffs.extend(sb)

class RSubtlety(Rogue):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+5% to Critical Strike Chance','+30% Bleed Damage Taken Debuff']
    self.buffs.extend(sb)

"""
Shamans
"""
class Shaman:
  def __init__(self):
    self.c = '0070DD'
    self.buffs = ['Bloodlust/Heroism/Time Warp','+10% to Melee Attack Speed','+5% to Spell Haste', 'Minor Spell Power (6%)','+Strength and Agility','+Armor','+Fire Resistance','+Frost Resistance','+Nature Resistance','Spell Pushback Protection','Mana Per 5 (Mp5)','-20% Melee Attack Speed Debuff']

class SEnhance(Shaman):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+10% to Attack Power']
    self.buffs.extend(sb)

class SElemental(Shaman):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+5% to Critical Strike Chance','Major Spellpower (10%)']
    self.buffs.extend(sb)

class SResto(Shaman):
  def __init__(self, role='heal'):
    super().__init__()
    self.r = role
    self.sb = ['Major Mana Replenishment']
    self.buffs.extend(sb)

"""
Warlocks
"""
class Warlock:
  def __init__(self):
    self.c = '8788EE'
    self.buffs = ['Combat Resurrection','+8% All Magic Damage Taken Debuff','-10% Physical Damage Dealt Debuff','-Casting Speed Debuff']

class WkAff(Warlock):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+Max Mana','Mana Per 5 (Mp5)']
    self.buffs.extend(sb)

class WkDemo(Warlock):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['Major Spell Power (10%)','-Healing Effectiveness Debuff']
    self.buffs.extend(sb)

class WkDestro(Warlock):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+Stamina','+5% Critical Strike Chance for Spells Debuff','Replenishment']
    self.buffs.extend(sb)

"""
Warriors
"""
class Warrior:
  def __init__(self):
    self.c = 'C69B6D'
    self.buffs = ['+Strength and Agility','+Stamina','-Armor Debuff','-10% Physical Damage Dealt Debuff']

class WaArms(Warrior):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+30% Bleed Damage Taken Debuff', '+4% Physical Damage Taken Debuff','-Healing Effectiveness Debuff']
    self.buffs.extend(sb)

class WaFury(Warrior):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = ['+5% to Critical Strike Chance','-Healing Effectiveness Debuff']
    self.buffs.extend(sb)

class WaProt(Warrior):
  def __init__(self, role='tank'):
    super().__init__()
    self.r = role
    self.sb = ['-20% Melee Attack Speed Debuff']
    self.buffs.extend(sb)
