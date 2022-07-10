import discord
from discord.ext import commands
import os
import traceback
import asyncio

@bot.command()
  async def help(self,ctx):
    embed = discord.Embed(title=f"help",timestamp=ctx.message.created_at,color=discord.Colour.purple(),inline=False)
    embed.set.thumbnail(url=ctx.guild.icon.url)
    #embed.add_field(vaule=f"このbotのプレフィックスは「{}」です。コマンドの前につけてください")
    embed.add_field(name="help",value=f"このコマンドです。\nbotのコマンドについて書かれています、",inline=False)
    embed.add_field(name="serverinfo",value=f"サーバー情報が取得できます。",inline=False)
    embed.add_field(name="tenki",value="天気が取得できます",inline=False)
    #embed.add_field(name="",value=guild.owner,inline=False)
    #embed.add_field(name="チャンネル数",value=f"{len(text_channels)}",inline=False)
    #embed.add_field(name="ロール数",value=f"{len(roles)}",inline=False)
    #embed.add_field(name="サーバーブースト数",value=guild.premium_subscription_count,inline=False)
    #embed.add_field(name="メンバー数",value=guild.member_count,inline=False)
    embed.set_footer(text=f"実行者：{ctx.author} ",icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
  
  def setup(bot):
  bot.add_cog(help(bot))
