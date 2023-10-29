
from django.urls import path 
from .views import ProductDeleteView, ProductDetailView, ProductListCreateView, ProductListView, ProductMixinsView, ProductUpdateView, ProductView

urlpatterns = [
    path('product/v1/', ProductView, name='produit'),
    path('product/mixin/create', ProductMixinsView.as_view()),
    path('product/mixin/list', ProductMixinsView.as_view()),
    path('product/mixin/<int:pk>/update', ProductMixinsView.as_view()),
    path('product/mixin/<int:pk>/delete', ProductMixinsView.as_view()),
    path('product/mixin/<int:pk>/detail', ProductMixinsView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),
    path('product/', ProductListCreateView.as_view()),
    path('product/list/', ProductListView.as_view()),
    path('product/<int:pk>/update/', ProductUpdateView.as_view()),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view()),
    
] 
