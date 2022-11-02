from django.db import models


class Comment(models.Model):

    user_id = models.IntegerField('对应用户的id', db_index=True, default=0)
    level = models.IntegerField('评论级别', default=0) # 0 -> 顶级评论, 1 -> 回复评论 
    father_id = models.IntegerField('对应父评论的id', default=0)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    work_id = models.CharField('评论文章的id', max_length=50, default="")
    content = models.TextField('评论内容', max_length=1024, default="")

    class Meta:
        db_table = 'scholar_comment'