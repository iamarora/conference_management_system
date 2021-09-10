from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, views, status
from rest_framework.response import Response

from cmsapp.models import Conference, Person, Talk
from cmsapp.serializers import ConferenceSerializer, PersonSerializer, TalkSerializer


class ConferenceViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer


class TalkViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer


class PersonViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class AddRemovePersonView(views.APIView):

    def get_talk_obj(self, talk_id):
        try:
            talk_obj = Talk.objects.get(id=talk_id)
        except Talk.DoesNotExist:
            talk_obj = None
        return talk_obj

    def add_remove_talk_people(self, talk_obj, person, action):
        person_obj, _created = Person.objects.get_or_create(**person)
        if action == 'remove':
            talk_obj.people.remove(person_obj)
        elif action == 'add':
            talk_obj.people.add(person_obj)

    @swagger_auto_schema(operation_description="Add person to a talk", request_body=PersonSerializer)
    def post(self, request, talk_id):
        response = {}
        status_code = status.HTTP_404_NOT_FOUND
        person_serializer = PersonSerializer(data=request.data)
        if person_serializer.is_valid():        
            talk_obj = self.get_talk_obj(talk_id)
            if talk_obj is None:
                response = {"error": "Object not found"}
            else:
                self.add_remove_talk_people(talk_obj, person_serializer.validated_data, action='add')
                status_code = status.HTTP_201_CREATED
        else:
            response = person_serializer.errors
        return Response(response, status=status_code)

    @swagger_auto_schema(operation_description="Remove person from a talk", request_body=PersonSerializer)
    def put(self, request, talk_id):
        response = {}
        status_code = status.HTTP_404_NOT_FOUND
        person_serializer = PersonSerializer(data=request.data)
        if person_serializer.is_valid():        
            talk_obj = self.get_talk_obj(talk_id)
            if talk_obj is None:
                response = {"error": "Object not found"}
            else:
                self.add_remove_talk_people(talk_obj, person_serializer.validated_data, action='remove')
                status_code = status.HTTP_202_ACCEPTED
        else:
            response = person_serializer.errors
        return Response(response, status=status_code)
