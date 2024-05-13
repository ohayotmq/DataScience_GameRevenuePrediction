from django.apps import AppConfig
import threading
import globalVar

class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainApp'
    def ready(self):
        # # cao data va luu vao file csv
        # globalVar.scrapedFile = 'newFile.csv'

        # # huan luyen mo hinh
        # globalVar.model = None

        # # repeat after 7 days
        # threading.Timer(3600*24*7, self.ready).start()

        print('hello world')