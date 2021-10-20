import aip

def emo() :
    client_appId = '25004504'
    client_apiKey = '3TFg3faCWVBiCy8eSQ93PoEz'
    client_secretKey = 'F6rDKNQhwmUNwMXZBuyGN52Zh5p0GQC3'

    lyrics = ''

    with open('../speech_txt/lyrics.txt', "r", encoding='utf-8') as f:
        lyrics = f.read()

    # print(lyrics)

    # 调用自然语言处理api
    my_nlp = aip.nlp.AipNlp(client_appId, client_apiKey, client_secretKey)

    # sentimentClassify(self, text, options=None)
    result = my_nlp.sentimentClassify(lyrics)

    print(result)

    positive_prob = float(result['items'][0]['positive_prob'])
    confidence = float(result['items'][0]['confidence'])
    negative_prob = float(result['items'][0]['negative_prob'])

    print('positive_prob: ', positive_prob)
    print('confidence: ',  confidence)
    print('negative_prob: ', negative_prob)
