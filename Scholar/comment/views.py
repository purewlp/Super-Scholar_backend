from django.core.cache import cache

from comment.models import Comment
from comment.tasks import *
from comment.utils import get_all_comments_by_work_id
from utils.Redis_utils import *

from utils.Sending_utils import *


@login_checker
def add_comment(request):
    if request.method == 'POST':
        # 获取表单信息
        data_json = json.loads(request.body.decode())
        user_id = request.user_id
        work_id = data_json.get('work_id')
        content = data_json.get('content')

        # 异常处理
        # 评论内容为空
        if len(content) == 0:
            result = {'result': 0, 'message': r"评论内容为空！"}
            return JsonResponse(result)

        # 创建数据
        comment = Comment.objects.create(user_id=user_id, work_id=work_id, content=content)

        # 更新缓存
        cache_set_after_create("comment", "comment", comment.id, comment.to_dic())

        # 延迟更新数据库
        add_comment_of_work(comment.id, work_id)

        result = {'result': 0, 'message': r"添加成功！"}
        return JsonResponse(result)



    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


# 获取当前文章的全部评论
def get_all_comments(request):
    if request.method == 'POST':
        # 获取表单信息
        data_json = json.loads(request.body.decode())
        work_id = data_json.get('work_id')

        all_comments = get_all_comments_by_work_id(work_id)

        result = {'result': 0, 'message': r"查找成功！", 'all_comments': all_comments}
        return JsonResponse(result)



    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)
