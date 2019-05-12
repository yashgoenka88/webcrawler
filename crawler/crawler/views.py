import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.core.serializers.json import DjangoJSONEncoder
from .crawler import Crawler


class CrawlerView(APIView):

    def get(self, request):
        try:
            level = request.GET.get('level')
            url = request.GET.get('url')

            crawler = Crawler(url, level)
            # links = crawler.crawl(url)
            links = crawler.fetch()

            return HttpResponse(json.dumps(links, cls=DjangoJSONEncoder), content_type='application/json',status=200)
        except:
            error = {
                "msg": "Verify URL"
            }
            return HttpResponse(json.dumps(error, cls=DjangoJSONEncoder), content_type='application/json', status=500)
