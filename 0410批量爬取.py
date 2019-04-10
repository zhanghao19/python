import urllib3, re
from urllib import request

http = urllib3.PoolManager()

resp = http.request('GET', 'http://desk.zol.com.cn/pc/')

# print(resp.status)
find_key = re.compile('<li class="photo-list-padding".*?src="(.*?\.jpg)"')
imglist = find_key.findall(resp.data.decode('gbk'))
print(imglist)
for imgurl in imglist:
        path = re.findall(r'.{10}\.jpg', imgurl)[0]
        request.urlretrieve(imgurl, path)
        # print(imgurl)
        # resp_img = http.request('GET', imgurl, verify=False)
        # img_data = resp_img.data
        # with open(r'{}.jpg'.format(imgurl), 'wb') as f:
        #         f.write(img_data)

