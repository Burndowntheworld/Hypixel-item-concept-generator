def generate_damage(damage, reforge=0, hpb=0):
    out = '[{"text":"Damage:","italic":false,"color":"gray"},{"text":" +%s","color":"red"}' %(damage)
    if hpb > 0:
        out += ',{"text":" (+%s)","color":"yellow"}' %(hpb)
    if reforge > 0:
        out += ',{"text":" (+%s)","color":"blue"}' %(reforge)
    return out + ']'

def generate_strength(strength, reforge=0, hpb=0, aow=0):
    out = '[{"text":"Strength: ","italic":false,"color":"gray"},{"text":"+%s","color":"red"}' %(strength)
    if hpb > 0:
        out += ',{"text":" (+%s)","color":"yellow"}' %(hpb)
    if aow > 0:
        out += ',{"text":" [+%s]","color":"gold"}' %(aow)
    if reforge > 0:
        out += ',{"text":" (+%s)","color":"blue"}' %(reforge)
    return out + ']'

def generate_crit_chance(cc, reforge=0):
    out = '[{"text":"Crit Chance: ","italic":false,"color":"gray"},{"text":"+%s%%","color":"red"}' %(cc)
    if reforge > 0:
        out += ',{"text":" (+%s%%)","color":"blue"}' %(reforge)
    return out + ']'

def generate_crit_damage(cd, reforge=0):
    out = '[{"text":"Crit Damage: ","italic":false,"color":"gray"},{"text":"+%s%%","color":"red"}' %(cd)
    if reforge > 0:
        out += ',{"text":" (+%s%%)","color":"blue"}]' %(reforge)
    return out + ']'

def generate_attack_speed(aspeed, reforge=0):
    out = '[{"text":"Attack Speed: ","italic":false,"color":"gray"},{"text":"+%s%%","color":"red"}' %(aspeed)
    if reforge > 0:
        out += ',{"text":" (+%s%%)","color":"blue"}]' %(reforge)
    return out + ']'

def generate_ferocity(fero, reforge=0):
    out =  '[{"text":"Ferocity: ","italic":false,"color":"gray"},{"text":"+%s","color":"green"}' %(fero)
    if reforge > 0:
        out += ',{"text":" (+%s)","color":"blue"}]' %(reforge)
    return out + ']'

def generate_speed(speed, reforge=0):
    out = '[{"text":"Speed: ","italic":false,"color":"gray"},{"text":"+%s","color":"green"}' %(speed)
    if reforge > 0:
        out += ',{"text":" (+%s)","color":"blue"}]' %(reforge)
    return out + ']'

def generate_health(health, reforge=0, hpb=0):
    out = '[{"text":"Health: ","italic":false,"color":"gray"},{"text":"+%s","color":"green"}' %(health)
    if hpb > 0:
        out += ',{"text":" (+%s)","color":"yellow"}' %(hpb)
    if reforge > 0:
        out += ',{"text":" (+%s)","color":"blue"}]' %(reforge)
    return out + ']'

def generate_defense(defense, reforge=0, hpb=0):
    out = '[{"text":"Defense: ","italic":false,"color":"gray"},{"text":"+%s","color":"green"}' %(defense)
    if hpb > 0:
        out += ',{"text":" (+%s)","color":"yellow"}' %(hpb)
    if reforge > 0:
        out += ',{"text":" (+%s)","color":"blue"}' %(reforge)
    return out + ']'

def generate_intelligence(intelligence, reforge=0):
    out = '[{"text":"Intelligence: ","italic":false,"color":"gray"},{"text":"+%s","color":"aqua"}' %(intelligence)
    if reforge > 0:
        out += ',{"text":" (+%s)","color":"blue"}' %(reforge)
    return out + ']'

def generate_magic_find(magic_find):
    return '[{"text":"Magic Find: ","italic":false,"color":"gold"},{"text":"+%s","color":"gold"}]' %(magic_find)

def enchantments(**enchants):
    enchant_list = ['{id:"%s",lvl:%s}' %(k,v) for k,v in enchants.items()]
    return ',Enchantments:[' + ','.join(enchant_list) + ']'

def ability(name, description, mana):
    return '[{"text":"","italic":false}]\',\'[{"text":"Item Ability: %s ","italic":false,"color":"gold"},{"text":"RIGHT CLICK","color":"yellow","bold":true}]\',\'[{"text":"%s","italic":false,"color":"gray"}]\',\'[{"text":"mana cost: ","italic":false,"color":"dark_gray"},{"text":"%s","color":"dark_aqua"}]' %(name, description, mana)

def star(amount):
    return " " + "\u272A"*amount

def rarity(rarity, item, color, recombobulated=False):
    if recombobulated:
        return ",\'[{\"text\":\"%s %s\",\"italic\":false,\"color\":\"%s\",\"bold\":true}]','[{\"text\":\"e\",\"italic\":false,\"color\":\"light_purple\",\"obfuscated\":true},{\"text\":\" Rarity upgraded \",\"obfuscated\":false},{\"text\":\"e\"}]'" %(rarity, item, color)
    else:
        return ",\'[{\"text\":\"%s %s\",\"italic\":false,\"color\":\"%s\",\"bold\":true}]'" %(rarity, item, color)

def generate_command(item, name, color, stars, rarity, enchantments, *stats):
    out = "/give @p %s{display:{Name:'[{\"text\":\"%s\",\"color\":\"%s\",\"italic\":false},{\"text\":\"%s\",\"color\":\"gold\",\"italic\":false}]',Lore:[" %(item, name, color, star(stars))
    out += ",".join("'%s'" %(stat) for stat in stats)
    out += rarity
    out += "]}%s} 1" %(enchantments)
    print(out)


generate_command("stone", "slasher", "dark_purple", 6, rarity("Epic","Sword","dark_purple", True), enchantments(sharpness=24,knockback=9), generate_health(10,15,20), generate_defense(13,13,54), generate_damage(54,0,32), generate_strength(12,203,2,5))