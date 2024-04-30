"""
This file defines a player class and the attributes/functions available for that class
"""
import classes

class Character:
  def __init__(self, name, cl, spec, **kwargs):
    n = name
    c = cl
    s = spec
    a = None

    if c=='Death Knight':
      if s=='Blood':
        if 'role' in kwargs:
          r = kwargs.get('role')
          a=classes.DKBlood(role=r)
        else:
          a=classes.DKBlood()
      elif s=='Frost':
        a=classes.DKFrost()
      elif s=='Unholy':
        a=classes.DKUnholy()
      else:
        print("Invalid Class/Spec Pairing")    
        
    elif c=='Druid':
      if s=='Feral':
        if 'role' in kwargs:
          r = kwargs.get('role')
          a=classes.DrFeral(role=r)
        else:
          a=classes.DrFeral()
      elif s=='Balance':
        a=classes.DrBalance()
      elif s=='Restoration':
        a=classes.DrResto()
      else:
        print("Invalid Class/Spec Pairing")       

    elif c=='Hunter':
      if s=='BM':
        a=classes.HBM()
      elif s=='Marksmanship':
        a=classes.HMarks()
      elif s=='Survival':
        a=classes.HSurv()
      else:
        print("Invalid Class/Spec Pairing")       

    elif c=='Mage':
      if s=='Arcane':
        a=classes.MArcane()
      elif s=='Fire':
        a=classes.MFire()
      elif s=='Frost':
        a=classes.MFrost()
      else:
        print("Invalid Class/Spec Pairing")      

    elif c=='Paladin':
      if s=='Protection':
        a=classes.PalProt()
      elif s=='Holy':
        a=classes.PalHoly()
      elif s=='Retribution':
        a=classes.PalRet()
      else:
        print("Invalid Class/Spec Pairing")        

    elif c=='Priest':
      if s=='Discipline':
        a=classes.PrDisc()
      elif s=='Holy':
        a=classes.PrHoly()
      elif s=='Shadow':
        a=classes.PrShadow()
      else:
        print("Invalid Class/Spec Pairing")        

    elif c=='Rogue':
      if s=='Assassination':
        a=classes.RAss()
      elif s=='Combat':
        a=classes.RCombat()
      elif s=='Subtlety':
        a=classes.RSubtlety()
      else:
        print("Invalid Class/Spec Pairing")       

    elif c=='Shaman':
      if s=='Enhancement':
        a=classes.SEnhance()
      elif s=='Elemental':
        a=classes.SElemental()
      elif s=='Restoration':
        a=classes.SResto()
      else:
        print("Invalid Class/Spec Pairing") 

    elif c=='Warlock':
      if s=='Affliction':
        a=classes.WkAff()
      elif s=='Demonology':
        a=classes.WkDemo()
      elif s=='Destruction':
        a=classes.WkDestro()
      else:
        print("Invalid Class/Spec Pairing")        

    elif c=='Warrior':
      if s=='Arms':
        a=classes.WaArms()
      elif s=='Fury':
        a=classes.WaFury()
      elif s=='Protection':
        a=classes.WaProt()
      else:
        print("Invalid Class/Spec Pairing")       

    else:
      print("Invalid Class")              

  def buff_check(self):
    print(self.n+" provides "+ self.a.buffs)


class Player:
  def __init__(self, name, **kwargs):
    self.name = name
    self.charlist = []

  def add_character(self, name, cl, spec, **kwargs):
    if 'role' in kwargs:
      r = kwargs.get('role')
      self.charlist.append(Character(name, cl, spec, role=r))
    else:
      self.charlist.append(Character(name, cl, spec))
    
      

    
    
