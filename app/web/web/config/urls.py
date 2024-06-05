# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('profiles.urls')),
    path('api/', include('reqs.urls')),
    path('api/', include('payments.urls')),
    path('api/', include('reviews.urls')),
    path('api/', include('media.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('complaints.urls')),
    path('api/', include('otp.urls')),
    path('api/', include('notifications.urls')),
    path('api/', include('support_tickets.urls')),
    path('api/', include('roles.urls')),
    path('api/', include('achievements.urls')),
    path('api/', include('cars.urls')),
    path('api/', include('blog_posts.urls')),
    path('api/', include('cities.urls')),
    path('api/', include('certificates.urls')),
    path('api/', include('services.urls')),
    path('api/', include('transactions.urls')),
    path('api/', include('faqs.urls')),
    path('api/', include('live_location.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
