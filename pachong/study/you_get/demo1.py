import sys
from you_get import common as you_get

#  设置下载目录
directory=r'mp4\\'
#  要下载的视频地址
url='https://www.bilibili.com/video/BV1Vq4y197dH?spm_id_from=333.999.0.0'
#  传参数
sys.argv=['you-get','-o',directory,'--format=flv',url]
you_get.main()
