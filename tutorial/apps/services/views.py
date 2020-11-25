import json
from django.shortcuts import render
from django.views import View
from .decorators import set_str_upper, set_array
# Create your views here.


class ParserView(View):
    """http://127.0.0.1:8000/parser/data"""

    @staticmethod
    def parse_data(data: dict = ()):
        data = {'people': []}
        data['people'].append({
            'name': 'Scott',
            'website': 'stackabuse.com',
            'from': 'Nebraska'
        })
        file_json = 'data_parse/data'
        with open(file_json + '.json', '+a') as outfile:
            json.dump(data, outfile)
            # _id = load_data[0]['id']
            # data['id'] = _id + 1
            # load_data.append(data)
            # return load_data

    template_name = 'services/parser.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = {
            "id": 0,
            "name": request.POST['name'],
            "age": request.POST['age'],
            "lang": request.POST['lang']
        }
        # new = [
        #     {"id": 2, "name": "eshmat", "age": 24, "lang": "uz"},
        #     {"id": 3, "name": "toshmat", "age": 25, "lang": "ru"}
        # ]
        self.parse_data(data=data)
        return render(request, self.template_name)


class PriceView(View):
    """http://127.0.0.1:8000/service/separator"""
    template_name = "price.html"

    def get(self, request):
        if request.method == 'GET':
            context = {}
            try:
                price = int(request.GET['price'])
                count = len(str(price))
                if count > 3:
                    if count == 4:
                        context['data'] = str(price)[:1] + " " + str(price)[1:]
                    elif count == 5:
                        context['data'] = str(price)[:2] + " " + str(price)[2:]
                    elif count == 6:
                        context['data'] = str(price)[:3] + " " + str(price)[3:]
                    elif count == 7:
                        context['data'] = str(price)[:1] + " " + str(price)[-3:] + " " + str(price)[-3:]
                    elif count == 8:
                        context['data'] = str(price)[:2] + " " + str(price)[-3:] + " " + str(price)[-3:]
                    elif count > 8:
                        context['data'] = str(price)[:3] + " " + str(price)[-3:] + " " + str(price)[-3:]
                else:
                    context['data'] = price
                return render(request, self.template_name, context)
            except KeyError:
                return render(request, self.template_name, {'data': '...'})


class Separator(View):
    """http://127.0.0.1:8000/service/price"""
    template_name = "separator.html"

    def get(self, request):
        @set_str_upper
        def get_str_upper(str_obj):
            return str_obj
        print(get_str_upper('alik'))  # ALIK

        @set_array
        def get_array(str_obj):
            return str_obj
        print(get_array('Hello world'))  # ['Hello', 'world']

        if request.method == 'GET':
            vowels = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
            consonants = "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", \
                         "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"
            context = {}
            try:
                undefined_str = str(request.GET['str'])
                vowel_letters = ""
                consonant_letters = ""
                for v in undefined_str:
                    if v in vowels:
                        vowel_letters += v
                for c in undefined_str:
                    if c in consonants:
                        consonant_letters += c
                context['count_v'] = len(str(vowel_letters))
                context['count_c'] = len(str(consonant_letters))
                context['vowel'] = vowel_letters
                context['consonant'] = consonant_letters
                return render(request, self.template_name, context)
            except KeyError:
                return render(request, self.template_name, {'data': '...'})


