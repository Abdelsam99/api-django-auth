from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.forms.models import model_to_dict
from rest_framework import authentication, generics,mixins, permissions
from .permissions import IsStaffPermission,IsAuthenticatedOrReadOnly
# from apiApp import serializers
# Create your views here.
@api_view(['GET','POST'])
def ProductView(request):
    query=Product.objects.all().first()
    data=ProductSerializer(query).data
    if request.method=='POST':
        serialiser=ProductSerializer(data=request.data)
        if serialiser.is_valid(raise_exception=True):
            serialiser.save()
            return Response(serialiser.data)
    return Response(data)
    # serialiser=ProductSerializer
    
    """Cette classe est pour le détail d'un produit"""
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    #on donne des permissions, sur la class
    #on verifit si l'utilisateur est connecté
    #permission_classes=[permissions.DjangoModelPermissions]
    #on s'authentifie avec des sessiones
    # authentication_classes=[authentication.SessionAuthentication,authentication.TokenAuthentication]
    """Cette classe est pour la création d'un produit 
    et ensuite pour la recupération des produits
    c'est en fonction de la requête qu'il fonction et elle 
    n'accepte que des get ou post"""
    
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    #ici avant d'enregistrer je récupère le name et le content 
    #si le content est vide je met la valeur de name dans le 
    #content avant de sauvegarder
    # authentication_classes=[authentication.SessionAuthentication]
    # permission_classes=[permissions.IsAdminUser,IsStaffPermission]
    permission_classes=[permissions.IsAuthenticated]
    # def perform_create(self, serializer):
    #     name=serializer.validated_data.get('name')
    #     content=serializer.validated_data.get('content') or None
    #     if content is None:
    #         content = name
    #     serializer.save(content=content + " content")

    """Cette classe est pour la modification d'un produit"""
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    
    """Cette classe est pour la suppression d'un produit"""
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    
    """Cette methode est pour afficher tout les produits """
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    """Cette methode est une surcharge"""
    def get_queryset(self):
        return super().get_queryset()
    
    """Cette classe peut faire tout le crud"""
class ProductMixinsView(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # def perform_create(self, serializer):
    #     name = serializer.validated_data.get('name')
    #     content = serializer.validated_data.get('content') or None
    #     if content is None:
    #         content = name
    #     serializer.save(content=content + " content")

    # def perform_update(self, serializer):
    #     name = serializer.validated_data.get('name')
    #     content = serializer.validated_data.get('content') or None
    #     if content is None:
    #         content = name
    #     serializer.save(content=content + " contentMofier")
        
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs) 
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)   

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)