# import threading
# import time
#
#
# class ThreadWithReturnValue(threading.Thread):
#     def __init__(self, target, args=(), kwargs=None):
#         if kwargs is None:
#             kwargs = {}
#         self.target = target
#         self.args = args
#         self.kwargs = kwargs
#         super().__init__()
#
#     def run(self):
#         self.result = self.target(*self.args, **self.kwargs)
#
#     def join(self, timeout=None):
#         super().join(timeout)
#         return self.result
#
#
# def print_cube(num):
#     # A function that returns the third power of a number given as a parameter
#     time.sleep(5)
#     print(f"Cube: {num * num * num}")
#
#
# def print_square(num):
#     # A function that returns the square of the number given as a parameter
#     time.sleep(5)
#     return num * num
#
#
# if __name__ == "__main__":
#     # creating threads
#     t1 = ThreadWithReturnValue(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))
#
#     # starting threads
#     t1.start()
#     t2.start()
#
#     # waiting until both threads have finished executing before executing further code
#     print(t1.join())
#     t2.join()
#
#     print("Done!")

import re

my_config_data = {'init-param': {'cachePackageTagsRefresh': 60,
  'cachePackageTagsStore': 200,
  'cachePackageTagsTrack': 200,
  'cachePagesDirtyRead': 10,
  'cachePagesRefresh': 10,
  'cachePagesStore': 100,
  'cachePagesTrack': 200,
  'cacheTemplatesRefresh': 15,
  'cacheTemplatesStore': 50,
  'cacheTemplatesTrack': 100,
  'configGlossary:adminEmail': 'ksm@pobox.com',
  'configGlossary:installationAt': 'Philadelphia, PA',
  'configGlossary:poweredBy': 'Cofax',
  'configGlossary:poweredByIcon': '/images/cofax.gif',
  'configGlossary:staticPath': '/content/static',
  'dataStoreClass': 'org.cofax.SqlDataStore',
  'dataStoreConnUsageLimit': 100,
  'dataStoreDriver': 'com.microsoft.jdbc.sqlserver.SQLServerDriver',
  'dataStoreInitConns': 10,
  'dataStoreLogFile': '/usr/local/tomcat/logs/datastore.log',
  'dataStoreLogLevel': 'debug',
  'dataStoreMaxConns': 100,
  'dataStoreName': 'cofax',
  'dataStorePassword': 'dataStoreTestQuery',
  'dataStoreTestQuery': "SET NOCOUNT ON;select test='test';",
  'dataStoreUrl': 'jdbc:microsoft:sqlserver://LOCALHOST:1433;DatabaseName=goon',
  'dataStoreUser': 'sa',
  'defaultFileTemplate': 'articleTemplate.htm',
  'defaultListTemplate': 'listTemplate.htm',
  'jspFileTemplate': 'articleTemplate.jsp',
  'jspListTemplate': 'listTemplate.jsp',
  'maxUrlLength': 500,
  'redirectionClass': 'org.cofax.SqlRedirection',
  'searchEngineFileTemplate': 'forSearchEngines.htm',
  'searchEngineListTemplate': 'forSearchEnginesList.htm',
  'searchEngineRobotsDb': 'WEB-INF/robots.db',
  'templateLoaderClass': 'org.cofax.FilesTemplateLoader',
  'templateOverridePath': '',
  'templatePath': 'templates',
  'templateProcessorClass': 'org.cofax.WysiwygTemplate',
  'useDataStore': True,
  'useJSP': False},
 'servlet-class': 'org.cofax.cds.CDSServlet',
 'servlet-name': 'cofaxCDS'}

def calc_cache():
    result = 0
    pattern = "^cache."
    my_key = 'init-param'
    cache_data = my_config_data[my_key]
    for key in cache_data:
      match = re.match(pattern, key)
      if match:
        print(key)
        value = cache_data[key]
        result += value


    return result

result = calc_cache()
print(result)

def check_db_url():
    cache_data = my_config_data['init-param']
    url = cache_data['dataStoreUrl']
    pattern = "sqlserver"
    rez_match = re.findall(pattern, url)
    if rez_match:
        return True
    return False

print(check_db_url())
import threading
class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result


t1 = ThreadWithReturnValue(target=calc_cache)
t2 = ThreadWithReturnValue(target=check_db_url)

t1.start()
t2.start()

rv = t1.join()
rv2 = t2.join()

print(rv, rv2)
