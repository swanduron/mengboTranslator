import json
# text = '''
# {"returnPhrase":["good"],"query":"good","errorCode":"0","l":"en2zh-CHS","tSpeakUrl":"https://openapi.youdao.com/ttsapi?q=%E5%A5%BD&langType=zh-CHS&sign=3E73CE7224412A8D624338B126E046CA&salt=1643433358740&voice=4&format=mp3&appKey=0cb9e41da38052c8&ttsVoiceStrict=false","web":[{"value":["好的","善","良好","商品"],"key":"good"},{"value":["心灵捕手","骄阳似我","心魄捕手"],"key":"Good Will Hunting"},{"value":["很好","非常好","相当好","好极了"],"key":"Very Good"}],"requestId":"596cbb34-9b1d-4dd3-821e-a8f40538798b","translation":["好"],"dict":{"url":"yddict://m.youdao.com/dict?le=eng&q=good"},"webdict":{"url":"http://mobile.youdao.com/dict?le=eng&q=good"},"basic":{"exam_type":["初中","高中","CET4","CET6","考研"],"us-phonetic":"ɡʊd","phonetic":"ɡʊd","uk-phonetic":"ɡʊd","wfs":[{"wf":{"name":"复数","value":"goods"}},{"wf":{"name":"比较级","value":"better"}},{"wf":{"name":"最高级","value":"best"}}],"uk-speech":"https://openapi.youdao.com/ttsapi?q=good&langType=en&sign=A8EEC6D9D91E4AD900217FF694C7B4B6&salt=1643433358740&voice=5&format=mp3&appKey=0cb9e41da38052c8&ttsVoiceStrict=false","explains":["adj. 好的，优良的；能干的，擅长的；好的，符合心愿的；令人愉快的，合意的；（心情）愉快的；迷人的，漂亮的；可能会成功的，可能正确的；合适的，方便的；有益的，有好处的，有用的；温顺的，乖的，有礼貌的；虔诚的，遵守规则（或约定）的；健康的，健全的；状况好的；助人为乐的，心地善良的，好心的；符合道德的，正派的，高尚的；（数量或程度）相当大的，相当多的；很，非常；彻底的，完全的；合情理的，有说服力的，有充分根据的；划算的，收益可观的；赞同的，赢得赞许的，令人尊敬的；（用于表示回应）好的；表示惊讶、生气或者加强语气；（用于打招呼）好；至少，不少于；有趣的，逗笑的；在…时间内有效，非伪造的；（比赛中打的球）好的，有效的，可以得分的；（踢、射、投）命中；能提供……的；足够支付的；上流的，高贵的；（衣服）时髦的，适合正式场合穿着的；亲密的，友好的；尤指以屈尊俯就或幽默的方式好（人）；有……意向的；够了，到此为止了；精确的，准确的","n. 合乎道德的行为，正直的行为，善行；对的事情（the good）；好事（the good）；好的方面；好结果；有道德的人，高尚的人，好人（the good）；用处，益处，利益；商品，所有物；<英>（与乘客相区别的）待运货物（goods）；私人财物（goods）；<非正式>真货，正品（the goods）","adv. <非正式>好地；<美>彻底地，完全地","【名】 （Good）（英）古德，（瑞典）戈德（人名）"],"us-speech":"https://openapi.youdao.com/ttsapi?q=good&langType=en&sign=A8EEC6D9D91E4AD900217FF694C7B4B6&salt=1643433358740&voice=6&format=mp3&appKey=0cb9e41da38052c8&ttsVoiceStrict=false"},"isWord":true,"speakUrl":"https://openapi.youdao.com/ttsapi?q=good&langType=en&sign=A8EEC6D9D91E4AD900217FF694C7B4B6&salt=1643433358740&voice=4&format=mp3&appKey=0cb9e41da38052c8&ttsVoiceStrict=false"}
#
# '''
# with open('json.json', 'w') as file_obj:
#     json_obj = json.loads(text)
#     json.dump(json_obj, file_obj, indent=2)

with open('json.json') as file_obj:
    json_obj = json.load(file_obj)

res = {
    'word': json_obj['query'],
    'translation': json_obj.get('web'),
    'pronounce-us': json_obj.get('basic').get('us-phonetic'),
    'pronounce-uk': json_obj.get('basic').get('uk-phonetic'),
       }

print(res)