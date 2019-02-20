"""
  created by IAmFiveHigh on 2019-02-20
 """

from . import web
from app.models.goods import Good


@web.route('/good')
def good():
    json = {
        "id": "15",
        "title": "iPhone X 全面屏 全面绽放",
        "descr": "",
        "oldPrice": "8316",
        "nowPrice": "7799",
        "lowerPrice": "203.97/周",
        "createTime": "12/02/2018 10:18:23",
        "activityEndTime": "02/19/2019 00:00:00",
        "tags": "零元购机,闪电发货,按需付租,正品保证",
        "tagIds": "4,3,2,1",
        "step": "http://47.92.123.35:22222//0/1543911293572.jpg",
        "content": "<p><img src=\"http://47.92.123.35:22222/ueditor/1543911313470.jpg\" style=\"\" title=\"11.jpg\"/></p><p><img src=\"http://47.92.123.35:22222/ueditor/1543911352190.jpg\" style=\"\" title=\"22.jpg\"/></p><p><img src=\"http://47.92.123.35:22222/ueditor/1543911355560.jpg\" style=\"\" title=\"33.jpg\"/></p><p><img src=\"http://47.92.123.35:22222/ueditor/1543911359125.jpg\" style=\"\" title=\"44.jpg\"/></p><p><img src=\"http://47.92.123.35:22222/ueditor/1543911363274.jpg\" style=\"\" title=\"55.jpg\"/></p><p><img src=\"http://47.92.123.35:22222/ueditor/1543911367384.jpg\" style=\"\" title=\"66.jpg\"/></p><p><img src=\"http://47.92.123.35:22222/ueditor/1543911371825.jpg\" style=\"\" title=\"77.jpg\"/></p><p><img src=\"http://47.92.123.35:22222/ueditor/1543911375799.jpg\" style=\"\" title=\"88.jpg\"/></p><p><br/></p>",
        "params": "[{\"h1\":\"主体\",\"list\":[{\"key\":\"品牌\",\"value\":\"Apple\"},{\"key\":\"型号\",\"value\":\"iPhone X\"},{\"key\":\"入网型号\",\"value\":\"A1865\"},{\"key\":\"上市年份\",\"value\":\"2017年\"},{\"key\":\"上市月份\",\"value\":\"11月\"}]},{\"h1\":\"基本信息\",\"list\":[{\"key\":\"机身颜色\",\"value\":\"深空灰/银色\"},{\"key\":\"机身长度（mm）\",\"value\":\"143.6\"},{\"key\":\"机身宽度（mm）\",\"value\":\"70.9\"},{\"key\":\"机身厚度（mm）\",\"value\":\"7.7\"},{\"key\":\"机身重量（g）\",\"value\":\"174\"},{\"key\":\"运营商标志或内容\",\"value\":\"其他\"},{\"key\":\"机身材质分类\",\"value\":\"其他\"}]},{\"h1\":\"操作系统\",\"list\":[{\"key\":\"操作系统\",\"value\":\"ios\"}]},{\"h1\":\"主芯片\",\"list\":[{\"key\":\"CPU品牌\",\"value\":\"以官网信息为准\"},{\"key\":\"CPU频率\",\"value\":\"以官网信息为准\"},{\"key\":\"CPU核数\",\"value\":\"其他\"},{\"key\":\"CPU型号\",\"value\":\"其他\"}]},{\"h1\":\"网络支持\",\"list\":[{\"key\":\"双卡机类型\",\"value\":\"单卡\"},{\"key\":\"最大支持SIM卡数量\",\"value\":\"1个\"},{\"key\":\"SIM卡类型\",\"value\":\"Nano SIM\"},{\"key\":\"4G网络\",\"value\":\"4G：移动（TD-LTE)；4G：电信(FDD-LTE)；4G：联通(TD-LTE)\"},{\"key\":\"3G/2G网络\",\"value\":\"--\"},{\"key\":\"网络频率（2G/3G）\",\"value\":\"--\"},{\"key\":\"是否支持同时使用联通卡\",\"value\":\"不支持\"}]},{\"h1\":\"存储\",\"list\":[{\"key\":\"ROM\",\"value\":\"64GB/256GB\"},{\"key\":\"RAM\",\"value\":\"其他\"},{\"key\":\"存储卡\",\"value\":\"不支持\"}]},{\"h1\":\"屏幕\",\"list\":[{\"key\":\"主屏幕尺寸（英寸）\",\"value\":\"5.8英寸\"},{\"key\":\"分辨率\",\"value\":\"2436×1125\"},{\"key\":\"屏幕材质类型\",\"value\":\"其他\"}]},{\"h1\":\"前置摄像头\",\"list\":[{\"key\":\"前置摄像头\",\"value\":\"700万像素\"},{\"key\":\"前摄光圈大小\",\"value\":\"f/2.2\"}]},{\"h1\":\"后置摄像头\",\"list\":[{\"key\":\"摄像头数量\",\"value\":\"2个\"},{\"key\":\"后置摄像头\",\"value\":\"双1200万像素\"}]},{\"h1\":\"电池信息\",\"list\":[{\"key\":\"电池容量（mAh）\",\"value\":\"以官网信息为准\"},{\"key\":\"电池是否可拆卸\",\"value\":\"否\"},{\"key\":\"充电器\",\"value\":\"其他\"}]},{\"h1\":\"数据接口\",\"list\":[{\"key\":\"数据传输接口\",\"value\":\"WIFI；蓝牙；WiFi热点\"},{\"key\":\"NFC/NFC模式\",\"value\":\"其他\"},{\"key\":\"耳机接口类型\",\"value\":\"Lightning\"},{\"key\":\"充电接口类型\",\"value\":\"Lightning（iPhone）\"}]},{\"h1\":\"手机特性\",\"list\":[{\"key\":\"指纹识别\",\"value\":\"不支持\"},{\"key\":\"GPS\",\"value\":\"支持\"},{\"key\":\"陀螺仪\",\"value\":\"其他\"}]},{\"h1\":\"辅助功能\",\"list\":[{\"key\":\"常用功能\",\"value\":\"其他\"}]}]",
        "images": "http://kernel.yunqihui.net:22222//0/1546572480784.jpg;http://kernel.yunqihui.net:22222//0/1546572484378.jpg;http://kernel.yunqihui.net:22222//0/1546572488687.jpg;http://kernel.yunqihui.net:22222//0/1546572492161.jpg;",
        "icon": "http://kernel.yunqihui.net:22222//0/1546572473389.png",
        "innerIcon": "http://47.92.123.35:22222//0/1543717086749.jpg",
        "liTags": "http://47.92.123.35:22222//0/1543717091296.png",
        "shareTitle": "",
        "shareDescr": "",
        "shareIcon": "",
        "accident": "",
        "sort": "18",
        "del": "0",
        "safExplain": "",
        "bargainMoney": "",
        "bargainPercent": "",
        "bargainNum": "",
        "bargain": "0",
        "bargainSelect": "0",
        "shareLink": "",
        "shareOpen": "",
        "nowTime": "2019-02-20 15:30:11",
        "tagSafe": "http://kernel.yunqihui.net:22222//0/1550225139384.png",
        "saleCount": "0"
    }
    model = Good()

    return '<p>good</p>'


