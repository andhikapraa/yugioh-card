from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("xml/", views.show_xml, name="show_xml"),
    path("json/", views.show_json, name="show_json"),
    path("xml/<int:id>/", views.show_xml_by_id, name="show_xml_by_id"),
    path("json/<int:id>/", views.show_json_by_id, name="show_json_by_id"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("add_amount/<int:id>", views.add_amount, name="add_amount"),
    path("reduce_amount/<int:id>", views.reduce_amount, name="reduce_amount"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("delete_all/", views.delete_all, name="delete_all"),
    path("get-items-json/", views.get_items_json, name="get_items_json"),
    path("create-ajax/", views.create_item_ajax, name="create_item_ajax"),
]