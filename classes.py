""" This file contains the class and spec information for WoW Cata Classic
"""

""" 
Death Knights
"""
class DeathKnight:
  def __init__(self):
    self.c = 'C41E3A'
    self.buffs = []

class DKBlood(DeathKnight):
  def __init__(self, role='tank'):
    super().__init__()
    self.r = role
    self.buffs.append('')

class DKFrost(DeathKnight):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

class DKUnholy(DeathKnight):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')
  
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
    self.buffs.append('')

class DrBalance(Druid):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

class DrResto(Druid):
  def __init__(self, role='heal'):
    super().__init__()
    self.r = role
    self.buffs.append('')

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
    self.buffs.append('')

class HMarks(Hunter):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

class HSurv(Hunter):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

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
    self.buffs.append('')    

class MFire(Mage):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

class MFrost(Mage):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

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
    self.buffs.append('')

class PalHoly(Paladin):
  def __init__(self, role='heal'):
    super().__init__()
    self.r = role
    self.buffs.append('')

class PalRet(Paladin):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

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
    self.buffs.append('')

class PrHoly(Priest):
  def __init__(self, role='heal'):
    super().__init__()
    self.r = role
    self.buffs.append('')

class PrShadow(Priest):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

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
    self.buffs.append('')

class RCombat(Rogue):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

class RSubtlety(Rogue):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

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
    self.buffs.append('')

class SElemental(Shaman):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

class SResto(Shaman):
  def __init__(self, role='heal'):
    super().__init__()
    self.r = role
    self.buffs.append('')

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
    self.buffs.append('')

class WkDemo(Warlock):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

class WkDestro(Warlock):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

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
    self.buffs.append('')

class WaFury(Warrior):
  def __init__(self, role='dps'):
    super().__init__()
    self.r = role
    self.buffs.append('')

class WaProt(Warrior):
  def __init__(self, role='tank'):
    super().__init__()
    self.r = role
    self.buffs.append('')
