from django.shortcuts import render
from django.utils import timezone
import math
# Create your views here.


def index(request):
    context = {'title': '超市进销存管理系统'}
    if request.user.is_authenticated:
        now = timezone.now()
        passed = now - request.user.date_joined
        if passed.days == 0 and passed.seconds >= 0 and passed.seconds < 60:
            passed = '成功'
        elif passed.days == 0 and passed.seconds >= 60 and passed.seconds < 3600:
            passed = str(math.floor(passed.seconds / 60)) + "分钟" + \
                str(math.floor(math.floor(passed.seconds % 60) / 60))+"秒"
        elif passed.days == 0 and passed.seconds >= 3600 and passed.seconds < 86400:
            passed = str(math.floor(passed.seconds / 3600)) + "小时" + \
                str(math.floor(math.floor(passed.seconds % 3600) / 60)) + "分"
        elif passed.days >= 1 and passed.days < 30:
            passed = str(passed.days) + "天" + \
                str(math.floor(math.floor(passed.seconds % 86400) / 3600)) + "小时"
        elif passed.days >= 30 and passed.days < 365:
            passed = str(math.floor(passed.days / 30)) + "个月" + \
                str(math.floor(passed.days % 30)) + "天"
        elif passed.days >= 365:
            passed = str(math.floor(passed.days / 365)) + "年" + \
                str(math.floor(math.floor(passed.days % 365) / 30))+"个月"
        context['passed'] = passed
    return render(request, 'index.html', context)
