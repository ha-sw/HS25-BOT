import discord, asyncio, datetime, pytz
from discord import member
from discord import message

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("HS25 관리"))


@client.event
async def on_message(message):
    
    if message.content == "!직원현황": # 메세지 감지
        embed = discord.Embed(title="직원현황", description="HS25 직원입니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="\n점장", value="잔액 | 하승운#8347", inline=False)
        embed.add_field(name="\n매니저", value="앤디 | 𝓒𝓱𝓮𝓻𝓲𝓼𝓱#8881", inline=False)
        embed.add_field(name="\n정직원", value="지판다 | 지판다#0702 \n파란앵무새 | 파란앵무새#7973\n귤 | 귤귤#5667\n펭귄수오 | 펭귄수오#4793\n시몬 | 이심원#4113", inline=False)
        embed.add_field(name="\n알바", value=" - ", inline=False)
        embed.add_field(name="\n\n직원모집", value="배너관리 총 책임자 모집중(매니저급).", inline=False)

        embed.set_footer(text="HS25", icon_url="https://media.discordapp.net/attachments/873167914432335963/878924753358954496/-001.png")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/873167914432335963/878924379604521020/-001_6.png")
        await message.channel.send (embed=embed)

    if message.content == "!역할안내": # 메세지 감지
        embed = discord.Embed(title="역할안내", description="HS25 역할입니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="\n점장", value="총관리자", inline=False)
        embed.add_field(name="\n매니저", value="부총관리자", inline=False)
        embed.add_field(name="\n정직원", value="관리자", inline=False)
        embed.add_field(name="\n알바", value="관리자 보조", inline=False)
        embed.add_field(name="\n\n단골손님", value="관리자 지인", inline=False)
        embed.add_field(name="\n손님", value="인증유저", inline=False)
        embed.add_field(name="\n진상손님", value="경고", inline=False)


        embed.set_footer(text="HS25", icon_url="https://media.discordapp.net/attachments/873167914432335963/878924753358954496/-001.png")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/873167914432335963/878924379604521020/-001_6.png")
        await message.channel.send (embed=embed)

    if message.content == "!명령어안내": # 메세지 감지
        embed = discord.Embed(title="명령어 목록", description="HS25봇 명령어 모음입니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="유저명령어", value="유저가 사용가능한 명령어입니다.", inline=False)
        embed.add_field(name="대답", value="유저에 말에 등록된 답변을 합니다.\n\n 안녕 :: 인사대답\n 안녕하세요 :: 인사대답\n 서버안내 :: 짧은서버소개 ", inline=False)
        embed.add_field(name="명령어", value="특정 명령어를 사용하면 반응합니다.\n\n!직원현황 :: 직원현황 안내\n!명령어안내 :: 명령어 목록", inline=False)
        
        embed.set_footer(text="HS25", icon_url="https://media.discordapp.net/attachments/873167914432335963/878924753358954496/-001.png")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/873167914432335963/878924379604521020/-001_6.png")
        await message.channel.send (embed=embed)

    if message.content == "!봇온": # 메세지 감지
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
             embed = discord.Embed(title="봇 현황", description="\n",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

             embed.add_field(name="봇 상태", value=":green_circle: | 봇 ON", inline=False)
             
             embed.set_footer(text="HS25", icon_url="https://media.discordapp.net/attachments/873167914432335963/878924753358954496/-001.png")
             embed.set_thumbnail(url="https://media.discordapp.net/attachments/873167914432335963/878924379604521020/-001_6.png")
             await message.channel.send ("@everyone", embed=embed)
             

    if message.content == "!봇오프": # 메세지 감지
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
             embed = discord.Embed(title="봇 현황", description="\n",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

             embed.add_field(name="봇 상태", value=":red_circle: | 봇 OFF", inline=False)
             
             embed.set_footer(text="HS25", icon_url="https://media.discordapp.net/attachments/873167914432335963/878924753358954496/-001.png")
             embed.set_thumbnail(url="https://media.discordapp.net/attachments/873167914432335963/878924379604521020/-001_6.png")
             await message.channel.send ("@everyone", embed=embed)
        


    if message.content.startswith ("!인증 "):
        if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="HS25")
            await message.channel.send(embed=embed)
            role = discord.utils.get(message.guild.roles, name = '손님')
            await user.add_roles(role)

        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))\

    if message.content.startswith ("!뮤트 "):
        if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="뮤트 시스템", description="채팅을 칠수없습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="뮤트 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="HS25")
            await message.channel.send(embed=embed)
            role = discord.utils.get(message.guild.roles, name = '뮤트')
            await user.add_roles(role)


        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))

    if message.content.startswith ("!경고1 "):
        if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="경고 시스템", description="경고 부여가 정상적으로 완료되었습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="경고 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="HS25")
            await message.channel.send(embed=embed)
            role = discord.utils.get(message.guild.roles, name = '진상손님 L1')
            await user.add_roles(role)


        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))

    if message.content.startswith ("!경고2 "):
        if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="경고 시스템", description="경고 부여가 정상적으로 완료되었습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="경고 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="HS25")
            await message.channel.send(embed=embed)
            role = discord.utils.get(message.guild.roles, name = '진상손님 L2')
            await user.add_roles(role)


        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))
    
    if message.content.startswith ("!경고3 "):
        if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="경고 시스템", description="경고 부여가 정상적으로 완료되었습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="경고 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="HS25")
            await message.channel.send(embed=embed)
            role = discord.utils.get(message.guild.roles, name = '진상손님 L3')
            await user.add_roles(role)


        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))
    


    if message.content.startswith ("!공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(873174451028631632)
            embed = discord.Embed(title="**HS25 공지사항**", description="\n=====\n\n**{}**\n\n=====".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')),color=0x00ff00)
            embed.set_footer(text="HS25 | 담당 관리자 : {}".format(message.author), icon_url="https://media.discordapp.net/attachments/873167914432335963/878924753358954496/-001.png")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/873167914432335963/878924379604521020/-001_6.png")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("*[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

    if message.content.startswith ("!업데이트"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[5:]
            channel = client.get_channel(873174866562523166)
            embed = discord.Embed(title="**HS25 업데이트**", description="\n=====\n\n**{}**\n\n=====\n[A] = 추가 | [M] = 제거 | [R] = 수정\n===== ".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')),color=0x00ff00)
            embed.set_footer(text="HS25 | 담당 관리자 : {}".format(message.author), icon_url="https://media.discordapp.net/attachments/873167914432335963/878924753358954496/-001.png")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/873167914432335963/878924379604521020/-001_6.png")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("*[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))


    if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="HS25", icon_url="https://media.discordapp.net/attachments/873167914432335963/878924753358954496/-001.png")
            await message.channel.send(embed=embed)
            await message.channel.purge(limit=1)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

    
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))
            
    if message.content == "안녕": # 메세지 감지
     await message.channel.send ("{}님 안녕하세요.".format(message.author.mention))
        
    if message.content == "안녕하세요": # 메세지 감지
     await message.channel.send ("{}님 안녕하세요.".format(message.author.mention)) 
 
    if message.content == "서버안내": # 메세지 감지
     await message.channel.send ("저희서버는 커뮤니티 중심 편의점 컨셉의 디스코드서버입니다.") 

    if message.content == "잔액게이": # 메세지 감지
     await message.channel.send ("잔액게이아니다.") 

    

    

    


    

    



  

     


    

    
             





client.run('ODc4OTA5NTg4ODM2MDg5OTE3.YSICVw.02vCcOGpP_U7yJLMEPljfmXLNtE')