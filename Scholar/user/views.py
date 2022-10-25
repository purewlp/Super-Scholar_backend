import json

from user.models import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from utils.Login_utils import hash_encode
from utils.Redis_utils import cache_get_by_id

from utils.Sending_utils import *


def test(request):
    return HttpResponse("Hello world!")

# 用户注册
def register( request ):
    """
    :param request: 请求体
    :return:        1 - 成功， 0 - 失败

    请求体包含包含 username，password1，password2，email
    """
    if request.method == 'POST':
        data_json = json.loads(request.body.decode())
        print( data_json)

        username = data_json.get('username', '')
        password1 = data_json.get('password1', '')
        password2 = data_json.get('password2', '')
        email = data_json.get('email', '')

        if len(username) == 0 or len(password1) == 0 or len(password2) == 0 or len(email) == 0:
            result = {'result': 0, 'message': r'用户名, 邮箱, 与密码不允许为空!'}
            return JsonResponse( result )

        if User.objects.filter(username=username, is_active=True).exists():
            result = {
                'result': 0,
                'message': r'用户已存在!'
            }
            return JsonResponse(result)

        if password1 != password2:
            result = {
                'result': 0,
                'message': r'两次密码不一致!'
            }
            return JsonResponse(result)

        user = User.objects.create(
            username=username,
            email=email,
            password=hash_encode(password1),
            is_active=False
        )

        payload = {'user_id': user.id, 'email': email }

        send_result = send_email(payload, email, 'register')
        if not send_result:
            result = {'result': 0, 'message': r'发送失败!请检查邮箱格式'}
            return JsonResponse(result)
        else:
            result = {'result': 1, 'message': r'发送成功!请及时在邮箱中查收.'}
            return JsonResponse(result)


    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


def login( request ):
    """
        :param request: 请求体
        :return:        1 - 成功， 0 - 失败

        请求体包含包含 username, password
    """
    if request.method == 'POST':

        # 获取表单信息
        data_json = json.loads(request.body.decode())
        print( data_json )
        username = data_json.get('username', '')
        password = data_json.get('password', '')

        # 检验错误情况
        if len(username) == 0 or len(password) == 0:
            result = {'result': 0, 'message': r'用户名与密码不允许为空!'}
            return JsonResponse(result)

        if not User.objects.filter(username=username, is_active=True).exists():
            result = {'result': 0, 'message': r'用户不存在!'}
            return JsonResponse(result)

        # 获取用户实体
        user = User.objects.get(username=username, is_active=True)

        if user.password != hash_encode(password):
            result = {'result': 0, 'message': r'用户名或者密码有误!'}
            return JsonResponse(result)

        # 需要加密的信息
        payload = {'user_id': user.id}
        # 签发登录令牌
        token = sign_token(payload, exp=3600 * 24)

        # 获取缓存信息
        user_key, user_dict = cache_get_by_id('user', 'user', user.id)

        result = {'result': 1, 'message': r"登录成功！", 'token': token, 'user': user_dict}
        return JsonResponse(result)

    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)
