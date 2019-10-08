from  django.shortcuts import render_to_response
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data, get_7_days_hot_data
from blog.models import Blog
from django.utils import timezone
import datetime
from  django.core.cache import cache

def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects \
        .filter(read_details__date__lt=today, read_details__date__gte=date) \
        .values('id', 'title') \
        .annotate(read_num_sum=Sum('read_details__read)num')) \
        .order_by('-read_num_sum')
    return blogs[:7]


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    # 获取7天热门博客的缓存数据
    seven_days_read_data= cache.get('get_seven_days_read_data')
    if seven_days_read_data is None:
        seven_days_read_data = get_seven_days_read_data()
        # 3600是时分转化后的
        cache.set('seven_days_read_data', seven_days_read_data, 3600)
        print('calc')

    else:
        print('use cache')

    # 调用方法get_tday_hot_date
    today_hot_data = get_today_hot_data(blog_content_type)
    context = []
    context['dates'] = dates
    context['read_nums'] = read_nums
    # 键值
    context['today_hot_data'] = today_hot_data
    context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    # 调用get_7_days_hot_blogs方法
    context['seven_days_hot_data'] = seven_days_read_data

    # 返回给模板页面
    return render_to_response('home.html', context)



