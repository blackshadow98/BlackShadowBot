"""Emoji



Available Commands:



.emoji shrug



.emoji apple



.emoji :/



.emoji -_-"""



from telethon import events



import asyncio











@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))



async def _(event):



 if event.fwd_from:



 return



 animation_interval = 5



 animation_ttl = range(0, 11)



 input_str = event.pattern_match.group(1)



 if input_str == "dad":



 await event.edit(input_str)



 animation_chars = [



"`Son Founded`",

 "`Mission Finding Your Dad Initiated `",

 "`Finding Your Dad\n\n\nYour Dad' Location Locked\n We are reaching out \n\nAlmost Done... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Finding Your Dad\n\n\nYour Dad' Location Locked\n We are reaching out \n\nAlmost Done...\n\n Percentage... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Finding Your Dad\n\n\nYour Dad' Location Locked\n We are reaching out \n\nAlmost Done...\n\n Percentage... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `", 

"`Finding Your Dad\n\n\nYour Dad' Location Locked\n We are reaching out \n\nAlmost Done...\n\n Percentage... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Finding Your Dad\n\n\nYour Dad' Location Locked\n We are reaching out \n\nAlmost Done...\n\n Percentage... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Finding Your Dad\n\n\nYour Dad' Location Locked\n We are reaching out \n\nAlmost Done...\n\n Percentage... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Finding Your Dad\n\n\nYour Dad' Location Locked\n We are reaching out \n\nAlmost Done...\n\n Percentage... 84%\n█████████████████████▒▒▒▒ `",

 "`Finding Your Dad\n\n\nYour Dad' Location Locked\n We are reaching out \n\nAlmost Done...\n\n Percentage... 100%\n█████████████████████████ `",

 "`Mission accomplished\n\\n\nSuccessfully we found your DAD \n\nResult:Oop's @iaminnocentyaar is Your DAD `"

 ]



 for i in animation_ttl:



 await asyncio.sleep(animation_interval)



 await event.edit(animation_chars[i % 11])



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))



async def _(event):



 if event.fwd_from:



 return



 animation_interval = 0.1



 animation_ttl = range(0, 11)



 input_str = event.pattern_match.group(1)



 if input_str == "sqh":



 await event.edit(input_str)



 animation_chars = [



"`Downloading File..`",

 "`File Downloaded....`",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `", 

"`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nReault: No Virus Found...`"

 ]



 for i in animation_ttl:



 await asyncio.sleep(animation_interval)



 await event.edit(animation_chars[i % 11])





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))



async def _(event):



 if event.fwd_from:



 return



 animation_interval = 5



 animation_ttl = range(0, 11)



 input_str = event.pattern_match.group(1)



 if input_str == "vquickheal":



 await event.edit(input_str)



 animation_chars = [



"`Downloading File..`",

 "`File Downloaded....`",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `", 

"`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",

 "`Quick Heal Total Security Checkup\n\n\nSubscription: Pru User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nReault:⚠️Virus Found⚠️\nMore Info: Torzan, Spyware, Adware`"

 ]



 for i in animation_ttl:



 await asyncio.sleep(animation_interval)



 await event.edit(animation_chars[i % 11])