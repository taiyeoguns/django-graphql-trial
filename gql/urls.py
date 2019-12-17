from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", RedirectView.as_view(url="/graphql"), name="index"),
    path("admin/", admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
