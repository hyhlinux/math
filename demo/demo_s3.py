import boto
import os
import boto.s3.connection

access_key = os.getenv("S3_PUREAPK_COM_ACCESS_KEY")
secret_key = os.getenv("S3_PUREAPK_COM_SECRET_KEY")
host = os.getenv("S3_PUREAPK_COM")

print(host, access_key, secret_key)
# conn = boto.connect_s3(
#     aws_access_key_id=access_key,
#     aws_secret_access_key=secret_key,
#     host=host,
#     # is_secure=False,               # uncomment if you are not using ssl
#     calling_format=boto.s3.connection.OrdinaryCallingFormat(),
# )
# print(conn)

# for bucket in conn.get_all_buckets():
#     print("{name}\t{created}".format(
#         name=bucket.name,
#         created=bucket.creation_date,
#     ))
#     if bucket.name == "user":
#         print("yes bucket:{}".format(bucket))
#         for key in bucket.list():
#             print("bucket:{buck} {name}\t{size}\t{modified}\t\t{acl}".format(
#                 buck=bucket.name,
#                 name=key.name,
#                 size=key.size,
#                 modified=key.last_modified,
#                 acl="r",
#             ))
# pre="avatar/Mjk5ODM0XzIwMTcwNTMxMDkwNTM2LnBuZ18yMDE3MDUzMTA2MDUzMTQ1Mg.png"
# pre="Y29tLmlsb2VuLm1lbG9uX3NjcmVlbl8wXzNmaHZwYmlj"
# for key in bucket.list(prefix=pre):
#     print key.name
#     print key
#     print key.get_acl()
#     data = key.read()
#     print len(data)
#     with open(pre, "w") as f:
#         f.write(data)
preList = [
    "Y29tLmFuZHJvaWQuY2hyb21lX2ljb25fMzIwMjA4NDAxX2hmZTBuZDBs",
    # 299834_20170531090536.png_20170531060531452
    # "Mjk5ODM0XzIwMTcwNTMxMDkwNTM2LnBuZ18yMDE3MDUzMTA2MDUzMTQ1Mg.png",
    # 357888_20170528120503.png_20170528170505119
    # "MzU3ODg4XzIwMTcwNTI4MTIwNTAzLnBuZ18yMDE3MDUyODE3MDUwNTExOQ.png",
    # 362084_20170530122307.png_20170530172309187
    # "MzYyMDg0XzIwMTcwNTMwMTIyMzA3LnBuZ18yMDE3MDUzMDE3MjMwOTE4Nw.png",
    # 273897_20170504141832.png_20170504091842173
    # "MjczODk3XzIwMTcwNTA0MTQxODMyLnBuZ18yMDE3MDUwNDA5MTg0MjE3Mw.png",
    # "MzAwODIwXzIwMTcwNTI3MTMwMzAwLnBuZ18yMDE3MDUyNzIwMDMwMjEwMA.png",
    # "avatar/MzYyMDg0XzIwMTcwNTMwMTIyMjMzLnBuZ18yMDE3MDUzMDE3MjIzODA4MQ"
]


def main():
    conn = boto.connect_s3(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        host=host,
        # is_secure=False,               # uncomment if you are not using ssl
        calling_format=boto.s3.connection.OrdinaryCallingFormat(),
    )

    if not conn:
        print("conn:", conn)
        return

    bucket = conn.get_bucket("image")
    print(bucket)
    for pre in preList:
        # pre = "avatar/" + pre
        key = bucket.get_key(pre)
        if not key:
            continue
        print(key)
        data = key.read()
        print('len:', len(data))
        with open('/tmp/'+pre, "w") as f:
            f.write(str(data))
        
        # print(key, key.get_acl(), key.set_acl(""))
if __name__ == '__main__':
    main()