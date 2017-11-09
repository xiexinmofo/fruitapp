from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import GoodsType,Goods
import random
from django.views.decorators.csrf import csrf_exempt
import json
from decimal import Decimal
def home(request):
    good_type=GoodsType.objects.all()
    type_list=[]
    for item in good_type:
        print(item)
        type_list.append(item)

    return render(request,'demo/home.html',{'type':type_list})

#自定义decimal类型字符的json处理
class DecimalEncoder(json.JSONEncoder):
    def _iterencode(self,o,markers=None):
        if isinstance(o,Decimal):
            return float(o)
        return super(DecimalEncoder,self)._iterencode(o,markers)





@csrf_exempt
def json_response(request):
    goods_list = []
    if request.is_ajax():
        id=request.POST['id']
        goodtype=get_object_or_404(GoodsType,pk=id)
        goods=goodtype.goods.order_by('-type__flag')[:4]
        for good in goods:
            #price = DecimalEncoder(good.price)
            #print(price)
            print(str(good.price))
            good_info={'name':good.title,'price':str(good.price),'img':good.picture.url}
            goods_list.append(good_info)

    return HttpResponse(json.dumps(goods_list),content_type='application/json')




