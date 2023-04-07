from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super

# Create your views here.
@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        
        super_types_param = request.query_params.get('type')
        sort_param = request.query_params.get('sort')

        if super_types_param:
            supers = supers.filter(super_type__type=super_types_param)
            serializer = SuperSerializer(supers, many=True)
        else:
            #super_serializer = SuperSerializer(supers, many=True)
            #super_type_serializer = SuperTypesSerializer(super_types, many=True)
            heroes = supers.filter(super_type__type='hero')
            villains = supers.filter(super_type__type='villain')
            Heroserializer = SuperSerializer(heroes, many=True)
            Villainserializer = SuperSerializer(villains, many=True)
            custom_response_dict = {
            'heroes': Heroserializer.data,
            'vilains': Villainserializer.data
            }
            return Response(custom_response_dict)

        if sort_param:
            super = supers.order_by(sort_param)

        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#@api_view(['GET'])
#def supers_and_super_types(request):

   # supers = Super.objects.all()
   # super_types = SuperTypes.objects.all()

    #super_serializer = SuperSerializer(supers, many=True)
    #super_type_serializer = SuperTypesSerializer(super_types, many=True)

    #custom_response_dict = {
        #'supers': super_serializer.data
        #'super_types': super_type_serializer.data
    #}
    #return Response(custom_response_dict)

@api_view(['GET', 'PUT', 'DELETE'])   
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method =='GET':
        serializer = SuperSerializer(super);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)