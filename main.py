# インストールした discord.py を読み込む
import discord
from discord.ext import commands
# prefix&intent
bot = commands.Bot(command_prefix = "a!", intents=discord.Intents.all())
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

# 天気
# どこを取得するか
citycodes = {
    "北海道":"016010",
    "青森":"020010",
    "岩手":"030010",
    "宮城":"040010",
    "秋田":"050010",
    "山形":"060010",
    "福島":"070010",
    "茨城":"080010",
    "栃木":"090010",
    "群馬":"100010",
    "埼玉":"110010",
    "千葉":"120010",
    "東京":"130010",
    "神奈川":"140010",
    "新潟":"150010",
    "富山":"160010",
    "石川":"170010",
    "福井":"180010",
    "山形":"190010",
    "長野":"200010",
    "岐阜":"210010",
    "静岡":"220010",
    "愛知":"230010",
    "三重":"240010",
    "滋賀":"250010",
    "京都":"260010",
    "大阪":"270000",
    "兵庫":"280010",
    "奈良":"290010",
    "和歌山":"300010",
    "鳥取":"310010",
    "島根":"320010",
    "岡山":"330010",
    "広島":"340010",
    "山口":"350010",
    "徳島":"360010",
    "香川":"370000",
    "愛媛":"380010",
    "高知":"390010",
    "福島":"400010",
    "佐賀":"410010",
    "長崎":"420010",
    "熊本":"430010",
    "大分":"440010",
    "宮崎":"450010",
    "鹿児島":"460010",
    "沖縄":"471010",    
}

 # 取得
    
@bot.event
async def on_message(message):
  if message.author != client.user:

    reg_res = re.compile(u"(.+)の天気").search(message.content)
    if reg_res:

      if reg_res.group(1) in citycodes.keys():

        citycode = citycodes[reg_res.group(1)]
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
        resp = json.loads(resp.decode('utf-8'))
# メッセージにして送信
        msg = resp['location']['city']
        msg += "の天気は、\n"
        for f in resp['forecasts']:
          msg += f['dateLabel'] + "が" + f['telop'] + "\n"
        msg += "です。"

        await client.send_message(message.channel, message.author.mention + msg)

      else:
        await client.send_message(message.channel, message.content + "は対応していないか受信ができませんでした。")

# サーバー情報
@bot.command()
async def serverinfo(ctx):
    guild = ctx.message.guild
    roles =[role for role in guild.role]
    text_channels = [text_channels for textchannels in guild.text_channels]
    #embedのないよう
    embed = discord.Embed(title=f"サーバー情報 - {guild.name}",timestamp=ctx.message.created_at,color=discord.Colour.purple(),inline=False)
    embed.set.thumbnail(url=ctx.guild.icon.url)
    embed.add_field(name="サーバー名",value=f"{guild.name}",inline=False)
    embed.add_field(name="サーバー地域",value=f"{ctx.guild.region}",inline=False)
    embed.add_field(name="サーバー設立日",value=guild.created.at,inline=False)
    embed.add_field(name="サーバーオーナー",value=guild.owner,inline=False)
    embed.add_field(name="チャンネル数",value=f"{len(text_channels)}",inline=False)
    embed.add_field(name="ロール数",value=f"{len(roles)}",inline=False)
    embed.add_field(name="サーバーブースト数",value=guild.premium_subscription_count,inline=False)
    embed.add_field(name="メンバー数",value=guild.member_count,inline=False)
    embed.set_footer(text=f"実行者：{ctx.author} ",icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    

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
