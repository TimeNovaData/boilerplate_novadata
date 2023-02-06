from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class NovadataModelViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticated,
    ]

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    def get_fk_fields(self):
        model = self.serializer_class().Meta.model
        fields = model._meta.get_fields()
        fk_fields = [
            (field.name, field.remote_field.model)
            for field in fields
            if field.get_internal_type() == "ForeignKey"
        ]

        return fk_fields

    def get_data(self, request):
        data = request.data.copy()
        for fk_field in self.get_fk_fields():
            field_name = fk_field[0]
            try:
                data[field_name] = data[field_name]["id"]
            except KeyError:
                print(f"Não passou {field_name}")

        return data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.get_data(request))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        obj_datas = {}
        for field in self.get_fk_fields():
            field_name = field[0]
            obj_datas[field_name] = request.data.pop(
                field_name,
                None,
            )

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial,
        )
        serializer.is_valid(raise_exception=True)

        for field in self.get_fk_fields():
            field_name = field[0]

            try:
                model = field[1]
                obj_data = obj_datas[field_name]
                if obj_data:
                    fk_instance = model.objects.get(pk=obj_data["id"])
                    setattr(serializer.instance, field_name, fk_instance)
            except model.DoesNotExist:
                print(f"Não passou {field_name}")

        self.perform_update(serializer)
        serializer.instance.save()

        return Response(serializer.data)
