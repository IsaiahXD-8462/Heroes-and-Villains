from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET']):
def supers_list(request):

    super_types_param = request.query_params.get('super_types')
    sort_param = request.query_params.get('sort')

    supers = Super.objects.all()

    if super_types_param:
        supers = supers.filter(super_types__name=super_types_param)

    if sort_param:
        super = supers.order_by(sort_param)

    return Response('super_types_param')
    return(sort_param)

@api_view(['GET']):
def supers_and_super_types(request):

    supers = Super.objects.all()
    super_types = SuperTypes.objects.all()

    super_serializer = SuperSerializer(supers, many=True)
    super_type_serializer = SuperTypesSerializer(super_types, many=True)

    custom_response_dict = {
        'supers': super_serializer.data
        'super_types': dealership_serializer.data
    }
    return Response(custom_reponse_dict)