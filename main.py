#importing libraries
from webserver import keep_alive #for bot to run 24/7
import discord 
from discord.ext import commands
import random
import os
bot=commands.Bot(command_prefix='')

#memes
images = ['https://i.im.ge/2022/06/10/rz60iq.jpg',
'https://i.im.ge/2022/06/10/rz6iXC.jpg',
'https://i.im.ge/2022/06/10/rz6m71.png',
'https://i.im.ge/2022/06/10/rz69GP.png',
'https://i.im.ge/2022/06/10/rz65bp.png',
'https://i.im.ge/2022/06/10/rz6wAf.png',
'https://i.im.ge/2022/06/10/rz66pm.png',
'https://i.im.ge/2022/06/10/rz6P2r.png',
'https://i.im.ge/2022/06/10/rz6twW.png',
'https://i.im.ge/2022/06/10/rz6yK0.png',
'https://i.im.ge/2022/06/10/rz6ClT.png',
'https://i.im.ge/2022/06/10/rz6Eic.png',
'https://i.im.ge/2022/06/10/rz6xcL.png',
'https://i.im.ge/2022/06/10/rz6b7x.png',
'https://i.im.ge/2022/06/10/rz63GG.jpg',
'https://i.im.ge/2022/06/10/rz6cCa.jpg',
'https://i.im.ge/2022/06/10/rz6gpJ.jpg',
'https://i.im.ge/2022/06/10/rz6R2y.jpg',
'https://i.im.ge/2022/06/10/rz6W6S.jpg',
'https://i.im.ge/2022/06/10/rz6ZKz.jpg',
'https://i.im.ge/2022/06/10/rz6Vl6.jpg',
'https://i.im.ge/2022/06/10/rz6f0F.jpg',
'https://i.im.ge/2022/06/10/rz6kcK.jpg',
'https://i.im.ge/2022/06/10/rz6ze9.jpg',
'https://i.im.ge/2022/06/10/rz6pDX.jpg']


#functionality
@bot.command ()
async def hello(ctx):
    await ctx.send("Hello " + ctx.author.display_name)

@bot.command ()
async def meme(ctx):
  embed=discord.Embed(color=discord.Color.red())
  random_meme=random.choice(images)
  embed.set_image(url=random_meme)
  await ctx.send(embed=embed)
  

#token and bot running    
token=os.environ['token']
keep_alive()
bot.run(token)