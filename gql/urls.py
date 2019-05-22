from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from graphene_django.views import GraphQLView

urlpatterns = [
    path("", RedirectView.as_view(url="/graphql"), name="index"),
    path("admin/", admin.site.urls),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
