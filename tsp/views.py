from django.views import generic
from django.http import HttpResponse
# application/write_data.pyをインポートする
from .application import write_data


class TitleView(generic.TemplateView):
    template_name = 'tsp/title.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_str'] = "TSPのタイトル"
        return context
    

def call_write_data(req):
       if req.method == 'GET':
        # write_data.pyのwrite_csv()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        write_data.write_csv(req.GET.get("input_data"))
        return HttpResponse()



from urllib import request
from django.shortcuts import render
from numpy import record
from django.views import generic
import json
from django.shortcuts import render
import json

#####################edc
import random
import math
import copy

NUM_CITY = 10 # 都市の総数
NUM_GENE = 200 # 遺伝子の総数

Num_select = int(NUM_GENE/2) #選択する遺伝子の数
Num_kousa = int(NUM_GENE/4) #交叉する遺伝子の数
P_mut = 0.05 #突然変異確率
G_fin = 100 #世代数
G_disp_GA = 10 #出力制御
Gene = [[0 for j in range(NUM_CITY)] for i in range(NUM_GENE)]
City = [[0 for j in range(2)] for i in range(NUM_CITY)]
Kyori_city = [[0 for j in range(NUM_CITY)] for i in range(NUM_CITY)]


#結果用変数
recordlist = []
record = 0.0
genelist = [[0 for j in range(NUM_CITY)] for i in range(math.ceil(G_fin/G_disp_GA))]
###################edc

# Create your views here.

class CreateCityView(generic.TemplateView):
    template_name = 'tsp/make_city.html'
    global NUM_CITY, NUM_GENE, Num_select, Num_kousa, P_mut, G_fin, G_disp_GA, Gene, City, Kyori_city
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


def create_city(request):
    global NUM_CITY, NUM_GENE, Num_select, Num_kousa, P_mut, G_fin, G_disp_GA, Gene, City, Kyori_city, recordlist, record, genelist

    get_num_city = request.GET.get('num_city')
    NUM_CITY = int(get_num_city)
    
    City = [[0 for j in range(2)] for i in range(NUM_CITY)]
    Kyori_city = [[0 for j in range(NUM_CITY)] for i in range(NUM_CITY)]

    mk_city()
    
    context = {}
    context['City_json'] = json.dumps(City)
    context['get_num_city'] = get_num_city

    return render(request, "tsp/disp_route.html", context)



def search(request):
    global NUM_CITY, NUM_GENE, Num_select, Num_kousa, P_mut, G_fin, G_disp_GA, Gene, City, Kyori_city, recordlist, record, genelist

    get_num_gene = request.GET.get('num_gene')
    get_g_fin = request.GET.get('g_fin')
    get_p_select = request.GET.get('p_select')
    get_p_kousa = request.GET.get('p_kousa')
    get_p_mut = request.GET.get('p_mut')

    NUM_GENE = int(get_num_gene)
    G_fin = int(get_g_fin)
    p_select = float(get_p_select)
    p_kousa = float(get_p_kousa)
    P_mut = float(get_p_mut)

    G_disp_GA = 10
    wk1 = math.ceil(G_fin/G_disp_GA)
    genelist = [[0 for j in range(NUM_CITY)] for i in range(wk1)]
    recordlist = [0 for j in range(wk1)]
    Gene =[[0 for j in range(NUM_CITY)] for i in range(NUM_GENE)]
    

    main_GA(p_select, p_kousa, P_mut)

    context = {}
    context['City_json'] = json.dumps(City)
    context['genelist_json'] = json.dumps(genelist)
    context['recordlist_json'] = json.dumps(recordlist)
    context['record_json'] = json.dumps(record)
    context['Gene_json'] = json.dumps(Gene[0])

    context['get_num_gene'] = get_num_gene
    context['get_num_city'] = NUM_CITY
    context['get_g_fin'] = get_g_fin
    context['get_p_select'] = get_p_select
    context['get_p_kousa'] = get_p_kousa
    context['get_p_mut'] = get_p_mut

    return render(request, "tsp/disp_route.html", context)




# def edc_main():
#     mk_city()
#     main_GA()

def mk_city():
    global City, Kyori_city
    for i in range(0, NUM_CITY):
        City[i][0] = random.random()
        City[i][1] = random.random()
    
    for i in range(0, NUM_CITY):
        for j in range(0, NUM_CITY):
            if(i != j):
                wk1 = City[i][0] - City[j][0]
                wk2 = City[i][1] - City[j][1]
                Kyori_city[i][j] = math.sqrt(wk1 * wk1 + wk2 * wk2)

def main_GA(select, kousa, mutate):
    global recordlist, record, genelist
    init_gene()

    n = 0
    for g in range(0, G_fin):
        sort_gene()

        if(g%G_disp_GA == 0):
            recordlist[n] = round(kyori_gene(0), 3)
            genelist[n] = copy.copy(Gene[0])
            n+=1

        select_gene_zyoui(select)
        kousa_gene_zyoui(kousa)
        mutate_gene(mutate)
    sort_gene()
    record = kyori_gene(0) #一番早い

def init_gene(): #Geneの並び順の初期化
    global Gene
    for i in range(0, NUM_GENE):
        Gene[i] = rand_ints_nodup(0, NUM_CITY-1, NUM_CITY)

def rand_ints_nodup(a, b, k): #a~b,要素数kの重複無し乱数リスト
    ns = []
    while len(ns) < k:
        n = random.randint(a, b)
        if not n in ns:
            ns.append(n)
    return ns

def sort_gene():
    global Gene
    kyori = []
    temp = []
    for i in range(0, NUM_GENE):
        kyori.append(kyori_gene(i)) 
    for i in range(0, NUM_GENE - 1):
        for j in range(i+1, NUM_GENE):
            if(kyori[i] > kyori[j]):
                temp = copy.copy(Gene[i])
                Gene[i] = copy.copy(Gene[j])
                Gene[j] = copy.copy(temp)

                kyori[i], kyori[j] = kyori[j], kyori[i]
    
def kyori_gene(i):
    global Gene, Kyori_city
    sum = 0
    n1 = 0
    n2 = 0
    for j in range(0, NUM_CITY):
        n1 = Gene[i][j]
        if (j != NUM_CITY - 1):
            n2 = Gene[i][j+1]
        else:
            n2 = Gene[i][0]
        sum += Kyori_city[n1][n2]
    return sum

def select_gene_zyoui(n): # 上位(n * 100)%を選択
    global Gene, Num_select
    Num_select = int(NUM_GENE * n)
    wk1 = math.ceil(NUM_GENE / n)
    for i in range(1, wk1):
        for j in range(0, Num_select):
            wk2 = Num_select*i + j
            if(wk2 == NUM_GENE - 1):
                return
            Gene[wk2] = copy.copy(Gene[j])


def kousa_gene_zyoui(n): # 上位(n*100)%を交叉
    global Num_kousa
    Num_kousa = int(NUM_GENE * n)
    for i in range(0, Num_kousa):
        cross_cycle(i, i+1)
        i += 1

def cross_cycle(i, j):
    global Gene
    mask = 0
    start = Gene[i][mask]
    wk1 = mask  
    while(start != Gene[j][wk1]):
        for l in range(0, NUM_CITY):
            if(Gene[j][wk1] == Gene[i][l]):
                Gene[i][wk1],Gene[j][wk1] = Gene[j][wk1],Gene[i][wk1]
                wk1 = l
                break
    Gene[i][wk1],Gene[j][wk1] = Gene[j][wk1],Gene[i][wk1]

def mutate_gene(p): # pの確率で変異
    global Gene, P_mut
    P_mut = p
    for i in range(0, NUM_GENE):
        if(p_select(P_mut)):
            randam_no = random.randint(0, NUM_CITY-1)
            randam_ge = random.randint(0, NUM_CITY-1)
            for j in range(0, NUM_CITY):
                if(Gene[i][j] == randam_ge):
                    Gene[i][randam_no], Gene[i][j] = Gene[i][j], Gene[i][randam_no]
                    break

def p_select(epsilon):
    if(epsilon > random.random()):
        return True
    else:
        return False