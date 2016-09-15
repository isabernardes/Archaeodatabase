from django.conf.urls import url

from .views import (
	#excavation_create,
	excavation_list,
	#befund_create,
	excavation_detail,
	#befund_detail,
	#befund_update,
	#befund_delete,
	#photos_list,

	)

urlpatterns = [
    url(r'^$', excavation_list, name='excavation'),
	#url(r'^create/$', excavation_create, name='create'),
	url(r'^(?P<id>\d+)/$', excavation_detail),
	#url(r'^(?P<slug>[\w-]+)/$', befund_detail, name='befund_detail'),
	#url(r'^(?P<slug>[\w-]+)/edit$', befund_update, name='update'),
	#url(r'^(?P<slug>[\w-]+)/delete/$', befund_delete),
	#url(r'^tag/(?P<tag>\w+)/$', photos_list),


	

    ]