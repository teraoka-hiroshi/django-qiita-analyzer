import json
# コマンドラインをスクリプトから実行
import subprocess
import urllib.parse
import urllib.request

from django.shortcuts import render
# Create your views here.
from django.views import View
from qiita.models import AccessToken

# credentialsファイルにclient_idとclient_secret用意
from . import credentials


class UpdatesView(View):

    def get(self, request):
        # subprocess.call('./qiita_module_execution.sh')
        # GET /api/v2/oauth/authorize へ client_idとscopeでアクセス『許可』画面へのURL
        client_id = credentials.client_id
        scope = "read_qiita"
        page = "https://qiita.com/api/v2/oauth/authorize?"+"client_id="+client_id+"&scope="+scope
        return render(request, 'qiita/data_update.html', {
            'page': page
        })


class RedirectView(View):

    def get(self, request):
        if "code" in request.GET:
            # query_paramが指定されている場合の処理( codeを取得 )
            param_value = request.GET.get("code")

            data = {
                "client_id": credentials.client_id,
                "client_secret": credentials.client_secret,
                "code": param_value
            }
            json_data = json.dumps(data).encode("utf-8")
            url = "https://qiita.com/api/v2/access_tokens"
            method = "POST"
            headers = {"Content-Type": "application/json"}

        req = urllib.request.Request(url, data=json_data, method=method, headers=headers)
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode("utf-8")
            json_body = json.loads(response_body)


        if "token" in json_body:
            # query_paramが指定されている場合の処理
            print("json_body", json_body['token'])
            token = json_body['token']
            access_token = AccessToken.objects.create(token=token)
            access_token.save()
        # print("param_value", param_value)
        return render(request, 'qiita/redirect.html', {
            'token': token
        })
