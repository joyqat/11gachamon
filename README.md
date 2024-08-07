本仓库提供的脚本可以连续采集中奖名单的滚动播报。

依赖为requests。
在浏览器中打开相应的API页面并登录，然后复制并替换py文件中的COOKIE，并设置适当的输出文件路径，使用python运行脚本即可。

活动ID自己想办法抓http包，或者通过活动页面确认，例如本次嫦娥的页面为https://rpgact.5211game.com/lotteryTemplate/#/110154。

采集的数据来源于滚动播报，采集的数据可以使用提供的xlsx文件处理汇总。

例如本次嫦娥的数据。
![image](https://github.com/user-attachments/assets/0ab723d2-416f-457f-9bd2-54504cfbe4e6)

以及采集了一天的鸣人池。
![image](https://github.com/user-attachments/assets/0475b1f8-04ca-4c45-8e50-d772e65d0774)

希望大家可以参与进来，判断一下概率是否真实。

### 数据统计表格的使用方法
使用EXCEL 2019以上的版本，（最好是365之类的），选择数据->查询和连接->output->编辑->右侧边栏中选择源的设置->修改数据文件路径到上面设置的csv路径

![image](https://github.com/user-attachments/assets/2d9e67dd-8dd5-4476-9038-cdd9bebd7645)

数据有更新后只需要点 数据->全部刷新 （需要刷新两次，因为第二次才会刷新统计表格）
