from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from apps.info.views import HomeView, TwoView, CathHomeView, CathAboutView, CathClassesView, CathOneView, CathLocationsView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djaleo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^two/$', TwoView.as_view(), name='two'),
    # CATH URLS BEGIN
    url(r'^cath/$', CathHomeView.as_view(), name="cath-home"),
    url(r'^cath/about/$', CathAboutView.as_view(), name="cath-about"),
    url(r'^cath/class/$', CathClassesView.as_view(), name="cath-class"),
    url(r'^cath/1-on-1/$', CathOneView.as_view(), name="cath-one"),
    url(r'^cath/locations/$', CathLocationsView.as_view(), name="cath-locations"),
    #url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
