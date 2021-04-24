import os
import discord
from dotenv import load_dotenv
from apex_rng.apex_class import apex as ar
import emoji

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = 'The Loot Goblins'
client = discord.Client()
hal_emote = '<:halMoment:830282349408157756>'

idiot_msg = emoji.emojize('idiot specify arguments :clown: :toilet: -- Hal') + 8*hal_emote
lucas_msg = emoji.emojize('Lucas is a wing man user Blugh Blugh Blugh Blugh. :face_vomiting::face_vomiting::poop::poop::poop::poop::poop:')
meme_msg = 'Your a :regional_indicator_m::regional_indicator_e::regional_indicator_m::regional_indicator_e:'
nathaniel_msg = 'Boink Boink Nathaniel is tweakin off the doink'

class MyClient(discord.Client):
    def print_weapons(self,num_players):
        apex_rng = ar()
        weapons = apex_rng.get_players_weapons(int(num_players))

        msg = '\n'
        index = 0

        for i in weapons:
            if (index % 2 == 0):
                msg = msg + '\n> Player %s\'s Weapons\n' % ((index // 2) + 1 ) 
            weapon_slot = str((index % 2)+1)

            msg = msg + '```fix\n' + '\t'+ 'Slot ' + weapon_slot + ' = ' + str(i) + '\n```'
            index+=1
        msg = msg + '\n'
        return msg

    def print_drop_site(self,curr_map):
        apex_rng = ar()
        drop_site = apex_rng.pick_random_drop_site(curr_map)
        msg = '```yaml\n' + str(drop_site) + '```'
        msg = msg + '\n'
        return msg

    def print_characters(self,num_players):
        apex_rng = ar()
        characters = apex_rng.pick_random_character(int(num_players))
        msg = ''
        index = 1
        for i in characters:
            msg = msg + '```fix\n' 'Player ' + str(index) +  ' = ' + str(i) + '\n```'
            index +=1
        msg = msg + '\n'
        return msg

    def color_fy(self,str):
        return '```yaml\n' + str + '```'

    def print_help_menu(self):

        description = 'Here is the help menu for arguments accepted by this bot. '
        description += 'Each argument is listed under the header for each command. '
        description += '[a|b] is the means argument could be a or b'


        rng_msg = 'Syntax: ' + self.color_fy('!rng [kc|KC|kings canyon|olympus] [1|2|3]')
        rng_msg += 'Description: Generates random loadouts, drop location, and characters\n'

        players_msg = 'Syntax: ' + self.color_fy('!players [1|2|3]\n')
        players_msg += 'Description: Generates random characters\n'

        map_msg = 'Syntax: ' + self.color_fy('!map [kc|KC|kings canyon|olympus]\n')
        map_msg += 'Description: Generates random drop locations\n'

        weapons_msg = 'Syntax: ' + self.color_fy('!weapons [1|2|3]\n')
        weapons_msg += 'Description: Generates random weapon loadouts\n'

        server_msg ="Bot commands that are specific to the Loot Goblins Server"
        isaac_msg = 'Syntax: ' + self.color_fy('!isaac') + 'Kill Steal Complainer  ' +  5* (' ' + hal_emote)
        nathaniel_msg = 'Syntax: ' + self.color_fy('!nathaniel') + 'Sweaty Wraith  ' +  hal_emote
        lucas_msg = 'Syntax: ' + self.color_fy('!lucas') + 'Wingman User ' + 5 * ':face_vomiting:'

        embed=discord.Embed(title="Light Ammo Bot Help Menu", description=description, color=0xf59542)
        #embed.set_image(url='https://cdn-images.win.gg/resize/w/610/h/345/format/webp/type/progressive/fit/cover/path/news/f1a94cef23357f68031e958c443c0dfe/4484809be87819c27a1b7e81508f743a/original.jpg')
        embed.set_author(name="Light Ammo")

        embed.add_field(name="Apex Commands", value="Apex Bot Commands", inline=False)

        embed.add_field(name="!rng", value=rng_msg, inline=True)
        embed.add_field(name="!map", value=map_msg, inline=False)
        embed.add_field(name="!players", value=players_msg, inline=True)

        embed.add_field(name="!weapons", value=weapons_msg, inline=True)

        embed.add_field(name="Server Commands", value=server_msg, inline=False)
        embed.add_field(name="!isaac", value=isaac_msg, inline=True)
        embed.add_field(name="!lucas", value=lucas_msg, inline=True)
        embed.add_field(name="!nathaniel", value=nathaniel_msg, inline=True)
        return embed

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!bot'):
            channel = message.channel
            await message.reply('Why the heck are u in ' + str(channel)+'. You are the real bot KEKW', mention_author=True)
        #=================================
        # Players Command [!players]
        #=================================
        if message.content.startswith('!players'):
            msg_len = len(message.content)
            if (int(msg_len) > 8):
                num_players = message.content[9]
                msg = self.print_characters(num_players)
                description = 'You have chosen to randomly characters for %s Player(s)' % (num_players)
                embed=discord.Embed(title="Randomly Generated Characters", description=description, color=0xf59542)
                embed.add_field(name="Characters", value=msg)
                await message.reply(embed=embed, mention_author=True)
            else:
                msg = idiot_msg
                await message.reply(msg, mention_author=True)
        #=================================
        # Drop Site Command [!map]
        #=================================
        if message.content.startswith('!map'):
            msg_len = len(message.content)
            if (int(msg_len) > 4):
                curr_map = message.content[5:]
                msg = self.print_drop_site(curr_map)
                embed=discord.Embed(title="Randomly Generated Drop Site", description=msg, color=0xf59542)
                await message.reply(embed=embed, mention_author=True)
            else:
                msg = idiot_msg
                await message.reply(msg, mention_author=True)

        #=================================
        # Players Command [!weapons]
        #=================================
        if message.content.startswith('!weapons'):
            msg_len = len(message.content)

            if (int(msg_len) > 8):
                num_players = message.content[9]
                msg = self.print_weapons(num_players)
                description = 'You have chosen to randomly generate a loadout for %s Player(s)' % (num_players)
                embed=discord.Embed(title="Randomly Generated Weapons", description=description, color=0xf59542)
                embed.add_field(name="Weapons", value=msg)
                await message.reply(embed=embed, mention_author=True)
            else:
                msg = idiot_msg
                await message.reply(msg, mention_author=True)
            #await message.reply(msg, mention_author=True)

        #=================================
        # Full Command
        #=================================    
        if message.content.startswith('!rng'):
            msg_len = len(message.content)
            if (int(msg_len) > 4):
                curr_map = message.content[5:-2]
                num_players = int(message.content[-1])
                char_msg = self.print_characters(num_players)
                wep_msg = self.print_weapons(num_players)
                ds_msg = self.print_drop_site(curr_map)

                description = 'You have chosen to randomly generate weapons, characters, and a dropsite for %s Player(s)' % (num_players)
                embed=discord.Embed(title="Randomly Generated Full Package", description=description, color=0xf59542)


                embed.add_field(name="Characters", value=char_msg, inline=False)
                embed.add_field(name="Weapons", value=wep_msg, inline=False)
                embed.add_field(name="Dropsite", value=ds_msg, inline=False)

                embed.set_footer(text="Light Boi Tingz")
                await message.reply(embed=embed, mention_author=True)
            else:
                msg = idiot_msg
            await message.reply(msg, mention_author=True)

        #================
        # Lucas
        #================
        if message.content.startswith('!lucas'):
            await message.reply(lucas_msg, mention_author=True,tts=True)
        #================
        # !meme
        #================
        if message.content.startswith('!meme'):
            await message.reply(meme_msg, mention_author=True)
        #================
        # !nathaniel
        #================
        if message.content.startswith('!nathaniel'):
            await message.reply(nathaniel_msg, mention_author=True,tts=True)
        #================
        # !isaac
        #================
        if message.content.startswith('!isaac'):
            await message.reply('I cannot get mad at my creator KEKW', mention_author=True,tts=True)
        #==========
        # !help
        #==========
        if message.content.startswith('!help'):
            embed = self.print_help_menu()
            await message.reply(embed=embed, mention_author=True)

    async def on_ready(self):
        await client.change_presence(status=discord.Status.online, activity=discord.Game('Apex Legends'))
    async def restartBot(ctx):
        await ctx.bot.logout()
        await ctx.bot.login(TOKEN, bot=True)  



client = MyClient()
client.run(TOKEN)