import json
import logging
import package.xmltodict as xmltodict
import urllib.request

# Logging Setting
logger = logging.getLogger()
logger.setLevel('INFO')


def lambda_handler(event, context):
    
    # jmaURL
    jmaURL = "https://www.data.jma.go.jp/"
    
    #URL パラメータ
    param = event.get('queryStringParameters')
    
    logger.info(param)
    
    isExistsUrl = param != None
    
    # XMLデータの取得
    # デフォルトURL
    url = "https://www.data.jma.go.jp/developer/xml/feed/regular.xml"
    
    # URL指定があれば設定
    if isExistsUrl:
        if param['url'] != None:
            url = str(param['url'])
        else:
            return {
                'statusCode': 400,
                'body': "ParameterError"
            }       
    
    with urllib.request.urlopen(url) as res:
        xml_data = res.read()
        
        # XMLから辞書型に変換
        dict_data = xmltodict.parse(xml_data)
        
        # 辞書型をJSON形式に変換
        json_data = json.dumps(dict_data, ensure_ascii=False, indent=4)
        
        logger.info(json_data)
    
        return {
            'statusCode': 200,
            'body': json_data
        }

