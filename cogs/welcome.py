import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv() 

def circle(pfp):
    pass  

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"Member {member.display_name} joined the server.")  # Debugging message

        try:
            asset = member.avatar_url_as(size=128)
            data = BytesIO(await asset.read())
            pfp = Image.open(data).convert("RGBA")
            pfp = circle(pfp)
            pfp = pfp.resize((350, 350))

            background = Image.open("BACKGROUND.png")  # Replace with your background image path
            font_size = 60  # Adjust the font size 
            font = ImageFont.truetype("leaguegothic-condensed-italic-webfont.ttf", font_size) 

            draw = ImageDraw.Draw(background)
            member_text = member.display_name  # Use member's display name

            # Drawing member's name
            draw.text((720, 290), member_text, font=font)

            background.paste(pfp, (190, 145), pfp)
            filename = "welcome_image.png"
            background.save(filename)

            guild = self.bot.get_guild(int(os.getenv('SERVER_ID')))
            welcome_channel = guild.get_channel(int(os.getenv('WELCOME_CHANNEL_ID')))

            # Mention the member in the message
            message_content = f"Hi {member.mention} Welcome to the server!"
            await welcome_channel.send(message_content, file=discord.File(filename))

            # Add role to the member
            role = guild.get_role(int(os.getenv('ROLE_ID')))
            await member.add_roles(role)

            await asyncio.sleep(5)

            try:
                os.remove(filename)
            except:
                pass

        except Exception as e:
            print(f"Error fetching avatar: {e}")

def setup(bot):
    bot.add_cog(Welcome(bot))
