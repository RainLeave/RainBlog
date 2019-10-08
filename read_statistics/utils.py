import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum, ReadDetail


def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_or_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        # 总阅读数 +1
        readnum, created = ReadNum.objects,get_or_creaet(content_type=t, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()

        # 当天阅读数 +1
        date = timezone.time.now().date()
        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num += 1
    return key


# 获取过去七天的数据
def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(7, 0, -1):
        date = today -  datetime.timedelta(days=i)
        dates.append(date.strftime("%m%d"))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums


# 获取今日热门
def get_today_hot_data(content_type):
    """
    类型: 传入博客类型
    日期：今天
    :param content_type: 类型是博客
    :return: 今日博客数量
    """
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(content_type=content_type, date=today).order_by('-read_num')
    # 使用切片器取出前7条数据
    return read_details[:7]


# 获取昨天日期
def get_yesterday_hot_data(content_type):
    """
    用于给视图调用

    :param content_type:
    :return:
    """
    today = timezone.now().date()
    # 今天减去1天等于昨天
    yesterday = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(content_type=content_type, date=yesterday).order_by('-read_num')
    return read_details

# 用get_7_days_hot_blogs方法代替了
# def get_7_days_hot_data(content_type):
#     # 获取今天的时间
#     today = timezone.now().date()
#     # 今天的时间减去7天得到七天前的当天的时间
#     date = today - datetime.timedelta(days=7)
#     # \ 用作换行处理
#     # lt:小于 gt:大于 关键字 小于今天，大于等于第前七天的日期
#     # 分组统计博客 避免获取的数据零散，
#     # 对content_type和object_id进行分组构成一个对应的分组对象 得到一个列表 .values('content_type', 'object_id')
#     # 对列表进行注释 annotate 同时进行Sum操作 from django.db.models import Sum
#     # annotate(Sum('reaf_num')) 对read_num字段进行求和和分组
#     # 对结果read_num_sum进行倒序排序
#     # 这个values方法是将查询集变成一个迭代器，迭代器里元素是字典，
#     # 后面指定参数就可以取出每项的键值对，之后进行求和
#     # 类似于sql中的group，再sum，相当于数据库中的分组求和
#
#     read_details = ReadDetail.objects \
#                 .filter(content_type=content_type, date__lt=today, date_gte=date) \
#                 .values('content_type', 'object_id') \
#                 .annotate(read_num_sum = Sum('reaf_num')) \
#                 .order_by('-read_num_sum')
#     return read_details[:7]
#
#
#
#
