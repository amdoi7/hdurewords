import re
import os
import json
import time
import uuid
import requests

from gettoken import token


def get_an(msg):
    url = "https://aicursor.com/conversation"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Cursor/0.1.0 Chrome/108.0.5359.62 Electron/22.0.0 Safari/537.36",
        "content-type": "application/json",
        "sec-fetch-site": "cross-site",
        "sec-fetch-type": "cors",
        "sec-fetch-dest": "empty",
        # 'authorization': 'Bearer '
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN"
    }
    payload = {
        "userRequest": {
            "message": msg,
            "currentFileContents": '',
            "precedingCode": [],
            "currentSelection": None,
            "suffixCode": [],
            "copilotCodeBlocks": [],
            "customCodeBlocks": [],
            "codeBlockIdentifiers": [],
            "msgType": "freeform",
            "maxOrigLine": None
        },
        "userMessages": [
            {
                "sender": "user",
                "sentAt": 1679800699667,
                "message": "give the titles  and  correct  answer\n\"title\":\"equipment.\",\n\"answerA\":\"等价物.\",\n\"answerB\":\"等式.\",\n\"answerC\":\"设备.\",\n\"answerD\":\"相等物.\",\n\"title\":\"ambitious.\",\n\"answerA\":\"模糊的.\",\n\"answerB\":\"有雄心的.\",\n\"answerC\":\"宽敞的.\",\n\"answerD\":\"权威的.\",\n\"title\":\"avert.\",\n\"answerA\":\"开始.\",\n\"answerB\":\"避免.\",\n\"answerC\":\"授权.\",\n\"answerD\":\"使挫折.\",\n\"title\":\"点头.\",\n\"answerA\":\"shake.\",\n\"answerB\":\"shriek.\",\n\"answerC\":\"nod.\",\n\"answerD\":\"tremble.\",\n\"title\":\"attendant.\",\n\"answerA\":\"护理人员.\",\n\"answerB\":\"出席者.\",\n\"answerC\":\"被告人.\",\n\"answerD\":\"资质.\",\n\"title\":\"round.\",\n\"answerA\":\"圆形的.\",\n\"answerB\":\"旋转的.\",\n\"answerC\":\"粗略的.\",\n\"answerD\":\"弯曲的.\",\n\"title\":\"athlete.\",\n\"answerA\":\"健康.\",\n\"answerB\":\"忍受.\",\n\"answerC\":\"徽章.\",\n\"answerD\":\"运动员.\",\n\"title\":\"摘要.\",\n\"answerA\":\"summary.\",\n\"answerB\":\"summer.\",\n\"answerC\":\"supper.\",\n\"answerD\":\"superficial.\",\n\"title\":\"使同化.\",\n\"answerA\":\"affiliate.\",\n\"answerB\":\"absorb.\",\n\"answerC\":\"assimilate.\",\n\"answerD\":\"accumulate.\",\n\"title\":\"机构，团体.\",\n\"answerA\":\"instinction.\",\n\"answerB\":\"inspiration.\",\n\"answerC\":\"institution.\",\n\"answerD\":\"indication.\",\n\"title\":\"straight.\",\n\"answerA\":\"确定的.\",\n\"answerB\":\"奇怪的.\",\n\"answerC\":\"稳定的.\",\n\"answerD\":\"坦率的.\",\n\"title\":\"在远处的.\",\n\"answerA\":\"accessible.\",\n\"answerB\":\"securable.\",\n\"answerC\":\"distant.\",\n\"answerD\":\"available.\",\n\"title\":\"adjacent.\",\n\"answerA\":\"调整的.\",\n\"answerB\":\"有雄心的.\",\n\"answerC\":\"足够的.\",\n\"answerD\":\"毗邻的.\",\n\"title\":\"amend.\",\n\"answerA\":\"修正.\",\n\"answerB\":\"增强.\",\n\"answerC\":\"分辨.\",\n\"answerD\":\"管理.\",\n\"title\":\"amends.\",\n\"answerA\":\"古物.\",\n\"answerB\":\"附录.\",\n\"answerC\":\"赔偿.\",\n\"answerD\":\"标志.\",\n\"title\":\"alongside.\",\n\"answerA\":\"在...里面.\",\n\"answerB\":\"在...外面.\",\n\"answerC\":\"在...上面.\",\n\"answerD\":\"在...旁边.\",\n\"title\":\"speech.\",\n\"answerA\":\"范围.\",\n\"answerB\":\"速度.\",\n\"answerC\":\"演讲.\",\n\"answerD\":\"专业.\",\n\"title\":\"outer.\",\n\"answerA\":\"外面的.\",\n\"answerB\":\"外出者.\",\n\"answerC\":\"出局的.\",\n\"answerD\":\"落后的.\",\n\"title\":\"workshop.\",\n\"answerA\":\"办公室.\",\n\"answerB\":\"助手.\",\n\"answerC\":\"团建.\",\n\"answerD\":\"研讨会.\",\n\"title\":\"（值得注意的）事物.\",\n\"answerA\":\"someone.\",\n\"answerB\":\"something.\",\n\"answerC\":\"sometime.\",\n\"answerD\":\"somewhat.\",",
                "conversationId": "5833b9ba-0a60-472e-8593-fb3549737c38",
                "msgType": "freeform"
            },
        ],
        "botMessages": [
            {
                "sender": "bot",
                "sentAt": 1679800700472,
                "conversationId": "5833b9ba-0a60-472e-8593-fb3549737c38",
                "type": "markdown",
                "message": "The titles and correct answers are:\n- equipment. : \"设备.\"\n- ambitious. : \"有雄心的.\"\n- avert. : \"避免.\"\n- nod. : \"点头.\"\n- attendant. : \"护理人员.\"\n- round. : \"圆形的.\"\n- athlete. : \"运动员.\"\n- abstract. : \"summary.\"\n- assimilate. : \"同化.\"\n- institution. : \"机构，团体.\"\n- straight. : \"坦率的.\"\n- distant. : \"在远处的.\"\n- adjacent. : \"毗邻的.\"\n- amend. : \"修正.\"\n- amends. : \"赔偿.\"\n- alongside. : \"在...旁边.\"\n: speech. - \"演讲.\"\n: - outer. : \"外面的.\"\n- workshop. : \"研讨会.\"\n- something. : \"值得注意的事物.",
                "lastToken": "<|END_message|>",

            }
        ],
        "contextType": "copilot",
        "rootPath": r"C:\Users\HP\cursor-tutor"
    }
    res = []

    while not len(res):
        response = requests.request("POST", url, json=payload, headers=headers).content.decode("unicode_escape")

        response = re.sub(r'data:|"|\n| |\.', "", response)
        print(response)
        # 正则匹配  -(.+?)-(.+?)(?=\-|<)

        res = re.findall(r'-(.+?):(.+?)(?=\-|<)',
                            response, re.S)
        # if not res:
        #     res = re.findall(r'-(.+?)-(.+?)(?=\-|<)',
        #                      response, re.S)
        print(res)
    return res


class REWORDS:

    def get_mark(self, paperid):
        response = requests.get(
            "https://skl.hdu.edu.cn/api/paper/detail?paperId=" + paperid,
            headers=self._get_headers)
        print(f"得分：{json.loads(response.text)['mark']} 耗时：{json.loads(response.text)['totalTime'] / 1000}秒")

    def paper_data(self, type=0, week=6):
        # 获取当前时间戳
        timestamp = int(time.time() * 10000)
        response = requests.get(
            f'https://skl.hdu.edu.cn/api/paper/new?type={type}&week={week}&startTime=' + str(timestamp),
            headers=self._get_headers)
        return json.loads(response.text)

    @staticmethod
    def post_data(answer, x_token):
        url = 'https://skl.hdu.edu.cn/api/paper/save'

        postHeaders = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Host': 'skl.hdu.edu.cn',
            'Origin': 'https://skl.hduhelp.com',
            'Referer': 'https://skl.hduhelp.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-type': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'skl-ticket': str(uuid.uuid1()),
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
            'X-Auth-Token': x_token
        }
        requests.post(url, headers=postHeaders, data=answer)

    def __init__(self, user_id='', user_password='',
                    mode=0, week=1, delay=0):
        self._get_headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'skl.hdu.edu.cn',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': "Android",
            'Origin': 'https://skl.hduhelp.com',
            'Pragma': 'no-cache',
            'Referer': 'https://skl.hduhelp.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-type': 'no-cors',
            'Sec-Fetch-Site': 'cross-site',
            # 获取当前uuid（测试发现是uuid1）
            'skl-ticket': str(uuid.uuid1()),
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
            # 自己的token
            'X-Auth-Token': ''
        }
        if not all([user_id, user_password]): return
        print('********正在登录中********')
        self._X_Auth_Token = token(user_id, user_password)
        self._get_headers.update({'X-Auth-Token': self._X_Auth_Token})
        print('********登录成功！********')
        self._paper = self.paper_data(mode, week)
        # FIXME 20最稳定
        with open(os.path.dirname(os.path.abspath(__file__)) + '/src/answerList', 'r') as f:
            answer_source = f.read()
        self._answer_dict = json.loads(answer_source)
        self._loopStep = 20

        if len(self._paper.get('list', [])) == 100:
            print("成功获取题目！！！")
        else:
            print(self._paper)
            return
        self._papermsg = str(self._paper['list'])
        self._answer_dict['paperId'] = self._paper['paperId']
        print('********正在答题中********')
        qtext = re.findall(r"'title'.*?(?='questionId')", self._papermsg.replace(" ", "").replace(".", ""), re.S)
        print(len(qtext))

        index = 0
        for _ in range(100 // self._loopStep):
            msg = 'give the titles  and  correct  answer\n'

            for i in range(index, index + self._loopStep):
                msg += qtext[i]
            # print(msg)
            res = get_an(msg)
            for i in range(index, index + self._loopStep):

                t = re.sub(r' |\.|\"|\'', "", qtext[i]).split(",")
                try:
                    an = res[i % self._loopStep]
                except IndexError:
                    an = ['114', '514']
                print(an, t)

                self._answer_dict['list'][i]['input'] = 'C'
                for j in range(4):
                    if any(t[j + 1].split(":")[1] in a for a in an):
                        self._answer_dict['list'][i]['input'] = chr(ord('A') + j)

                self._answer_dict['list'][i]['paperDetailId'] = self._paper['list'][i]['paperDetailId']
            index += self._loopStep
        time.sleep(60 * delay)
        self.post_data(json.dumps(self._answer_dict), self._X_Auth_Token)
        self._get_headers.update({'skl-ticket': str(uuid.uuid1()), })
        self.get_mark(self._paper['paperId'])
