# Создать view

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from clinics.models import *
from clinics.serializers import *

random = openapi.Parameter(
    'random',
    openapi.IN_QUERY,
    description='This path parameter is used to filter data randomly',
    type=openapi.TYPE_BOOLEAN
)

is_in_home = openapi.Parameter(
    'home',
    openapi.IN_QUERY,
    description='This path parameter is used to filter data that is shown in the home page',
    type=openapi.TYPE_BOOLEAN
)

category_id = openapi.Parameter(
    'category_id',
    openapi.IN_QUERY,
    description='This path parameter is used to filter data by category id',
    type=openapi.TYPE_INTEGER
)


class ActionListAPIView(ListAPIView):
    queryset = Action.objects.filter(expires_in__gte=datetime.date.today()).order_by('-expires_in')
    serializer_class = ActionListSerializer

    @swagger_auto_schema(manual_parameters=[random])
    def get(self, request, *args, **kwargs):
        random = request.GET.get('random', None)
        if random is not None and random == 'true':
            self.queryset = self.queryset.order_by('?')[:13]

        return super().get(request, *args, **kwargs)


class OnlineAppointmentCreateAPIView(CreateAPIView):
    queryset = OnlineAppointment.objects.all()
    serializer_class = OnlineAppointmentSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.filter(published=True).order_by('-created_at')
    serializer_class = NewsListSerializer

    @swagger_auto_schema(manual_parameters=[is_in_home, category_id])
    def get(self, request, *args, **kwargs):
        query_param = request.GET.get('home', None)
        category_id = request.GET.get('category_id', None)
        if query_param is not None and query_param == 'true':
            self.queryset = self.queryset[:3]
        if category_id is not None:
            self.queryset = self.queryset.filter(category_id=category_id)

        return super().get(request, *args, **kwargs)


class SpecialistListAPIView(ListAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistListSerializer

    @swagger_auto_schema(manual_parameters=[is_in_home])
    def get(self, request, *args, **kwargs):
        query_param = request.GET.get('home', None)

        if query_param is not None and query_param == 'true':
            self.queryset = self.queryset[:12]

        return super().get(request, *args, **kwargs)


class ContactChiefDoctorCreateAPIView(CreateAPIView):
    queryset = ContactChiefDoctor.objects.all()
    serializer_class = ContactChiefDoctorSerializer


class FeedbackCreateAPIView(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackCreateSerializer


class FeedbackListAPIView(ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializer


class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer


class LicenseListAPIView(ListAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer


class ContactAPIView(RetrieveAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer

    def get_object(self):
        return self.queryset.first()


class NewsCategoryListAPIView(ListAPIView):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer


class PhotoGalleryCategoryListAPIView(ListAPIView):
    queryset = PhotoGalleryCategory.objects.all()
    serializer_class = PhotoGalleryCategorySerializer


class PhotoGalleryListAPIView(ListAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer

    @swagger_auto_schema(manual_parameters=[category_id])
    def get(self, request, *args, **kwargs):
        category_id = request.GET.get('category_id', None)
        if category_id is not None:
            self.queryset = self.queryset.filter(category_id=category_id)
        return super().get(request, *args, **kwargs)


class StoryCategoryListAPIView(ListAPIView):
    serializer_class = StoryCategoryListSerializer
    queryset = StoryCategory.objects.all()


class StoryCategoriesListAPIView(ListAPIView):
    queryset = StoryCategory.objects.all()
    serializer_class = StoryCategoryDetailSerializer