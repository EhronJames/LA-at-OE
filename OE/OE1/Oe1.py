class hero():
    def __init__(self, name, role, health, basic_attack, dmg_type):
        self.name = name
        self.role = role
        self.health = health
        self.basic_attack = basic_attack
        self.dmg_type = dmg_type

    def describe(self):
        return f"{self.name} is a {self.role} with a {self. dmg_type} power having {self.health} maximum health that can deal {self.basic_attack}%   "

hero_jg = hero("saber", "jg","basic attack damage",100, 50)
hero_mm1 = hero("lisli","marksman", "attack damage",100, 30)
hero_fighter1 = hero("lukas", "fighter", "attackdamage",150, 20)
hero_ap = hero("lunox", "mage", "ability",100, 10)
hero_roam = hero("atlas", "roamer", "hybrid",100, 10)

print(f'''
{hero_jg.name}
{hero_jg.role}
{hero_jg.health}
{hero_jg.basic_attack}
{hero_jg.dmg_type}
{hero_jg.describe()} 

{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.health}
{hero_mm1.basic_attack}
{hero_mm1.dmg_type}
{hero_mm1.describe()}

{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.health}
{hero_fighter1.basic_attack}
{hero_fighter1.dmg_type}
{hero_fighter1.describe()} 

{hero_ap.name}
{hero_ap.role}
{hero_ap.health}
{hero_ap.basic_attack}
{hero_ap.dmg_type}
{hero_ap.describe()} 

{hero_roam.name}
{hero_roam.role}
{hero_roam.health}
{hero_roam.basic_attack}
{hero_roam.dmg_type}
{hero_roam.describe()} 


''')
print("Jg diff")
