# ��������Ŀ���ģ��
import requests
import re

# ����ѭ������
urls = []
for i in list(range(1,100)):
    urls.append('https://rate.tmall.com/list_detail_rate.htm?itemId=521136254098&spuId=345965243&sellerId=2106525799&order=1&currentPage=%s' %i)
# �����ֶ�����
nickname = []
ratedate = []
color = []
size = []
ratecontent = []

# ѭ��ץȡ����
#for url in urls:
#    content = requests.get(url).text
#    nickname.extend(re.findall('"displayUserNick":"(.*?)"',content))
#    color.extend(re.findall(re.compile('��ɫ����:(.*?);'),content))
#    size.extend(re.findall(re.compile('����:(.*?);'),content))
#    ratecontent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'),content))
#    ratedate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'),content))

# д������
file = open('�ϼ�����è����2.csv','w')
for i in list(range(0,len(nickname))):
    file.write(','.join((nickname[i],ratedate[i],color[i],size[i],ratecontent[i]))+'\n')
file.close()