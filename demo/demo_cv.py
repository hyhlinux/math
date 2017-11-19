#coding:utf-8
import datetime
import cv2
import os
from log import get_log

# timeF = 10  # 视频帧计数间隔频率
logger = get_log("pig_cv")
# logger = get_log("zip")

# todo 每5帧采集1张
# time_fz = 5
time_fz = 1


def zip_dir(dst_dir):
    if not dst_dir:
        return
    cmd = "zip -r {}.zip {}".format(dst_dir, dst_dir)
    logger.debug(cmd)
    os.system(cmd)


def get_photo_by_video(video_path="", photo_dir=""):
    if not all([video_path, photo_dir]):
        return

    vc = cv2.VideoCapture(video_path)  # 读入视频文件
    if vc.isOpened():  # 判断是否正常打开
        rval, frame = vc.read()
    else:
        rval = False

    if not rval:
        return

    start_time = datetime.datetime.now()
    video_photo_num = 1

    fz = 0
    while rval:  # 循环读取视频帧
        rval, frame = vc.read()
        if fz % time_fz != 0:  # 每隔timeF帧进行存储操作
            fz += 1
            continue

        if not rval:
            break

        file_name = os.path.join(photo_dir,  "{}.jpg".format(video_photo_num))
        cv2.imwrite(file_name, frame)  # 存储为图像
        video_photo_num += 1
        now = datetime.datetime.now()
        logger.debug('now:{} mp4:{}  photo_num:{}'.format(now-start_time, video_path, file_name))
        cv2.waitKey(1)
    else:
        vc.release()

def main():
    video_dir = "../train"
    dst_photo_dir = os.path.join(video_dir, "dst_photo")
    if not os.path.exists(dst_photo_dir):
        os.mkdir(dst_photo_dir)

    g = os.walk(video_dir)
    for path, d, file_list in g:
        for file_name in file_list:
            if not file_name.endswith(".mp4"):
                # 只处理mp4
                continue
            photo_dir = os.path.join(dst_photo_dir, file_name[:len(file_name)-4])
            if not os.path.exists(photo_dir):
                os.mkdir(photo_dir)
            if not d:
                src_video_path = os.path.join(video_dir, d[0], file_name)
            else:
                src_video_path = os.path.join(video_dir, file_name)

            # 采集图片数据
            # get_photo_by_video(src_video_path, photo_dir)
            # 批量压缩
            # logger.debug("zip_photo_dir:{}".format(photo_dir))
            # zip_dir(photo_dir)
            logger.debug("d:{} src_video_path:{} photo_dir:{}".format(d, src_video_path, photo_dir))

if __name__ == '__main__':
    # logger.info('hello')
    main()