import discord
from discord.ext import commands
import os
import traceback
import asyncio

@commands.command()
  async def help(self,ctx):
    embed = discord.Embed(title=f"help",timestamp=ctx.message.created_at,color=discord.Colour.purple(),inline=False)
    embed.set.thumbnail(url=ctx.guild.icon.url)
    #embed.add_field(vaule=f"このbotのプレフィックスは「{}」です。コマンドの前につけてください")
    embed.add_field(name="help",value=f"このコマンドです。\nbotのコマンドについて書かれています、",inline=False)
    embed.add_field(name="serverinfo",value=f"サーバー情報が取得できます。",inline=False)
    embed.add_field(name="tenki",value="天気が取得できます",inline=False)
    embed.set_footer(text=f"実行者：{ctx.author} ",icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
  
async def setup(bot):
  await bot.add_cog(help(bot))
