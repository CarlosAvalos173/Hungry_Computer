from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sform", views.simple_form, name="sform"),
    path("delete_simple_form/<int:id>", views.delete_simple_form_id, name="delete_simple_form"),
    # almacen
    path("almacen", views.almacen_view, name="almacen"),
    path("add_product", views.add_product, name="add_product"),
    path("update_product", views.update_product, name="update_product"),
    path("delete_product/<int:id>", views.delete_product, name="delete_product"),
]
