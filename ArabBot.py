#صغصفصف
#العربية
#Шустрик)

import discord as dc
from translate import Translator

class ArabBot(dc.Client):
    async def on_message(self, message):
        m = '{0.content}'.format(message)
        if m[0] == '&':
            b_m = ''
            for i in range(len(m)-1):
                b_m += m[i+1]
            tr = Translator(from_lang='Russian', to_lang='Arabic')
            b_answer = tr.translate(b_m)
            print(b_answer)
            await message.channel.send(b_answer)
        if m[0] == '%':
            b_m = ''
            for i in range(len(m)-1):
                b_m += m[i+1]
            tr = Translator(from_lang='Arabic', to_lang='Russian')
            b_answer = tr.translate(b_m)
            print(b_answer)
            await message.channel.send(b_answer)

ArabBot().run('ODMxMTQxNTU5OTczMDUyNDM2.YHQ65Q.P3UDdRJCMDrlC2JX1A7C3Z5SRDo')