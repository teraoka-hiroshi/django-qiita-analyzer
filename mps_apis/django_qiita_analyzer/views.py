import json
# コマンドラインをスクリプトから実行
# import subprocess
# subprocess.call('./qiita_module_execution.sh')
import urllib.parse
import urllib.request

from django.shortcuts import render, render_to_response
import requests
from django.views import View
from django_qiita_analyzer.models import AccessToken


# credentialsファイルにclient_idとclient_secret用意
from . import credentials


class UpdatesView(View):

    def get(self, request):
        """
        Qiita API
        GET /api/v2/oauth/authorize (client_id,scope)アクセス『許可』へ
        """
        qiita_client_id = credentials.client_id
        scope = "read_qiita"
        qiita_api_url = "https://qiita.com/api/v2/oauth/authorize?"+"client_id="+qiita_client_id+"&scope="+scope
        return render(request, 'django_qiita_analyzer/data_update.html', {
            'qiita_api_url': qiita_api_url
        })


class RedirectView(View):

    def get(self, request):
        """QiitaのOAUTH使ってリダイレクトされた情報取得"""
        if "code" in request.GET:
            # リダイレクトされた情報の中にある"code"を取得
            param_value = request.GET.get("code")
            return self.get_accesstoken(param_value)

    def get_accesstoken(self, code):
        """取得した'code'を使ってアクセストークン取得"""
        data = {
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
            "code": code
        }
        # requestsを使ったPOST
        req = requests.post("https://qiita.com/api/v2/access_tokens",
                            json.dumps(data).encode("utf-8"),
                            headers={"Content-Type": "application/json"})
        print("req.json", req.json())
        # urllib.request.Requestを使ったPOSTのやり方<<jsonの扱いが色々しないといけない>>
        # json_data = json.dumps(data).encode("utf-8")
        # url = "https://qiita.com/api/v2/access_tokens"
        # method = "POST"
        # headers = {"Content-Type": "application/json"}
        #
        #
        # req = urllib.request.Request(url, data=json_data, method=method, headers=headers)
        # print("req", req)
        # with urllib.request.urlopen(req) as response:
        #     response_body = response.read().decode("utf-8")
        #     json_body = json.loads(response_body)
        #
        # if "token" in json_body:
        #     # query_paramが指定されている場合の処理
        #     print("json_body", json_body['token'])
        #     token = json_body['token']
        for key, value in req.json().items():
            print("item", key, value)
            if "token" in key:
                # query_paramが指定されている場合の処理
                print("item", value)
                token = value
                access_token = AccessToken.objects.create(token=token)
                access_token.save()
        return render_to_response('django_qiita_analyzer/redirect.html', {
            'token': token
        })
