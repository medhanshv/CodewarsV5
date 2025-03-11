from scripts.Troops.troop import Troop
from scripts.Troops.buildingtroop import BuildingTroop
from scripts.config import *

class Archer(Troop):
    def __init__(self,images , position, surf, myTower,std_size, uid):
        super().__init__(name="Archer", images = images, position = position, elixir = 3,
                         health=334, damage=118, velocity=MEDIUM_SPEED, type_="ground", attack_range = 5, surf = surf, discovery_range = 8, myTower = myTower,
                         target_type = {"air": True, "ground": True, "building": True}, splash_range = 0, size = 0.15,std_size= std_size, uid = uid, attack_speed = FAST_ATTACK,
                         number = 2)
class Giant(Troop):
    def __init__(self,images , position, surf, myTower,std_size, uid):
        super().__init__(name="Giant", images  = images,position = position, elixir = 5,
                         health=4496, damage=186, velocity=SLOW_SPEED, type_="ground", attack_range = 0, surf = surf, discovery_range = 7, myTower = myTower,
                         target_type = {"air": False, "ground": False, "building": True}, splash_range = 0, size = 0.5,std_size= std_size, uid = uid, attack_speed = SLOW_ATTACK)       
class Dragon(Troop):
    def __init__(self,images , position, surf, myTower, std_size, uid):
        super().__init__(name="Dragon", images  = images, position = position, elixir = 4,
                         health=1267, damage=176, velocity=FAST_SPEED, type_="air", attack_range = 3.5, surf = surf, discovery_range = 5, myTower = myTower,
                         target_type = {"air": True, "ground": True, "building": True}, splash_range = 1, size = 0.4, std_size= std_size, uid = uid, attack_speed = FAST_ATTACK)
class BombTower(BuildingTroop):
    def __init__(self, position, image_front, image_back, image_attack, surf, myTower,std_size, uid):
        super().__init__(name="BombTower", image_front = image_front, image_back=image_back, image_attack = image_attack, position = position, elixir = 5,
                         health=1670, damage=176, type_="building", attack_range = 3.5, surf = surf, myTower = myTower,
                         splash_range = 1, size = 1.2,std_size= std_size, uid = uid, attack_speed = MEDIUM_ATTACK)
class Balloon(Troop):
    def __init__(self,images , position, surf, myTower, std_size, uid):
        super().__init__(name="Balloon", images  = images, position = position, elixir = 5,
                         health=1848, damage=352, velocity=MEDIUM_SPEED, type_="air", attack_range = 3.5, surf = surf, discovery_range = 5, myTower = myTower,
                         target_type = {"air": False, "ground": False, "building": True}, splash_range = 1, size = 0.4, std_size= std_size, uid = uid, attack_speed = MEDIUM_ATTACK)
class Prince(Troop):
    def __init__(self, position, images , surf, myTower,std_size, uid):
        super().__init__(name="Prince", images = images, position = position, elixir = 5,
                         health=2312, damage=431, velocity=FAST_SPEED, type_="ground", attack_range = 0, surf = surf, discovery_range = 5, myTower = myTower,
                         target_type = {"air": False, "ground": True, "building": False}, splash_range = 0, size = 0.3,std_size= std_size, uid = uid, attack_speed = FAST_ATTACK)
class Barbarian(Troop):
    def __init__(self, position, images , surf, myTower,std_size, uid):
        super().__init__(name="Barbarian", images = images, position = position, elixir = 5,
                         health=736, damage=161, velocity=MEDIUM_SPEED, type_="ground", attack_range = 0, surf = surf, discovery_range = 5, myTower = myTower,
                         target_type = {"air": False, "ground": True, "building": False}, splash_range = 0, size = 0.25,std_size= std_size, uid = uid, attack_speed = MEDIUM_ATTACK,
                         number=5)
class Princess(Troop):
    def __init__(self, position, images , surf, myTower,std_size, uid):
        super().__init__(name="Princess", images = images, position = position, elixir = 3,
                         health=287, damage=186, velocity=MEDIUM_SPEED, type_="ground", attack_range = 9, surf = surf, discovery_range = 10, myTower = myTower,
                         target_type = {"air": True, "ground": True, "building": True}, splash_range = 1, size = 0.6,std_size= std_size, uid = uid, attack_speed = MEDIUM_ATTACK)
class Knight(Troop):
    def __init__(self, position, images , surf, myTower,std_size, uid):
        super().__init__(name="Knight", images = images, position = position, elixir = 3,
                         health=1938, damage=221, velocity=MEDIUM_SPEED, type_="ground", attack_range = 0, surf = surf, discovery_range = 7, myTower = myTower,
                         target_type = {"air": False, "ground": True, "building": True}, splash_range = 0, size = 0.3,std_size= std_size, uid = uid, attack_speed = FAST_ATTACK)
class Minion(Troop):
    def __init__(self, position, images , surf, myTower,std_size, uid):
        super().__init__(name="Minion", images = images, position = position, elixir = 5,
                         health=252, damage=129, velocity=FAST_SPEED, type_="air", attack_range = 2, surf = surf, discovery_range = 4, myTower = myTower,
                         target_type = {"air": True, "ground": True, "building": True}, splash_range = 0, size = 0.15,std_size= std_size, uid = uid, attack_speed = FAST_ATTACK,
                         number=3) 
class Skeleton(Troop):
    def __init__(self, position, images , surf, myTower,std_size, uid):
        super().__init__(name="Skeleton", images = images, position = position, elixir = 3,
                         health=89, damage=89, velocity=FAST_SPEED, type_="ground", attack_range = 0, surf = surf, discovery_range = 4, myTower = myTower,
                         target_type = {"air": False, "ground": True, "building": True}, splash_range = 0, size = 0.15,std_size= std_size, uid = uid, attack_speed = FAST_ATTACK,
                         number=10)    
class Wizard(Troop):
    def __init__(self,images , position, surf, myTower,std_size, uid):
        super().__init__(name="Wizard", images = images, position = position, elixir = 5,
                         health=1100, damage=410, velocity=MEDIUM_SPEED, type_="ground", attack_range = 5.5, surf = surf, discovery_range = 8, myTower = myTower,
                         target_type = {"air": True, "ground": True, "building": True}, splash_range = 1, size = 0.3,std_size= std_size, uid = uid, attack_speed = FAST_ATTACK,
                         number = 1) 

