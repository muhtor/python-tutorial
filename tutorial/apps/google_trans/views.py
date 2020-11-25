from django.shortcuts import render
from googletrans import Translator
from django.views import View

# Create your views here.


class GoogleTranslateApiView(View):
    def get(self, request):
        template_name = 'google-trans.html'
        try:
            translator = Translator(service_urls=[
                'translate.google.com',
                'translate.google.co.kr',
            ])
            detect = translator.detect(text='word').lang
            print("Detect......", detect, type(detect))
            words = 'apple1_2_3_4cherry__///__avocado__///__watermelon__///__banana__///__help'
            text = translator.translate(text=str(words), dest="uz")
            print("T......", text, type(text))
            try:
                response = text.text
                convert_to = response.replace('__ /// __', '@@')
                convert_to_list = convert_to.split('@@@')
                print("1......", response, type(response))
                print("2......", convert_to, type(convert_to))
                print("3......", convert_to_list, type(convert_to_list))

            except Exception as q:
                print("Q....", q.args)
        except Exception as e:
            print("E....", e.args)
        return render(request, template_name)
