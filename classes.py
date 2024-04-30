""" This file contains the class and spec information for WoW Cata Classic
"""

""" 
Death Knights
"""
class DeathKnight:
  def __init__(self):
    self.c = 'C41E3A'
    self.buffs = ['Agility and Strength','10% Melee Attack Speed Debuff']

class DKBlood(DeathKnight):
  def __init__(self, role='tank'):
    super().__init__()
    self.r = role
    self.sb = ['10% AP',]
    self.buffs.extend(sb)

class DKFrost(DeathKnight):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class DKUnholy(DeathKnight):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)
  
"""
Druids
"""
class Druid:
  def __init__(self):
    self.c = 'FF7C0A'
    self.buffs = []

class DrFeral(Druid):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class DrBalance(Druid):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class DrResto(Druid):
  def __init__(self, role='heal'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

"""
Hunters
"""
class Hunter:
  def __init__(self):
    self.c = 'AAD372'
    self.buffs = []
    
class HBM(Hunter):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class HMarks(Hunter):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class HSurv(Hunter):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

"""
Mages
"""
class Mage:
  def __init__(self):
    self.c = '3FC7EB'
    self.buffs = []

class MArcane(Mage):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)   

class MFire(Mage):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class MFrost(Mage):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

"""
Paladins
"""
class Paladin:
  def __init__(self):
    self.c = 'F48CBA'
    self.buffs = []

class PalProt(Paladin):
  def __init__(self, role='tank'):
    super().__init__()
    self.r = role
    self.sb = []
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
    self.sb = []
    self.buffs.extend(sb)

"""
Priests
"""
class Priest:
  def __init__(self):
    self.c = 'FFFFFF'
    self.buffs = []

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
    self.sb = []
    self.buffs.extend(sb)

"""
Rogues
"""
class Rogue:
  def __init__(self):
    self.c = 'FFF468'
    self.buffs = []

class RAss(Rogue):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class RCombat(Rogue):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class RSubtlety(Rogue):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

"""
Shamans
"""
class Shaman:
  def __init__(self):
    self.c = '0070DD'
    self.buffs = []

class SEnhance(Shaman):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class SElemental(Shaman):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class SResto(Shaman):
  def __init__(self, role='heal'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

"""
Warlocks
"""
class Warlock:
  def __init__(self):
    self.c = '8788EE'
    self.buffs = []

class WkAff(Warlock):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class WkDemo(Warlock):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class WkDestro(Warlock):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

"""
Warriors
"""
class Warrior:
  def __init__(self):
    self.c = 'C69B6D'
    self.buffs = []

class WaArms(Warrior):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class WaFury(Warrior):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)

class WaProt(Warrior):
  def __init__(self, role='tank'):
    super().__init__()
    self.r = role
    self.sb = []
    self.buffs.extend(sb)
