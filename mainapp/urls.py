from django.urls import path
from .views import CategoryCreateView, CategoryDetailView, ProductCreateView, ProductDetailView, CategoryListView, ProductListView, OrderListView, OrderCreateView

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/detail/', CategoryDetailView.as_view(), name='category-detail'),

    path('products/list/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/detail/', ProductDetailView.as_view(), name='product-detail'),

    path('orders/<int:user_id>/list/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:product_id>/create/', OrderCreateView.as_view(), name='order-create'),

    # path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

]
