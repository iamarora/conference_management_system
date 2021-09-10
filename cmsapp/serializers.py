from rest_framework import serializers

from cmsapp.models import Conference, Person, Talk


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['id', 'username', 'email_id', 'person_type']


class TalkSerializer(serializers.ModelSerializer):
    people = PersonSerializer(many=True, required=False, read_only=True)

    def get_or_create_people(self, people):
        people_ids = []
        for person in people:
            person_obj, _created = Person.objects.get_or_create(**person)
            people_ids.append(person_obj.pk)
        return people_ids

    def update(self, instance, validated_data):
        """
        In addition to the regular update custom code to handle the person ManytoManyField.
        The list sent in the people parameter to the PUT data will be the list of people to the talk - 
          "people": [{
            "username": "Person1",
            "email_id": "user1@example.com",
            "person_type": 0
            },
            {
                "username": "person2",
                "email_id": "user2@example.com",
                "person_type": 1
            }
        ]
        """
        people = validated_data.pop('people', [])
        instance.people.set(self.get_or_create_people(people))
        return super(TalkSerializer, self).update(instance, validated_data)

    class Meta:
        model = Talk
        fields = ['id', 'conference', 'title', 'description', 'duration', 'date_time', 'people']


class ConferenceSerializer(serializers.ModelSerializer):
    talk = TalkSerializer(many=True, read_only=True)

    class Meta:
        model = Conference
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'talk']
