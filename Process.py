import requests
import json
import time
import random
from Questions import Questions
from Users import Users

qb = Questions()
users = Users()

token_header = {
    "token": "",
    "memberId": "",
    "mobileTerminal": "0",
    "appversion": "3.0.4",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "js.lgb360.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}


def right_answer(json_dict):
    content_ = ""
    if "data" in json_dict.keys():
        ques_ = json_dict.get("data").get("ques")
        content_ = ques_.get("content")
    return qb.getAnswer(content_)


def process():
    num_ = 1
    num_users = len(users.getUsers())
    for token_data in users.getUsers():
        login_url = 'https://js.lgb360.com/lgb/user/loginByPassword.do'
        ua_ = token_data.get('userAgent')
        if ua_ is None:
            ua_ = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) " \
                  "Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/zh_CN"
        token_header['User-Agent'] = ua_
        token_result = requests.post(login_url, headers=token_header, data=token_data)
        token_dict = json.loads(token_result.text)
        print(token_dict)
        status = token_dict.get("status")
        token_ = ''
        memberId_ = ''
        if status == 20000:
            token_ = token_dict.get("data").get("token")
            memberId_ = token_dict.get("data").get("memberId")
        startComp = "https://aqy-app.lgb360.com/aqy/ques/startCompetition"
        header = {
            "Host": "aqy-app.lgb360.com",
            "accept": "application/json, text/plain, */*",
            "token": "%s" % token_,
            "user-agent": "%s" % ua_,
            "memberid": "%s" % memberId_,
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://aqy-app.lgb360.com",
            "x-requested-with": "com.hxak.liangongbao",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        result = requests.post(startComp, headers=header, data={})
        result_dict = json.loads(result.text)
        msg = result_dict.get("result").get("msg")
        code = result_dict.get("result").get("code")
        if msg == "每天只能挑战一次" and code == 9:
            print("每天只能挑战一次")
            continue

        answerQues = "https://aqy-app.lgb360.com/aqy/ques/answerQues"

        while 1:
            data = result_dict.get("data")
            if data:
                ques = data.get("ques")
                if not ques:
                    print("答题结束")
                    if num_ < num_users:
                        print("处理下个用户")
                        num_ += 1
                    break
                else:
                    quesId = ques.get("quesId")
                    answerOptions = ques.get("options")
            else:
                print("本用户处理结束 处理下个用户")
                break
            rightAnswer = right_answer(result_dict)
            if rightAnswer:
                data = {"quesId": "%s" % quesId, "answerOptions": rightAnswer}
                print("rightAnswer", data)
            else:
                data = {"quesId": "%s" % quesId, "answerOptions": ["%s" % answerOptions[0]]}
                print(answerOptions[0])
            answer = requests.post(answerQues, headers=header, data=json.dumps(data))
            print(answer.text)
            result_dict = json.loads(answer.text)
            time.sleep(random.randint(6, 9))
        time.sleep(5)
