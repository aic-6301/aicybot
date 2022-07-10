# インストールした discord.py を読み込む
import discord
from discord.ext import commands
import os
import traceback
import asyncio

# 定義 1
BACKUP_CHANNEL_ID = 995463878257430558
DEFAULT_PREFIX = 'a!'
TOKEN = 'token'
intents = discord.Intents.all()
def _prefix_callable(bot: commands.Bot, msg: discord.Message) -> str:
    base = [f"<@!{bot.user.id}> ", f"<@{bot.user.id}> ", PREFIX]
    if msg.guild is None:  # dmの場合
        return base
    else:
        if msg.guild.me.nick is None:
            return base
        nick = msg.guild.me.display_name
        result = nick.strip(f":{bot.user}")
        # print(result)
        base = [f"<@!{bot.user.id}> ", f"<@{bot.user.id}> ", PREFIX, result]
        # extras = await prefixes_for(message.guild) # returns a list
        # return commands.when_mentioned_or(*base)(bot, msg)
        return base
# prefix&intent
bot = commands.Bot(
    command_prefix = _change_command_prefix,
    activity = discord.Activity(name = 'Aicybot', type = discord.ActivityType.playing),
    intents=discord.Intents.all())
# help削除
bot.remove_command("help")

#client
client = discord.Client



# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    global backup_ch
    global prefix_dict

    backup_ch = await bot.fetch_channel(BACKUP_CHANNEL_ID)
    prefix_dict = {}

    async for m in backup_ch.history():
        splited = m.content.split(' ', 1)
        prefix_dict[splited[0]] = splited[1]
    for file in os.listdir('./cogs/bot'):
        if file.endswith('.py'):
            try:
                await bot.load_extension(f'cogs/{file[:-3]}')
                print(f'Loaded cog: bot.{file[:-3]}')
            except:
                traceback.print_exc()
     for file in os.listdir('./cogs/tools'):
        if file.endswith('.py'):
            try:
                await bot.load_extension(f'cogs/{file[:-3]}')
                print(f'Loaded cog: tools.{file[:-3]}')
            except:
                traceback.print_exc()
                print( client.user.name + 'でログインしたよ！')

# メッセージ受信時に動作する
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/おはよう」と発言したら「おはようございます」が返る処理
    if message.content == 'おはよう':
        await message.channel.send('おはようございます！')

# 334への返信
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「334」と発言したら「な阪関無」が返る処理
    if message.content == '334':
        await message.channel.send('な阪関無')
        
# serverprefix



@bot.command(aliases=['cp'])
async def change_prefix(ctx, new_prefix: str = None):
    guild_id = str(ctx.guild.id)

    if new_prefix == None:
        if guild_id in prefix_dict.keys():
            old_prefix = prefix_dict[guild_id]
            async for m in backup_ch.history():
                if m.content.startswith(guild_id):
                    await m.delete()
            prefix_dict.pop(guild_id)
            await ctx.send(embed=discord.Embed(title='This server\'s prefix was reseted', description=f'{old_prefix} -> default({DEFAULT_PREFIX})'))
            return

        else:
            return

    if guild_id in prefix_dict.keys():
        async for m in backup_ch.history():
            if m.content.startswith(guild_id):
                await m.edit(content=f'{guild_id} {new_prefix}')
                break
        old_prefix = prefix_dict[guild_id]
        prefix_dict.pop(guild_id)
        prefix_dict[guild_id] = new_prefix
        await ctx.send(embed=discord.Embed(title='This server\'s prefix was changed', description=f'{old_prefix} -> {prefix_dict[guild_id]}'))
        return

    else:
        await backup_ch.send(f'{guild_id} {new_prefix}')
        prefix_dict[guild_id] = new_prefix
        await ctx.send(embed=discord.Embed(title='This server\'s prefix was changed', description=f'default({DEFAULT_PREFIX}) -> {prefix_dict[guild_id]}'))
        return


        
# エラーを送信

    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        embed = discord.Embed(title=":x: 失敗 -MissingPermissions", description=f"実行者の必要な権限が無いため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
        embed = discord.Embed(title=":x: 失敗 -BotMissingPermissions", description=f"Botの必要な権限が無いため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(title=":x: 失敗 -CommandNotFound", description=f"不明なコマンドもしくは現在使用不可能なコマンドです。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.MemberNotFound):
        embed = discord.Embed(title=":x: 失敗 -MemberNotFound", description=f"指定されたメンバーが見つかりません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者をメンションしてください。")
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.errors.BadArgument):
        embed = discord.Embed(title=":x: 失敗 -BadArgument", description=f"指定された引数がエラーを起こしているため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者をメンションしてください。")
        await ctx.send(embed=embed) 
    elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title=":x: 失敗 -BadArgument", description=f"指定された引数が足りないため実行出来ません。", timestamp=ctx.message.created_at, color=discord.Colour.red())
        embed.set_footer(text="お困りの場合は、サーバー管理者をメンションしてください。")
        await ctx.send(embed=embed) 
    else:
        raise error
# Botの起動とDiscordサーバーへの接続
bot.run(TOKEN)
