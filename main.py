# インストールした discord.py を読み込む
import discord
from discord.ext import commands
# prefix&intent
bot = commands.Bot(
    command_prefix = "a!",
    activity = discord.Activity(name = 'Aicybot', type = discord.ActivityType.playing),
    intents=discord.Intents.all())
# help削除
bot.remove_command("help")

#client
client = discord.Client

# token
TOKEN = 'token'

# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print( client.user.name + 'でログインしたよ！')
    # いろいろな定義
    bot.owner = bot.get_user(964887498436276305)
    bot.admin = bot.guild.get_role(995450894659362836)
    bot.notfy_ch = bot.guild.get_channel(995451213149638656)
    bot.manage_guild = bot.get_guild(984807772333932594)
    
     for file in os.listdir('./cog'):
        if file.endswith('.py'):
            try:
                await bot.load_extension(f'cog.{file[:-3]}')
                print(f'Loaded cog: cogs.{file[:-3]}')
            except:
                traceback.print_exc()


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
