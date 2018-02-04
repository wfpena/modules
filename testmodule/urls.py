from django.conf.urls import url, include
from testapp.modules.testmodule.api import router

app_name = 'testmodule'
urlpatterns = [
    # API
    url(r'^api/', include(router.urls)),
]
