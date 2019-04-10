import urllib3
import re
import time
from multiprocessing.dummy import Pool

urllib3.disable_warnings()


def download_pic(image_info, http_obj):
        resp = http_obj.request("GET", url=image_info[0])
        with open(r"./images/{}.jpg".format(image_info[1]), "wb") as f:
                f.write(resp.data)
        print("[+] 图片 '{}' 下载完毕".format(image_info[1]))


def main():
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }
        th_pool = Pool()        #创建线程对象
        http = urllib3.PoolManager(headers=headers)     # 为了防止代码重复，在这里加headers是最适合的
        url = 'http://desk.zol.com.cn/pc/'      # 目标爬取网站的地址
        resp = http.request('GET', url=url)
        find_key = re.compile('photo-list-padding.*?src="(.*?\.jpg).*?title = "(.*?)"')
        img_list = find_key.findall(resp.data.decode('gb2312'))
        # print(img_list)
        start_time = time.time()
        for item in img_list:
                # download_pic(item, http)
                th_pool.apply_async(func=download_pic, args=(item, http))
        th_pool.close()
        th_pool.join()
        end_time = time.time()
        print("[+] 总耗时：{}s".format(end_time - start_time))


if __name__ == '__main__':
        main()