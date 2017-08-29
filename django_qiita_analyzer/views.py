import json

import requests
from django.shortcuts import render, render_to_response
from django.views import View
from django_qiita_analyzer.models import AccessToken

# credentialsファイルにclient_idとclient_secret用意
from . import credentials


class UpdatesView(View):

    def get(self, request):
        """
        Qiita API
        GET /api/v2/oauth/authorize (client_id,scope)アクセス『許可』へ
        client_id: credentials.py
        scope: credentials.py
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
        """
        取得した'code'を使ってアクセストークン取得
        requestsライブラリでPOSTしている
        """
        data = {
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
            "code": code
        }
        req = requests.post("https://qiita.com/api/v2/access_tokens",
                            json.dumps(data).encode("utf-8"),
                            headers={"Content-Type": "application/json"})

        for key, value in req.json().items():
            if "token" in key:
                # query_paramが指定されている場合の処理
                token = value
                access_token = AccessToken.objects.create(token=token)
                access_token.save()
        return render_to_response('django_qiita_analyzer/redirect.html', {
            'token': token
        })
