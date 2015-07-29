from django.contrib.auth import login
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from rest_framework.compat import View
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ViewSet
from documents.models import Document, DocumentPermission
from documents.serializers import DocumentSerializer, \
    DocumentUpdateSerializer, DocumentCreateSerializer, \
    DocumentPermissionSetSerializer
from secure_user.backends import EmailAuthBackend
from secure_user.models import User

__author__ = 'smuravko'


class LoginPageView(View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        args = {}
        args.update(csrf(request))

        return render_to_response(self.template_name, args)

    def post(self, request, *args, **kwargs):
        args = {}
        args.update(csrf(request))

        user = EmailAuthBackend().authenticate(
            email=request.POST.get('email'),
            password=request.POST.get('password'))
        if user:
            user.backend = 'secure_user.backends.EmailAuthBackend'
            login(request, user)
            return redirect(reverse('main'))
        else:
            return render(request,
                          self.template_name,
                          {'error': 'The email and password were incorrect.'})


class MainPageView(View):
    template_name = "main.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return render(request, self.template_name, {})
        else:
            return redirect('/')


class DocumentViewSet(ViewSet):
    model = Document
    serializer_class = DocumentSerializer
    create_serializer_class = DocumentCreateSerializer

    def list(self, request, format=None):
        queryset = self.model.objects.filter(
            permissions__user=request.user, permissions__can_read=True)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.create_serializer_class(data=request.data)

        if serializer.is_valid():
            data = serializer.data
            data['author'] = request.user
            Document.objects.create(**data)
            return Response({'status': 'ok'})
        else:
            print('error')
            print(serializer.errors)
            return Response({'status': 'fail'})

    def update(self, request, pk=None):
        document = self.model.objects.filter(permissions__user=request.user,
                                             permissions__can_update=True,
                                             id=pk).first()

        if not document:
            return Response({'status': 'fail'})
        serializer = DocumentUpdateSerializer(
            instance=document, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'ok'})
        else:
            print(serializer.errors)
            return Response({'status': 'fail'})

    @detail_route(methods=['POST'],
                  serializer_class=DocumentPermissionSetSerializer,
                  url_path='set_permissions')
    def set_permissions(self, request, pk=None):
        try:
            user_permited = User.objects.get(id=request.data.get('user'))
        except User.DoesNotExist:
            return Response({'status': 'fail'})

        permit, _ = DocumentPermission.objects.get_or_create(
            document_id=pk, user=user_permited)

        serializer = self.serializer_class(
            permit, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'ok'})
        else:
            print(serializer.errors)
            return Response({'status': 'fail'})

    def destroy(self, request, *args, **kwargs):
        document = self.model.objects.filter(
            permissions__user=request.user, permissions__can_delete=True,
            id=kwargs.get('pk')
        )
        document.delete()
        return Response({'status': 'ok'})
