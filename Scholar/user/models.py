from django.db import models

from collection.models import CollectionPackage
from follow.models import Follow


class User(models.Model):
    # 基础信息
    username = models.CharField('用户名', max_length=100, default='')
    password = models.CharField('密码', max_length=32)
    email = models.EmailField()
    introduction = models.TextField('自我介绍', blank=True, max_length=2048,
                                    default='Leave something to help others get to know you better!')
    is_active = models.BooleanField('邮箱是否已经验证', default=False)
    is_super = models.BooleanField('是否为超管', default=False)

    # 头像
    avatar_url = models.CharField('用户头像路径', max_length=128, default='')
    avatar = models.FileField('用户头像', upload_to='', default='')

    # 权限判断
    is_professional = models.IntegerField('是否认证', default=-1)

    # 实体属性
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'scholar_user'

    def to_dic(self):
        collection_package_list = CollectionPackage.objects.filter(user_id=self.id)
        collection_package_id_list = [cp.id for cp in collection_package_list]

        follow_list = Follow.objects.filter(user_id=self.id)
        follow_id_list = [f.author_id for f in follow_list]

        return {
            'user_id': self.id,
            'username': self.username,
            'email': self.email,

            "avatar_url": self.avatar_url,

            'is_active': self.is_active,
            'is_super': self.is_super,
            'is_professional': self.is_professional,

            'created_time': self.created_time,
            'updated_time': self.updated_time,

            'collection_package_id_list': collection_package_id_list,
            'follow_id_list': follow_id_list,
        }
