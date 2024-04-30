"""
This file defines a player class and the attributes/functions available for that class
"""
import classes

class Character:
  def __init__(self, n, c, s, **kwargs):
    name = n
    class = c
    spec = s

    if c=='Death Knight':
      if s=='Blood':
        if 'role' in kwargs:
          r = role
          a=DKBlood(role=r)
        else:
          a=DKBlood()
      elif s=='Frost':
        a=DKFrost()
      elif s=='Unholy':
        a=DKUnholy()
      else:
        print("Invalid Class/Spec Pairing")
        break
        
    elif c=='Druid':
      if s=='Feral':
        if 'role' in kwargs:
          r = role
          a=DrFeral(role=r)
        else:
          a=DrFeral()
      elif s=='Balance':
        a=DrBalance()
      elif s=='Restoration':
        a=DrResto()
      else:
        print("Invalid Class/Spec Pairing")
        break

    elif c=='Hunter':
      if s=='BM':
        a=HBM()
      elif s=='Marksmanship':
        a=HMarks()
      elif s=='Survival':
        a=HSurv()
      else:
        print("Invalid Class/Spec Pairing")
        break

    elif c=='Mage':
      if s=='Arcane':
        a=MArcane()
      elif s=='Fire':
        a=MFire()
      elif s=='Frost':
        a=MFrost()
      else:
        print("Invalid Class/Spec Pairing")
        break

    elif c=='Paladin':
      if s=='Protection':
        a=PalProt()
      elif s=='Holy':
        a=PalHoly()
      elif s=='Retribution':
        a=PalRet()
      else:
        print("Invalid Class/Spec Pairing")
        break

    elif c=='Priest':
      if s=='Discipline':
        a=PrDisc()
      elif s=='Holy':
        a=PrHoly()
      elif s=='Shadow':
        a=PrShadow()
      else:
        print("Invalid Class/Spec Pairing")
        break

    elif c=='Rogue':
      if s=='Assassination':
        a=RAss()
      elif s=='Combat':
        a=RCombat()
      elif s=='Subtlety':
        a=RSubtlety()
      else:
        print("Invalid Class/Spec Pairing")
        break

    elif c=='Shaman':
      if s=='Enhancement':
        a=SEnhance()
      elif s=='Elemental':
        a=SElemental()
      elif s=='Restoration':
        a=SResto()
      else:
        print("Invalid Class/Spec Pairing")
        break

    elif c=='Warlock':
      if s=='Affliction':
        a=WkAff()
      elif s=='Demonology':
        a=WkDemo()
      elif s=='Destruction':
        a=WkDestro()
      else:
        print("Invalid Class/Spec Pairing")
        break

    elif c=='Warrior':
      if s=='Arms':
        a=WaArms()
      elif s=='Fury':
        a=WaFury()
      elif s=='Protection':
        a=WaProt()
      else:
        print("Invalid Class/Spec Pairing")
        break

    else:
      print("Invalid Class")
      break
  
      
    

  def buff_check(self):
    print(name+" provides "+ a.buffs)
    
    

class Player:
  def __init__(self, name, **kwargs):
    self.name = name
    self.charlist = []

  def add_character(self, name, class, spec, **kwargs):
    if 'role' in kwargs:
      r = role
      self.charlist.append(Character(name, class, spec, role=r))
    else:
      self.charlist.append(Character(name, class, spec)
    
      

    
    
