import random
import copy

class apex:
    #====================================================================
    # Constructor
    #====================================================================
    def __init__(self):
        self.apex_characters = [    "Wraith","Path","Blood Hound","Gibby","Lifeline",
                    "Bang","Fart Boi","Mirage","Octane","Watson",
                    "Crypto","Rev","Loba","Rampart","Horizon","Fuze","Valkeryie"]
        self.guns       = ['eva','mastif','beak',
                'bow','sentinal','charge','longbow','pk'
                'r9','r301','p2020','alternator','G7-scout','re-45',
                'spittfire','flatline','hemlock','3030 Repeater','wingman',
                'volt','devo','L-Star','havoc']
        self.kings_canyon_drop_sites = ['Spotted Lake','Pit','Run-Off','Air-Base','Artillary',
                            'Gauntlet','Bunker','Salvage','Containment',
                            'Market','Caustic','Crash-Site','Broken-Relay','Capacitor',
                            'Labs','Hydro-Dam','Swamps','Repulsor','Rig','Map Room',
                            'Cage']
        self.olympus_drop_sites = [ 'Docks','Carrier','Estates','Elysium','Hydro-ponics','Power Grid',
                        'Turbine','Rift','Energy Depot','Hammond Labs','Solar Array','Bonzai',
                        'Gardens','Grow Towers','Orbital Canyon',]
        self.worlds_edge = [ 'Trials','Sky Hook','Lava Fisher','Countdown','Train Yard','Staging',
                        'Thermal','Tree','Harvester','Sorting','Launch Site','Dome',
                        'Lava City','Geyser','Overlook','Refinery','Survay','Epi-Center','Frag West','Frag East','Construction']

        self.drop_maps          = ['olympus','kings canyon','worlds edge',]
        self.long_line          = "====================================================================="
        self.short_line         = "==============================="
        self.weapons_list       = []
        self.character_list     = []

    def get_random_gun(self):
        w1 = random.choice(self.guns)
        self.guns.remove(w1)
        w2 = random.choice(self.guns)
        self.guns.remove(w2)
        return w1, w2

    def get_players_weapons(self,num_players):
        if (num_players >= 1):
            w1,w2 = self.get_random_gun()
            self.weapons_list.append(w1)
            self.weapons_list.append(w2)
        if (num_players >= 2):
            w1,w2 = self.get_random_gun()
            self.weapons_list.append(w1)
            self.weapons_list.append(w2)
        if (num_players >= 3):
            w1,w2 = self.get_random_gun()
            self.weapons_list.append(w1)
            self.weapons_list.append(w2)
        return self.weapons_list

    def pick_random_character(self,num_players):
        if (num_players >= 1):
            p1 = random.choice(self.apex_characters)
            self.apex_characters.remove(p1)
            self.character_list.append(p1)
        if (num_players >= 2):
            p2 = random.choice(self.apex_characters)
            self.apex_characters.remove(p2)
            self.character_list.append(p2)
        if (num_players >= 3):
            p3 = random.choice(self.apex_characters)
            self.apex_characters.remove(p3)
            self.character_list.append(p3)
        return self.character_list

    def pick_random_drop_site(self,map_name):
        if (map_name == 'kings canyon' or map_name == 'KC' or map_name =='kc'):
            target_list = self.kings_canyon_drop_sites
        elif (map_name == 'worlds edge' or map_name == 'we' or map_name == 'WE' or map_name == 'We'):
            target_list = self.worlds_edge
        elif (map_name == 'olympus'):
            target_list = self.olympus_drop_sites
        drop_site = random.choice(target_list)
        return drop_site