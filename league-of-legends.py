from flask import Flask
import csv

app = Flask(__name__)

champions = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe',
             'Aurelion Sol', 'Aurora', 'Azir', 'Bard', "Bel'Veth", 'Blitzcrank', 'Brand', 'Braum',
             'Briar', 'Caitlyn', 'Camille', 'Cassiopeia', "Cho'Gath", 'Corki', 'Darius', 'Diana', 'Dr. Mundo',
             'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio',
             'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Hwei',
             'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "K'Sante",
             "Kai'sa", 'Kalista', 'Karma', 'Khartus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen',
             "Kha'zix", 'Kindred', 'Kled', "Kog'Maw", 'LeBlanc', 'Lee Sin', 'Leona', 'Lillia', 'Lissandra',
             'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Master Yi', 'Milio',
             'Miss Fortune', 'Mordekaiser', 'Morgana', 'Naafiri', 'Nami', 'Nasus', 'Nautilus',
             'Neeko', 'Nidalee', 'Nilah', 'Nocturne', 'Nunu & Willump', 'Olaf', 'Orianna', 'Ornn', 'Pantheon',
             'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "Rek'Sai", 'Rell', 'Renata Glasc', 'Renekton',
             'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco',
             'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Smolder', 'Sona', 'Soraka', 'Swain',
             'Sylas', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle',
             'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar',
             "Vel'Koz", 'Vex', 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong',
             'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 'Zeri', 'Ziggs',
             'Zilean', 'Zoe', 'Zyra']

titles = ['the Darkin Blade', 'the Nine-Tailed Fox', 'the Rogue Assassin', 'the Rogue Sentinel', 'the Minotaur',
          'the Sad Mummy', 'the Cryophoenix', 'the Dark Child', 'the Weapon of the Faithful', 'the Frost Archer',
          'The Star Forger', 'the Witch Between Worlds', 'the Emperor of the Sands', 'the Wandering Caretaker',
          'the Empress of the Void', 'the Great Steam Golem', 'the Burning Vengeance', 'the Heart of the Freljord',
          'the Restrained Hunger', 'the Sheriff of Piltover', 'the Steel Shadow', "the Serpent's Embrace", 'the Terror of the Void',
          'the Daring Bombardier', 'the Hand of Noxus', 'Scorn of the Moon', 'the Glorious Executioner', 'the Madman of Zaun',
          'the Boy Who Shattered Time', 'the Spider Queen', "Agony's Embrace", 'the Prodigal Explorer', 'the Ancient Fear',
          'the Grand Duelist', 'the Tidal Trickster', 'the Colossus', 'the Saltwater Scourge', 'The Might of Demacia', 'the Missing Link',
          'the Rabble Rouser', 'the Outlaw', 'The Hallowed Seamstress', 'the Shadow of War', 'the Revered Inventor', 'the Visionary',
          'the Kraken Priestess', 'the Blade Dancer', 'the Green Father', "the Storm's Fury", 'the Exemplar of Demacia',
          'Grandmaster at Arms', 'the Defender of Tomorrow', 'the Virtuoso', 'the Loose Cannon', 'Daughter of the Void',
          'the Spear of Vengeance', 'the Enlightened One', 'the Deathsinger', 'the Void Walker', 'the Sinister Blade', 'the Righteous',
          'the Shadow Reaper', 'the Heart of the Tempest', 'the Voidreaver', 'The Eternal Hunters', 'the Cantankerous Cavalier',
          'the Mouth of the Abyss', 'the Pride of Nazumah', 'the Deceiver', 'the Blind Monk', 'the Radiant Dawn', 'the Bashful Bloom',
          'the Ice Witch', 'the Purifier', 'the Fae Sorceress', 'the Lady of Luminosity', 'Shard of the Monolith', 'the Prophet of the Void',
          'the Twisted Treant', 'the Wuju Bladesman', 'The Gentle Flame', 'the Bounty Hunter', 'the Monkey King', 'the Iron Revenant',
          'the Fallen', 'the Hound of a Hundred Bites', 'the Tidecaller', 'the Curator of the Sands', 'the Titan of the Depths', 'the Curious Chameleon',
          'the Bestial Huntress', 'the Joy Unbound', 'the Eternal Nightmare', 'the Boy and His Yeti', 'the Berserker', 'the Lady of Clockwork',
          'The Fire below the Mountain', 'the Unbreakable Spear', 'Keeper of the Hammer', 'the Bloodharbor Ripper', 'Empress of the Elements',
          "Demacia's Wings", 'The Charmer', 'the Armordillo', 'the Void Burrower', 'the Iron Maiden', 'the Chem-Baroness', 'the Butcher of the Sands',
          'the Pridestalker', 'the Exile', 'the Mechanized Menace', 'the Rune Mage', 'the Desert Rose', 'Fury of the North', 'the Redeemer',
          'the Starry-Eyed Songstress', 'the Boss', 'the Demon Jester', 'the Eye of Twilight', 'the Half-Dragon', 'the Mad Chemist',
          'The Undead Juggernaut', 'the Battle Mistress', 'the Primordial Sovereign', 'the Fiery Fledgling', 'Maven of the Strings',
          'the Starchild', 'the Noxian Grand General', 'the Unshackled', 'the Dark Sovereign', 'The River King', 'the Stoneweaver',
          "the Blade's Shadow", 'the Shield of Valoran', 'the Swift Scout', 'the Chain Warden', 'the Yordle Gunner', 'the Troll King',
          'the Barbarian King', 'the Card Master', 'the Plague Rat', 'the Spirit Walker', 'the Dreadnought', 'the Arrow of Retribution',
          'the Night Hunter', 'the Tiny Master of Evil', 'the Eye of the Void', 'the Gloomist', 'the Piltover Enforcer', 'The Ruined King',
          'the Machine Herald', 'the Crimson Reaper', 'the Relentless Storm', 'the Uncaged Wrath of Zaun', 'the Rebel', 'the Magus Ascendant',
          'the Seneschal of Demacia', 'the Unforgiven', 'the Unforgotten', 'Shepherd of Souls', 'the Magical Cat', 'the Secret Weapon',
          'the Master of Shadows', 'The Spark of Zaun', 'the Hexplosives Expert', 'the Chronokeeper', 'the Aspect of Twilight', 'Rise of the Thorns']

champion_data = [
    {'champion': champion, 'title': title,
     #  'skins': {'name', 'image'}}
     }
    for champion, title in zip(champions, titles)
]

keys = ['champion', 'title', 'skins', 'abilities', 'passive']

with open('lol_api.csv', 'w+') as csv_file:
   spreadsheet = csv.DictWriter(csv_file, fieldnames=keys)
   spreadsheet.writeheader()
   spreadsheet.writerows(champion_data)



# @app.get("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
#
# @app.get("/champions")
# def champions():
#     return champions_json
