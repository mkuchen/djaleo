from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from apps.info.views import HomeView, TwoView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djaleo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^two/$', TwoView.as_view(), name='two'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
