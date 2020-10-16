from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from social_center_app.models import *
from social_center_app.serializers import *
from rest_framework.generics import CreateAPIView, ListAPIView
from django.contrib.auth import get_user_model
from collections import Counter
from social_center_app.models import TestBoyko

User = get_user_model()


class UserView(APIView):
    """Иинформация по текущему пользователю (специалисту)"""

    def get(self, request):
        """
        Получение записи

        :param request: Запрос
        :return: Информация о пользователе
        """
        user = User.objects.filter(id=self.request.user.id)
        serializer = UserSerializers(user, many=True)
        return Response(serializer.data)

    def put(self, request):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :return: Статус Created
        """
        user = get_object_or_404(User.objects.all(), pk=self.request.user.id)
        serializer = UserSerializers(instance=user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)


class ClientView(APIView):
    """Информация о клиентах для главной страницы"""

    def get(self, request):
        """
        Получение записи

        :param request: Запрос
        :return: Информация о клиентах
        """
        clients = Client.objects.all()
        serializer = ClientListForMainWindow(clients, many=True)
        return Response(serializer.data)


class ClientInformationView(APIView):
    """Вся информация о клиенте"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id клиента
        :param pk: id клиента
        :return: Вся информация о клиенте
        """
        if pk is None:
            client_id = request.GET.get("client")
        else:
            client_id = pk
        client = Client.objects.filter(pk=client_id)
        if client.exists():
            if pk is None:
                serializer = ClientSerializers(client, many=True)
            else:
                serializer = ClientCRUDSerializers(client, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: id созданного клиента, в случае ошибки создания Bad Request
        """
        client = ClientCRUDSerializers(data=request.data)
        if client.is_valid():
            client.save()
            return Response({'id': client.data.get('id')})
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id клиента
        :return: Статус Created
        """
        client = get_object_or_404(Client.objects.all(), pk=pk)
        serializer = ClientCRUDSerializers(instance=client, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление клиента

        :param request: Запрос
        :param pk: id клиента
        :return: Статус Created
        """
        client = get_object_or_404(Client.objects.all(), pk=pk)
        client.delete()
        return Response(status=201)


class ASocialBehaviorView(APIView):
    """Информация о противоправных действиях, правонарушениях, употреблении наркотиков, алкоголя"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id клиента
        :param pk: id клиента
        :return: Информации о противоправных действиях, в случае отсутствия записи No Content
        """
        if pk is None:
            client = request.GET.get("client")
        else:
            client = pk
        social_behavior = ASocialBehavior.objects.filter(client=client)
        if social_behavior.exists():
            if pk is None:
                serializer = ASocialBehaviorSerializers(social_behavior, many=True)
            else:
                serializer = ASocialBehaviorCRUDSerializers(social_behavior, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        social_behavior = ASocialBehaviorCRUDSerializers(data=request.data)
        if social_behavior.is_valid():
            client = get_object_or_404(Client, id=self.request.data.get('client'))
            social_behavior.save(client=client)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        social_behavior = get_object_or_404(ASocialBehavior.objects.all(), pk=pk)
        serializer = ASocialBehaviorCRUDSerializers(instance=social_behavior, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        social_behavior = get_object_or_404(ASocialBehavior.objects.all(), pk=pk)
        social_behavior.delete()
        return Response(status=201)


class ChronicDiseaseView(APIView):
    """Информация о наличии хронического заболевания"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id клиента
        :param pk: id клиента
        :return: Информация о наличии хронического заболевания, в случае отсутствия записи No Content
        """
        if pk is None:
            client = request.GET.get("client")
        else:
            client = pk
        chronic_disease = ChronicDisease.objects.filter(client=client)
        if chronic_disease.exists():
            if pk is None:
                serializer = ChronicDiseaseSerializers(chronic_disease, many=True)
            else:
                serializer = ChronicDiseaseCRUDSerializers(chronic_disease, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        chronic_disease = ChronicDiseaseCRUDSerializers(data=request.data)
        if chronic_disease.is_valid():
            client = get_object_or_404(Client, id=self.request.data.get('client'))
            chronic_disease.save(client=client)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        chronic_disease = get_object_or_404(ChronicDisease.objects.all(), pk=pk)
        serializer = ChronicDiseaseCRUDSerializers(instance=chronic_disease, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Стутус Created
        """
        chronic_disease = get_object_or_404(ChronicDisease.objects.all(), pk=pk)
        chronic_disease.delete()
        return Response(status=201)


class ChildListView(APIView):
    """Список детей клиента"""

    def get(self, request):
        """
        Получение записи

        :param request: Запрос с id клиента
        :return: Список детей клиента
        """
        client = request.GET.get("client")
        child_list = Child.objects.filter(client=client)
        serializer = ChildListSerializers(child_list, many=True)
        return Response(serializer.data)


class ChildView(APIView):
    """Ребенок"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id ребенка
        :param pk: id ребенка
        :return: Информацию о ребенке, в случае отсутствия записи No Content
        """
        if pk is None:
            child_id = request.GET.get("child")
        else:
            child_id = pk
        child = Child.objects.filter(pk=child_id)
        if child.exists():
            if pk is None:
                serializer = ChildSerializers(child, many=True)
            else:
                serializer = ChildCRUDSerializers(child, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        child = ChildCRUDSerializers(data=request.data)
        if child.is_valid():
            client = get_object_or_404(Client, id=self.request.data.get('client'))
            child.save(client=client)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        child = get_object_or_404(Child.objects.all(), pk=pk)
        serializer = ChildCRUDSerializers(instance=child, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request:
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        child = get_object_or_404(Child.objects.all(), pk=pk)
        child.delete()
        return Response(status=201)


class FamilyMembersInformationView(APIView):
    """Сведения о членах семьи"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id клиента
        :param pk: id клиента
        :return: Сведения о членах семьи, в случае отсутствия записи No Content
        """
        if pk is None:
            client = request.GET.get("client")
        else:
            client = pk
        family = FamilyMembersInformation.objects.filter(client=client)
        if family.exists():
            if pk is None:
                serializer = FamilyMembersInformationSerializers(family, many=True)
            else:
                serializer = FamilyMembersInformationCRUDSerializers(family, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        family = FamilyMembersInformationCRUDSerializers(data=request.data)
        if family.is_valid():
            client = get_object_or_404(Client, id=self.request.data.get('client'))
            family.save(client=client)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        family = get_object_or_404(FamilyMembersInformation.objects.all(), pk=pk)
        serializer = FamilyMembersInformationCRUDSerializers(instance=family, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        family = get_object_or_404(FamilyMembersInformation.objects.all(), pk=pk)
        family.delete()
        return Response(status=201)


class HusbandListView(APIView):
    """Список мужей/партнеров клиента"""

    def get(self, request):
        """
        Получение записи

        :param request: Запрос с id Сведений о членах семьи
        :return: Список мужей/партнеров клиента
        """
        husband = request.GET.get("husband")
        husband_list = HusbandInformation.objects.filter(husband=husband)
        serializer = HusbandListSerializers(husband_list, many=True)
        return Response(serializer.data)


class HusbandInformationView(APIView):
    """Информация о муже/партнёре"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id Сведений о членах семьи
        :param pk: id Сведений о членах семьи
        :return: Информация о муже/партнёре, в случае отсутствия записи No Content
        """
        if pk is None:
            husband = request.GET.get("husband")
        else:
            husband = pk
        husband_information = HusbandInformation.objects.filter(husband=husband)
        if husband_information.exists():
            if pk is None:
                serializer = HusbandInformationSerializers(husband_information, many=True)
            else:
                serializer = HusbandInformationCRUDSerializers(husband_information, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        husband_information = HusbandInformationCRUDSerializers(data=request.data)
        if husband_information.is_valid():
            husband = get_object_or_404(FamilyMembersInformation, id=self.request.data.get('husband'))
            husband_information.save(husband=husband)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        husband_information = get_object_or_404(HusbandInformation.objects.all(), pk=pk)
        serializer = HusbandInformationCRUDSerializers(instance=husband_information, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        husband_information = get_object_or_404(HusbandInformation.objects.all(), pk=pk)
        husband_information.delete()
        return Response(status=201)


class SocialLivingConditionView(APIView):
    """Социально бытовые условия"""

    def get(self, request, pk=None):
        """
        Просмотр записи

        :param request: Запрос с id клиента
        :param pk: id клиента
        :return: Социально бытовые условия, в случае отсутствия записи No Content
        """
        if pk is None:
            client = request.GET.get("client")
        else:
            client = pk
        living_condition = SocialLivingCondition.objects.filter(client=client)
        if living_condition.exists():
            if pk is None:
                serializer = SocialLivingConditionSerializers(living_condition, many=True)
            else:
                serializer = SocialLivingConditionCRUDSerializers(living_condition, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        living_condition = SocialLivingConditionCRUDSerializers(data=request.data)
        if living_condition.is_valid():
            client = get_object_or_404(Client, id=self.request.data.get('client'))
            living_condition.save(client=client)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        living_condition = get_object_or_404(SocialLivingCondition.objects.all(), pk=pk)
        serializer = SocialLivingConditionCRUDSerializers(instance=living_condition, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        living_condition = get_object_or_404(SocialLivingCondition.objects.all(), pk=pk)
        living_condition.delete()
        return Response(status=201)


class SocialEconomicConditionView(APIView):
    """Социально экономические условия проживания"""

    def get(self, request, pk=None):
        """
        Получение данных

        :param request: Запрос с id клиента
        :param pk: id клиента
        :return: Социально экономические условия проживания, в случае отсутствия записи No Content
        """
        if pk is None:
            client = request.GET.get("client")
        else:
            client = pk
        economic_condition = SocialEconomicCondition.objects.filter(client=client)
        if economic_condition.exists():
            if pk is None:
                serializer = SocialEconomicConditionSerializers(economic_condition, many=True)
            else:
                serializer = SocialEconomicConditionCRUDSerializers(economic_condition, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        economic_condition = SocialEconomicConditionCRUDSerializers(data=request.data)
        if economic_condition.is_valid():
            client = get_object_or_404(Client, id=self.request.data.get('client'))
            economic_condition.save(client=client)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        economic_condition = get_object_or_404(SocialEconomicCondition.objects.all(), pk=pk)
        serializer = SocialEconomicConditionCRUDSerializers(instance=economic_condition, data=request.data,
                                                            partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        economic_condition = get_object_or_404(SocialEconomicCondition.objects.all(), pk=pk)
        economic_condition.delete()
        return Response(status=201)


class SourceIncomeView(APIView):
    """Источники дохода"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id Социально экономических условий проживания
        :param pk: id Социально экономических условий проживания
        :return: Источники дохода, в случае отсутствия записи No Content
        """
        if pk is None:
            economic_condition = request.GET.get("economic_condition")
        else:
            economic_condition = pk
        source_income = SourceIncome.objects.filter(economic_condition=economic_condition)
        if source_income.exists():
            if pk is None:
                serializer = SourceIncomeSerializers(source_income, many=True)
            else:
                serializer = SourceIncomeCRUDSerializers(source_income, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        source_income = SourceIncomeCRUDSerializers(data=request.data)
        if source_income.is_valid():
            economic_condition = get_object_or_404(SocialEconomicCondition,
                                                   id=self.request.data.get('economic_condition'))
            source_income.save(economic_condition=economic_condition)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        source_income = get_object_or_404(SourceIncome.objects.all(), pk=pk)
        serializer = SourceIncomeCRUDSerializers(instance=source_income, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        source_income = get_object_or_404(SourceIncome.objects.all(), pk=pk)
        source_income.delete()
        return Response(status=201)


class SocialPaymentView(APIView):
    """Социальные выплаты"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id Социально экономических условий проживания
        :param pk: id Социально экономических условий проживания
        :return: Социальные выплаты, в случае отсутствия записи No Content
        """
        if pk is None:
            economic_condition = request.GET.get("economic_condition")
        else:
            economic_condition = pk
        social_payment = SocialPayment.objects.filter(economic_condition=economic_condition)
        if social_payment.exists():
            if pk is None:
                serializer = SocialPaymentSerializers(social_payment, many=True)
            else:
                serializer = SocialPaymentCRUDSerializers(social_payment, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        social_payment = SocialPaymentCRUDSerializers(data=request.data)
        if social_payment.is_valid():
            economic_condition = get_object_or_404(SocialEconomicCondition,
                                                   id=self.request.data.get('economic_condition'))
            social_payment.save(economic_condition=economic_condition)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        social_payment = get_object_or_404(SocialPayment.objects.all(), pk=pk)
        serializer = SocialPaymentCRUDSerializers(instance=social_payment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        social_payment = get_object_or_404(SocialPayment.objects.all(), pk=pk)
        social_payment.delete()
        return Response(status=201)


class ChildAllowanceAndCompensationView(APIView):
    """Детские пособия и компенсационные выплаты"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id Социально экономических условий проживания
        :param pk: id Социально экономических условий проживания
        :return: Детские пособия и компенсационные выплаты, в случае отсутствия записи No Content
        """
        if pk is None:
            economic_condition = request.GET.get("economic_condition")
        else:
            economic_condition = pk
        child_allowance = ChildAllowanceAndCompensation.objects.filter(economic_condition=economic_condition)
        if child_allowance.exists():
            if pk is None:
                serializer = ChildAllowanceAndCompensationSerializers(child_allowance, many=True)
            else:
                serializer = ChildAllowanceAndCompensationCRUDSerializers(child_allowance, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        child_allowance = ChildAllowanceAndCompensationCRUDSerializers(data=request.data)
        if child_allowance.is_valid():
            economic_condition = get_object_or_404(SocialEconomicCondition,
                                                   id=self.request.data.get('economic_condition'))
            child_allowance.save(economic_condition=economic_condition)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        child_allowance = get_object_or_404(ChildAllowanceAndCompensation.objects.all(), pk=pk)
        serializer = ChildAllowanceAndCompensationCRUDSerializers(instance=child_allowance, data=request.data,
                                                                  partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        child_allowance = get_object_or_404(ChildAllowanceAndCompensation.objects.all(), pk=pk)
        child_allowance.delete()
        return Response(status=201)


class FacilitiesView(APIView):
    """Льготы и меры социальной поддержки,предусмотренные для определенных категорий"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id Социально экономических условий проживания
        :param pk: id Социально экономических условий проживания
        :return: Льготы и меры социальной поддержки, в случае отсутствия записи No Content
        """
        if pk is None:
            economic_condition = request.GET.get("economic_condition")
        else:
            economic_condition = pk
        facilities = Facilities.objects.filter(economic_condition=economic_condition)
        if facilities.exists():
            if pk is None:
                serializer = FacilitiesSerializers(facilities, many=True)
            else:
                serializer = FacilitiesCRUDSerializers(facilities, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        facilities = FacilitiesCRUDSerializers(data=request.data)
        if facilities.is_valid():
            economic_condition = get_object_or_404(SocialEconomicCondition,
                                                   id=self.request.data.get('economic_condition'))
            facilities.save(economic_condition=economic_condition)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        facilities = get_object_or_404(Facilities.objects.all(), pk=pk)
        serializer = FacilitiesCRUDSerializers(instance=facilities, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        facilities = get_object_or_404(Facilities.objects.all(), pk=pk)
        facilities.delete()
        return Response(status=201)


class ExpertOpinionView(APIView):
    """Заключение специалиста"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id клиента
        :param pk: id клиента
        :return: Заключение специалиста, в случае отсутствия записи No Content
        """
        if pk is None:
            client = request.GET.get("client")
        else:
            client = pk
        expert_opinion = ExpertOpinion.objects.filter(client=client)
        if expert_opinion.exists():
            if pk is None:
                serializer = ExpertOpinionSerializers(expert_opinion, many=True)
            else:
                serializer = ExpertOpinionCRUDSerializers(expert_opinion, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        expert_opinion = ExpertOpinionCRUDSerializers(data=request.data)
        if expert_opinion.is_valid():
            specialist = get_object_or_404(User, id=request.user.id)
            client = get_object_or_404(Client, id=self.request.data.get('client'))
            expert_opinion.save(client=client, specialist=specialist)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        expert_opinion = get_object_or_404(ExpertOpinion.objects.all(), pk=pk)
        serializer = ExpertOpinionCRUDSerializers(instance=expert_opinion, data=request.data,
                                                  partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        expert_opinion = get_object_or_404(ExpertOpinion.objects.all(), pk=pk)
        expert_opinion.delete()
        return Response(status=201)


class TestBoykoListView(APIView):
    """Список тестов Бойко"""

    def get(self, request):
        """
        Получение списка

        :param request: Запрос с id клиента
        :return: Список
        """
        client = request.GET.get("client")
        tests = TestBoyko.objects.filter(client=client)
        serializer = TestBoykoListSerializers(tests, many=True)
        return Response(serializer.data)


class TestBoykoView(APIView):
    """Тест Бойко"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id Теста Бойко
        :param pk: id Теста Бойко
        :return: Тест Бойко, в случае отсутствия записи No Content
        """
        if pk is None:
            test = request.GET.get("test")
        else:
            test = pk
        boyko = TestBoyko.objects.filter(pk=test)
        if boyko.exists():
            if pk is None:
                serializer = TestBoykoSerializers(boyko, many=True)
            else:
                serializer = TestBoykoCRUDSerializers(boyko, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        boyko = TestBoykoCRUDSerializers(data=request.data)
        if boyko.is_valid():
            client = get_object_or_404(Client, id=self.request.data.get('client'))
            boyko.save(client=client)
            return Response(boyko.data, status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        boyko = get_object_or_404(TestBoyko.objects.all(), pk=pk)
        serializer = TestBoykoCRUDSerializers(instance=boyko, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        boyko = get_object_or_404(TestBoyko.objects.all(), pk=pk)
        boyko.delete()
        return Response(status=201)


class GraphicBoykoView(APIView):
    """Получение значений двух интерпретаций тестов Бойко (первичная и вторичная диагностика) для графика"""

    def get(self, request):
        """
        Получение значений

        :param request:  Запрос с id интерпретаций тестов Бойко
        :return: Значения по двум интерпретациям
        """
        client = request.GET.get("client")
        tests = TestBoyko.objects.filter(client=client)
        interpretation_1 = InterpretationBoyko.objects.filter(test=tests.values('id').first().get('id'))
        interpretation_2 = InterpretationBoyko.objects.filter(test=tests.values('id').last().get('id'))
        serializer = TestBoykoCRUDSerializers(tests, many=True)
        labels = {}
        for field in InterpretationBoyko._meta.get_fields():
            if not field.is_relation:
                if field.name != 'id':
                    labels[field.name] = field.verbose_name
        array = [{'date': interpretation_1.values('date').first().get('date'),
                  'attempt': tests.values('attempt').first().get('attempt')},
                 {'date': interpretation_2.values('date').first().get('date'),
                  'attempt': tests.values('attempt').last().get('attempt')}]
        return Response({'data': serializer.data, 'labels': labels, 'date': array})


class InterpretationBoykoView(APIView):
    """Интерпретация теста Бойко"""

    def get(self, request):
        """
        Получение записи

        :param request: Запрос с id Теста Бойко
        :return: Интерпретация теста Бойко, в случае отсутствия записи No Content
        """
        test = request.GET.get("test")
        result = InterpretationBoyko.objects.filter(test=test)
        if result.exists():
            serializer = InterpretationBoykoSerializers(result, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        result = InterpretationBoykoCRUDSerializers(data=request.data)
        if result.is_valid():
            test = get_object_or_404(TestBoyko, id=self.request.data.get('test'))
            result.save(test=test)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :return: Статус Created
        """
        result = get_object_or_404(InterpretationBoyko.objects.all(), test=self.request.data.get('test'))
        serializer = InterpretationBoykoCRUDSerializers(instance=result, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    # def delete(self, request, pk):
    #     result = get_object_or_404(InterpretationBoyko.objects.all(), pk=pk)
    #     result.delete()
    #     return Response(status=201)


class TestGAGEListView(APIView):
    """Список тестов GAGE"""

    def get(self, request):
        """
        Получение списка

        :param request: Запрос с id клиента
        :return: Список
        """
        client = request.GET.get("client")
        tests = TestGAGE.objects.filter(client=client)
        serializer = TestGAGEListSerializers(tests, many=True)
        return Response(serializer.data)


class TestGAGEView(APIView):
    """Тест GAGE"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id Теста GAGE
        :param pk: id Теста GAGE
        :return: Тест GAGE, в случае отсутствия записи No Content
        """
        if pk is None:
            test = request.GET.get("test")
        else:
            test = pk
        gage = TestGAGE.objects.filter(pk=test)
        if gage.exists():
            if pk is None:
                serializer = TestGAGESerializers(gage, many=True)
            else:
                serializer = TestGAGECRUDSerializers(gage, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        gage = TestGAGECRUDSerializers(data=request.data)
        if gage.is_valid():
            client = get_object_or_404(Client, id=self.request.data.get('client'))
            gage.save(client=client)
            return Response(gage.data, status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        gage = get_object_or_404(TestGAGE.objects.all(), pk=pk)
        serializer = TestGAGECRUDSerializers(instance=gage, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        socrates = get_object_or_404(TestGAGE.objects.all(), pk=pk)
        socrates.delete()
        return Response(status=201)


class GraphicGAGEView(APIView):
    """Получение значений двух интерпретаций тестов GAGE для графика"""

    def get(self, request):
        """
        Получение значений

        :param request: Запрос с id интерпретаций тестов GAGE
        :return: Значения по двум интерпретациям
        """
        client = request.GET.get("client")
        tests = TestGAGE.objects.filter(client=client)
        interpretation_1 = InterpretationGAGE.objects.filter(test=tests.values('id').first().get('id'))
        interpretation_2 = InterpretationGAGE.objects.filter(test=tests.values('id').last().get('id'))
        serializer_1 = InterpretationGAGECRUDSerializers(interpretation_1, many=True)
        serializer_2 = InterpretationGAGECRUDSerializers(interpretation_2, many=True)
        labels = {}
        for field in InterpretationGAGE._meta.get_fields():
            if not field.is_relation:
                if field.name != 'id':
                    labels[field.name] = field.verbose_name
        return Response({'labels': labels, 'data': [
            {'test': serializer_1.data, 'attempt': tests.values('attempt').first().get('attempt')},
            {'test': serializer_2.data, 'attempt': tests.values('attempt').last().get('attempt')}]})


class InterpretationGAGEView(APIView):
    """Интерпретация теста GAGE"""

    def get(self, request):
        """
        Получение записи

        :param request: Запрос с id Теста GAGE
        :return: Интерпретация теста GAGE, в случае отсутствия записи No Content
        """
        test = request.GET.get("test")
        result = InterpretationGAGE.objects.filter(test=test)
        if result.exists():
            serializer = InterpretationGAGESerializers(result, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        result = InterpretationGAGECRUDSerializers(data=request.data)
        if result.is_valid():
            test = get_object_or_404(TestGAGE, id=self.request.data.get('test'))
            result.save(test=test)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :return: Статус Created
        """
        result = get_object_or_404(InterpretationGAGE.objects.all(), test=self.request.data.get('test'))
        serializer = InterpretationGAGECRUDSerializers(instance=result, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)


class TestSOCRATESListView(APIView):
    """Список тестов SOCRATES"""

    def get(self, request):
        """
        Получение списка

        :param request: Запрос с id клиента
        :return: Список
        """
        client = request.GET.get("client")
        tests = TestSOCRATES.objects.filter(client=client)
        serializer = TestSOCRATESListSerializers(tests, many=True)
        return Response(serializer.data)


class TestSOCRATESView(APIView):
    """Тест SOCRATES"""

    def get(self, request, pk=None):
        """
        Получение записи

        :param request: Запрос с id Теста SOCRATES
        :param pk: id Теста SOCRATES
        :return: Тест SOCRATES, в случае отсутствия записи No Content
        """
        if pk is None:
            test = request.GET.get("test")
        else:
            test = pk
        socrates = TestSOCRATES.objects.filter(pk=test)
        if socrates.exists():
            if pk is None:
                serializer = TestSOCRATESSerializers(socrates, many=True)
            else:
                serializer = TestSOCRATESCRUDSerializers(socrates, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        socrates = TestSOCRATESCRUDSerializers(data=request.data)
        if socrates.is_valid():
            client = get_object_or_404(Client, id=self.request.data.get('client'))
            socrates.save(client=client)
            return Response(socrates.data, status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        socrates = get_object_or_404(TestSOCRATES.objects.all(), pk=pk)
        serializer = TestSOCRATESCRUDSerializers(instance=socrates, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        socrates = get_object_or_404(TestSOCRATES.objects.all(), pk=pk)
        socrates.delete()
        return Response(status=201)


class GraphicSOCRATESView(APIView):
    """Получение значений двух тестов SOCRATES для графика"""

    def get(self, request):
        """
        Получение значений

        :param request: Запрос с id интерпретаций тестов SOCRATES
        :return: Значения по двум интерпретациям
        """
        client = request.GET.get("client")
        tests = TestSOCRATES.objects.filter(client=client)
        interpretation_1 = InterpretationSOCRATES.objects.filter(test=tests.values('id').first().get('id'))
        interpretation_2 = InterpretationSOCRATES.objects.filter(test=tests.values('id').last().get('id'))
        serializer_1 = InterpretationSOCRATESCRUDSerializers(interpretation_1, many=True)
        serializer_2 = InterpretationSOCRATESCRUDSerializers(interpretation_2, many=True)
        labels = {}
        for field in InterpretationSOCRATES._meta.get_fields():
            if not field.is_relation:
                if field.name != 'id':
                    labels[field.name] = field.verbose_name
        return Response({'labels': labels, 'data': [
            {'test': serializer_1.data, 'attempt': tests.values('attempt').first().get('attempt')},
            {'test': serializer_2.data, 'attempt': tests.values('attempt').last().get('attempt')}]})


class InterpretationSOCRATESView(APIView):
    """Интерпретация теста SOCRATES"""

    def get(self, request):
        """
        Получение записи

        :param request: Запрос с id Теста SOCRATES
        :return: Интерпретация теста SOCRATES, в случае отсутствия записи No Content
        """
        test = request.GET.get("test")
        result = InterpretationSOCRATES.objects.filter(test=test)
        if result.exists():
            serializer = InterpretationSOCRATESSerializers(result, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        result = InterpretationSOCRATESCRUDSerializers(data=request.data)
        if result.is_valid():
            test = get_object_or_404(TestSOCRATES, id=self.request.data.get('test'))
            result.save(test=test)
            return Response(status=201)
        else:
            return Response(status=400)

    def put(self, request):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :return: Статус Created
        """
        result = get_object_or_404(InterpretationSOCRATES.objects.all(), test=self.request.data.get('test'))
        serializer = InterpretationSOCRATESCRUDSerializers(instance=result, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)


class TypologicalGroupListView(APIView):
    """Список типологических групп"""

    def get(self, request):
        """
        Получение списка

        :param request: Запрос с id клиента
        :return: Список
        """
        client = request.GET.get("client")
        tests = TypologicalGroup.objects.filter(client=client)
        serializer = TypologicalGroupListSerializers(tests, many=True)
        return Response({"data": serializer.data})


class TypologicalGroupView(APIView):
    """Типологическая группа"""

    def get(self, request):
        """
        Получение записи

        :param request: Запрос с id Типологической группы
        :return: Типологическая группа, в случае отсутствия записи No Content
        """
        group_id = request.GET.get("group")
        group = TypologicalGroup.objects.filter(pk=group_id)
        if group.exists():
            serializer = TypologicalGroupSerializers(group, many=True)
            return Response(serializer.data)
        else:
            return Response(status=204)

    def post(self, request):
        """
        Создание записи

        :param request: Запрос с новыми данными
        :return: Статус Created, в случае ошибки создания Bad Request
        """
        group = TypologicalGroupCRUDSerializers(data=request.data)
        if group.is_valid():
            client = get_object_or_404(Client, id=self.request.data.get('client'))
            test = get_object_or_404(TestBoyko, id=self.request.data.get('test'))
            group.save(client=client, test=test)
            return Response(group.data, status=201)
        else:
            return Response(status=400)

    def put(self, request, pk):
        """
        Обновление записи

        :param request: Запрос с обновленными данными
        :param pk: id обновляемой записи
        :return: Статус Created
        """
        group = get_object_or_404(TypologicalGroup.objects.all(), pk=pk)
        serializer = TypologicalGroupCRUDSerializers(instance=group, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(status=201)

    def delete(self, request, pk):
        """
        Удаление записи

        :param request: Запрос
        :param pk: id удаляемой записи
        :return: Статус Created
        """
        group = get_object_or_404(TypologicalGroup.objects.all(), pk=pk)
        group.delete()
        return Response(status=201)


class FieldsGroupView(APIView):
    """Список полей для определения Типологической группы"""

    def get(self, request):
        """
        Получения списка

        :param request: Запрос с id клиента и id Теста Бойко
        :return: Список
        """
        client = request.GET.get("client")
        test = request.GET.get("test")
        social_behavior = ASocialBehavior.objects.filter(client=client)
        boyko = TestBoyko.objects.filter(pk=test)
        general_info = Client.objects.filter(pk=client)
        chronic_disease = ChronicDisease.objects.filter(client=client)
        serializer_social_behavior = GroupASocialBehaviorSerializers(social_behavior, many=True)
        serializer_general_info = GroupClientSerializers(general_info, many=True)
        serializer_chronic_disease = GroupChronicDiseaseSerializers(chronic_disease, many=True)
        serializer_boyko = GroupTestBoykoSerializers(boyko, many=True)
        return Response(
            {"social_behavior": serializer_social_behavior.data, "general_info": serializer_general_info.data,
             "chronic_disease": serializer_chronic_disease.data,
             "boyko": serializer_boyko.data})


def get_model_fields(model):
    """
    Получение обозначений, выборов и значений полей

    :param model: Выбранная модель
    :return: Обозначения, выборка и значения полей модели
    """
    labels = {}
    choices = {}
    items = {}
    for field in model._meta.get_fields():
        if not field.is_relation:
            if field.name != 'id':
                labels[field.name] = field.verbose_name
                items[field.name] = ''
            if field.choices is not None:
                buf = []
                for item in field.choices:
                    buf.append({'value': item[0], 'text': item[1]})
                choices[field.name] = buf
    return {'labels': labels, 'choices': choices, 'items': items}


MODEL = {'Client': Client, 'ASocialBehavior': ASocialBehavior,
         'ChronicDisease': ChronicDisease, 'Child': Child,
         'FamilyMembersInformation': FamilyMembersInformation, 'HusbandInformation': HusbandInformation,
         'SocialLivingCondition': SocialLivingCondition, 'SocialEconomicCondition': SocialEconomicCondition,
         'SourceIncome': SourceIncome, 'SocialPayment': SocialPayment,
         'ChildAllowanceAndCompensation': ChildAllowanceAndCompensation, 'Facilities': Facilities,
         'ExpertOpinion': ExpertOpinion, 'TestBoyko': TestBoyko, 'TestGAGE': TestGAGE, 'TestSOCRATES': TestSOCRATES}


class FieldsView(APIView):
    """Обозначения, выборы и значения для модели"""

    def get(self, request):
        """
        Получение полей

        :param request: Запрос с моделью
        :return: Поля
        """
        model = request.GET.get("model")
        fields = get_model_fields(MODEL.get(model))
        return Response(fields)

    # fields = GeneralInformation._meta.get_fields()
    # my_model_fields = [field.name for field in GeneralInformation._meta.get_fields()]


from rest_framework.permissions import IsAdminUser


class UserCRUDView(APIView):
    """Пользователь (специалист)"""
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        Информация о пользователях

        :param request: Запрос
        :return: Информация о пользователях
        """
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Создание пользователя

        :param request: Запрос с новыми данными
        :return: Статус Created
        """
        data = dict(
            [('username', None), ('email', None), ('password', None), ('first_name', None), ('patronymic', None),
             ('last_name', None), ('position', None)])
        for key in data.keys():
            data[key] = self.request.data.get(key)
        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'],
                                        first_name=data['first_name'], patronymic=data['patronymic'],
                                        last_name=data['last_name'], position=data['position'])
        user.save()
        return Response(status=201)

    def delete(self, request):
        """
        Удаление пользователя

        :param request: Запрос с username пользователя
        :return: Статус Created
        """
        user = get_object_or_404(User, username=request.data.get('username'))
        user.delete()
        return Response(status=201)


########################################################################################################################

def getIDFN(serializer):
    dataArray = [["ФИО клиента"], {}]
    for value in serializer.data:
        dataArray[1].update({value.get("id"): [value.get("full_name")]})
    return dataArray


def husbendSpecial(serializer):
    # newSer=FamilyMemberSpecial(FamilyMembersInformation.objects.all(), many=True).data
    # newSer=serializer
    myLiz = serializer
    for value in serializer.data:
        value.get('labels').update({'client': 'client'})
        value.get('labels').pop('husband')

        for hus in FamilyMemberSpecial(FamilyMembersInformation.objects.all(), many=True).data:
            if value.get('husband') == hus.get('id'):
                # print("yes")
                value.update({'client': hus.get('client')})
        value.pop('husband')

    return serializer


def getInformation(serializer):
    i = 0
    dat = []
    dat.append(serializer.data[0].get('labels'))
    while i < len(serializer.data):
        serializer.data[i].pop('labels')
        i = i + 1
    dat.append(serializer.data)
    # print(dat)
    return dat


def deleteIDClient(serializer):
    # print(serializer.data)
    newArray = []
    array = getInformation(serializer)
    for direct in array[1]:
        copy = direct.copy()
        direct.clear()
        for key in array[0].keys():
            direct.update({key: copy.get(key)})
        direct.update({'client': copy.get('client')})
        # print(copy.get('client'))
    array[0].pop("id")
    array[0].pop("client")
    newArray.append(array[0].values())
    newArray.append({})
    for value in array[1]:
        buf = value.get("client")
        value.pop("id")
        value.pop("client")
        newArray[1].update({buf: value.values()})
    return newArray


def deleteExcessDataFromChild(serializer):
    newArray = [[]]
    array = getInformation(serializer)
    array[0].pop('id')
    array[0].pop('client')
    countArray = []

    for value in array[1]:
        countArray.append(value.get('client'))
    NumChildFromClient = Counter(countArray)
    maxCountChild = max(NumChildFromClient.values())
    countLabels = len(array[0])
    for i in range(maxCountChild):
        for value in array[0].values():
            newArray[0].append(value)
            # newArray[0].append(value + "(" + str(i + 1) + ")")
        # newArray[0].extend(array[0])
    # newArray.append(array[0])
    newArray.append({})

    # print(NumChildFromClient.items())
    for item in NumChildFromClient.items():
        # print("_______________")
        newArray[1].update({item[0]: []})
        count = item[1]
        while count > 0:
            # print("__________")

            # i=1
            for data in array[1]:
                # print(i)
                # i=i+1
                # print("__________")
                # print(data)
                if data.get('client') == item[0]:
                    count = count - 1
                    # print("client"+str(item[0]))
                    for key in array[0].keys():
                        newArray[1].get(item[0]).append(data.get(key))
    newArray.append({})
    for i in range(maxCountChild):
        newArray[2].update({
            'child' + str(i + 1): {
                'nameRUS': str(i + 1) + 'ый ' + 'ребенок',
                'firstPoint': None,
                'lastPoint': None,
                'lenLabels': len(newArray[0]) // maxCountChild
            }
        })
    return newArray


def socialEconomCon():
    mainSerializer = SocialEconomicConditionSerializers(SocialEconomicCondition.objects.all(), many=True)
    arraySer = []
    if (len(SourceIncomeSerializers(SourceIncome.objects.all(), many=True).data) != 0):
        arraySer.append(SourceIncomeSerializers(SourceIncome.objects.all(), many=True))
    if (len(SocialPaymentSerializers(SocialPayment.objects.all(), many=True).data) != 0):
        arraySer.append(SocialPaymentSerializers(SocialPayment.objects.all(), many=True))
    if (len(ChildAllowanceAndCompensationSerializers(ChildAllowanceAndCompensation.objects.all(),
                                                     many=True).data) != 0):
        arraySer.append(
            ChildAllowanceAndCompensationSerializers(ChildAllowanceAndCompensation.objects.all(), many=True))
    if (len(FacilitiesSerializers(Facilities.objects.all(), many=True).data) != 0):
        arraySer.append(FacilitiesSerializers(Facilities.objects.all(), many=True))

    for serializer in arraySer:
        for value in serializer.data:
            for val in mainSerializer.data:
                if value.get('economic_condition') == val.get('id'):
                    value.update({'client': val.get('client')})
            value.get('labels').pop('economic_condition')
            value.get('labels').update({'client': 'client'})
            value.pop('economic_condition')
    finishArray = [[], {}]
    mainSerializer = deleteIDClient(mainSerializer)
    finishArray[0].extend(mainSerializer[0])
    for key, item in mainSerializer[1].items():
        finishArray[1].update({key: []})
        finishArray[1].get(key).extend(item)
    # finishArray.append(mainSerializer[1])

    for value in arraySer:
        value = deleteIDClient(value)
        finishArray[0].extend(value[0])
        count = len(finishArray[0])
        for key, val in value[1].items():
            finishArray[1].get(key).extend(val)
        for key, item in finishArray[1].items():

            if len(item) < count:
                difference = count - len(item)
                while (difference > 0):
                    difference = difference - 1
                    item.append("")

    # print(finishArray)

    return finishArray

    # SocialPaymentSerializers(SocialPayment.objects.all(), many=True)
    # ChildAllowanceAndCompensationSerializers(ChildAllowanceAndCompensation.objects.all(), many=True)
    # FacilitiesSerializers(Facilities.objects.all(), many=True)


class TestMy():
    def __init__(self, inArray):
        self.array = inArray

    # def setData(array):
    #     array=array
    def data(self):
        return self.array


def testAndRes(num, firstSerializer, secondSerializer):
    # attempt 0-Первая попытка,1-Вторая попытка
    attemptAr = [
        'Первичная',
        'Вторичная'
    ]
    newArray = getIDFN(ClientSerializers(Client.objects.all(), many=True))
    newArray[0].clear()
    for value in newArray[1].values():
        value.clear()
    # print(newArray)
    for value in firstSerializer.data:
        if value.get('attempt') == attemptAr[num]:
            value.get('labels').pop('attempt')
            value.pop('attempt')
            for inter in secondSerializer.data:
                if value.get('id') == inter.get('test'):
                    inter.get('labels').update({'client': 'client'})
                    inter.update({'client': value.get('client')})
                    inter.get('labels').pop('test')
                    inter.pop('test')
        else:
            value.get('labels').pop('attempt')
            value.pop('attempt')
            value.pop('client')
            value.update({'client': None})

    for value in secondSerializer.data:
        if (value.get('client') == None):
            value.get('labels').update({'client': 'client'})
            value.update({'client': None})
            value.get('labels').pop('test')
            value.pop('test')

    # for key in ar[1].keys():
    #     dataArray[1].get(key).extend(ar[1].get(key))

    bufArray = deleteIDClient(firstSerializer)
    # bufInt=deleteIDClient(secondSerializer)
    newArray[0].extend(bufArray[0])
    # print(newArray)
    for key, item in bufArray[1].items():
        if key != None:
            newArray[1].get(key).extend(item)
    bufArray = deleteIDClient(secondSerializer)
    newArray[0].extend(bufArray[0])
    for key, item in bufArray[1].items():
        if key != None:
            newArray[1].get(key).extend(item)

    count = len(newArray[0])
    for key in newArray[1].keys():
        if len(newArray[1].get(key)) < count:
            difference = count - len(newArray[1].get(key))
            while (difference > 0):
                difference = difference - 1
                newArray[1].get(key).append("")

    # newObject2.setData(intArray)
    # newObject2=TestMy(intArray)
    # print(newObject2.data())
    # for value in serArray:
    #     boykoSerializer.data.append(value)
    #
    # for value in boykoSerializer.data:
    #     print(value)

    # for value in intArray:
    #     boykoInterpretation.data.append(value)
    #
    # for value in boykoInterpretation.data:
    #     print(value)

    # boykoSerializer.data.clear()
    # boykoInterpretation.data.clear()
    # print("-_-_-_-_-_-_-_-_-_-")
    # print(boykoInterpretation.data)
    # for value in intArray:
    #     print("__________________")
    #     boykoInterpretation.data.append(value)
    # return deleteIDClient(newObject2)
    # return deleteIDClient(boykoInterpretation)
    # return deleteIDClient(boykoSerializer)
    # return boykoSerializer.data
    return newArray


def expertOpinion(serializer):
    expertSerializer = ExpertForTable(User.objects.all(), many=True).data
    # for value in ExpertForTable(User.objects.all(), many=True).data:
    #     print("____________________-")
    #     print(value)
    # print("ttttttttttttttttttttt")
    for value in serializer.data:
        # print("____________________-")
        for expert in expertSerializer:
            if value.get('specialist') == expert.get('id'):
                value.update({'first_name_ex': expert.get('first_name')})
                value.update({'last_name_ex': expert.get('last_name')})
                value.get('labels').update({'first_name_ex': 'Имя специалиста'})
                value.get('labels').update({'last_name_ex': 'Фамилия специалиста'})
                value.get('labels').pop('specialist')
                value.pop('specialist')

    # print(deleteIDClient(serializer))
    return serializer


def deleteIDForClient(serializer):
    newArray = []
    array = getInformation(serializer)
    for direct in array[1]:
        copy = direct.copy()
        direct.clear()
        passArray = ''
        for key in array[0].keys():

            # print(key + ' ')
            if key == 'passSeries' or key == 'passNumber':

                if copy.get(key)==None:
                    print(copy.get(key))
                    passArray=passArray
                else:
                    passArray = passArray+" "+str(copy.get(key))
                direct.update({'passSeries':passArray})
            else:
                direct.update({key: copy.get(key)})

        # direct.pop('passNumber')
        direct.update({'id': copy.get('id')})
        # print(copy.get('client'))
    array[0].pop('passNumber')
    array[0].update({'passSeries':"Серия,номер"})
    # array[0].pop("id")
    # array[0].pop("client")
    # newArray.append(array[0].values())
    # newArray.append({})
    # for value in array[1]:
    #     buf = value.get("client")
    #     value.pop("id")
    #     value.pop("client")
    #     newArray[1].update({buf: value.values()})

    # newArray = []
    # array = getInformation(serializer)
    array[0].pop("id")
    array[0].pop("full_name")
    newArray.append(array[0].values())
    newArray.append({})
    for value in array[1]:
        buf = value.get("id")
        value.pop("id")
        value.pop("full_name")
        newArray[1].update({buf: value.values()})

    # print(newArray)
    return newArray


def makeMarking(array, nameEN, nameRUS):
    array.append({
        nameEN: {
            'nameRUS': nameRUS,
            'firstPoint': None,
            'lastPoint': None,
            'lenLabels': len(array[0])
        }
    })
    return array


def updateMarking(lastPoint, dictionary):
    for dict in dictionary.values():
        dict.update({'firstPoint': lastPoint})
        dict.update({'lastPoint': dict.get('firstPoint') + dict.get('lenLabels') - 1})
        lastPoint = dict.get('lastPoint') + 1


def mySwitch(value):
    if value == "0":

        # return deleteIDForClient(ClientSerializers(Client.objects.all(), many=True))
        if (len(ClientSerializers(Client.objects.all(), many=True).data) == 0):
            return []
        return makeMarking(
            deleteIDForClient(ClientSerializers(Client.objects.all(), many=True)),
            'generalInformation',
            'Общая информация'
        )
    # elif value == "1":
    #     if (len(GeneralInformationSerializers(GeneralInformation.objects.all(), many=True).data) == 0):
    #         return []
    #     # return deleteIDClient(GeneralInformationSerializers(GeneralInformation.objects.all(), many=True))
    #     return makeMarking(
    #         deleteIDClient(GeneralInformationSerializers(GeneralInformation.objects.all(), many=True)),
    #         'generalInformation',
    #         'Общая информация'
    #     )
    elif value == "1":
        if (len(ASocialBehaviorSerializers(ASocialBehavior.objects.all(), many=True).data) == 0):
            return []
        # return deleteIDClient(ASocialBehaviorSerializers(ASocialBehavior.objects.all(), many=True))
        return makeMarking(
            deleteIDClient(ASocialBehaviorSerializers(ASocialBehavior.objects.all(), many=True)),
            'alcoholDrugsClient',
            'Информация о противоправных действиях, правонарушениях, употреблении наркотиков, алкоголя'
        )
    elif value == "2":
        if (len(ChronicDiseaseSerializers(ChronicDisease.objects.all(), many=True).data) == 0):
            return []
        # return deleteIDClient(ChronicDiseaseSerializers(ChronicDisease.objects.all(), many=True))
        return makeMarking(
            deleteIDClient(ChronicDiseaseSerializers(ChronicDisease.objects.all(), many=True)),
            'chronicDisease',
            'Информация о наличии хронического заболевания'
        )
    elif value == "3":
        if (len(ChildSerializers(Child.objects.all(), many=True).data) == 0):
            return []
        return deleteExcessDataFromChild(ChildSerializers(Child.objects.all(), many=True))
    elif value == "4":
        if (len(FamilyMembersInformationSerializers(FamilyMembersInformation.objects.all(), many=True).data) == 0):
            return []
        # return deleteIDClient(FamilyMembersInformationSerializers(FamilyMembersInformation.objects.all(), many=True))
        return makeMarking(
            deleteIDClient(FamilyMembersInformationSerializers(FamilyMembersInformation.objects.all(), many=True)),
            'generalInformationFamily',
            'Общие сведения о членах семьи'
        )
    elif value == "5":
        if (len(HusbandInformationSerializers(HusbandInformation.objects.all(), many=True).data) == 0):
            return []
        # return deleteIDClient(
        #     husbendSpecial(HusbandInformationSerializers(HusbandInformation.objects.all(), many=True)))
        return makeMarking(
            deleteIDClient(husbendSpecial(HusbandInformationSerializers(HusbandInformation.objects.all(), many=True))),
            'husbendInformation',
            'Информация о муже/партнёре'
        )
    elif value == "6":
        if (len(SocialLivingConditionSerializers(SocialLivingCondition.objects.all(), many=True).data) == 0):
            return []
        return makeMarking(
            deleteIDClient(SocialLivingConditionSerializers(SocialLivingCondition.objects.all(), many=True)),
            'socialLivingConditions',
            'Социально-бытовые условия'
        )
        # return deleteIDClient(SocialLivingConditionSerializers(SocialLivingCondition.objects.all(), many=True))
    elif value == "7":
        if (len(SocialEconomicConditionSerializers(SocialEconomicCondition.objects.all(), many=True).data) == 0):
            return []
        return makeMarking(
            socialEconomCon(),
            'socialEconomConditions',
            'Социально-экономические условия проживания'
        )
    elif value == "8":
        if (len(ExpertOpinionSerializers(ExpertOpinion.objects.all(), many=True).data) == 0):
            return []
        return makeMarking(
            deleteIDClient(expertOpinion(ExpertOpinionSerializers(ExpertOpinion.objects.all(), many=True))),
            'expertOpinion',
            'Заключение специалиста'
        )
        # return deleteIDClient(expertOpinion(ExpertOpinionSerializers(ExpertOpinion.objects.all(), many=True)))
    elif value == "9":
        if (len(TestBoykoSerializers(TestBoyko.objects.all(), many=True).data) == 0):
            return []
        return makeMarking(
            testAndRes(0,
                       TestBoykoSerializers(TestBoyko.objects.all(), many=True),
                       InterpretationBoykoSerializers(InterpretationBoyko.objects.all(), many=True)),
            'boykoFirst',
            'Первичная диагностика/Бойко'
        )
        # return testAndRes(0, TestBoykoSerializers(TestBoyko.objects.all(), many=True),
        # InterpretationBoykoSerializers(InterpretationBoyko.objects.all(), many=True))
    elif value == "10":
        if (len(TestGAGESerializers(TestGAGE.objects.all(), many=True).data) == 0):
            return []
        return makeMarking(
            testAndRes(0, TestGAGESerializers(TestGAGE.objects.all(), many=True),
                       InterpretationGAGESerializers(InterpretationGAGE.objects.all(), many=True)),
            'GAGEFirst',
            'Первичная диагностика/GAGE'
        )
        # return testAndRes(0, TestGAGESerializers(TestGAGE.objects.all(), many=True),
        #                   InterpretationGAGESerializers(InterpretationGAGE.objects.all(), many=True))
    elif value == "11":
        if (len(TestSOCRATESSerializers(TestSOCRATES.objects.all(), many=True).data) == 0):
            return []
        return makeMarking(
            testAndRes(0, TestSOCRATESSerializers(TestSOCRATES.objects.all(), many=True),
                       InterpretationSOCRATESSerializers(InterpretationSOCRATES.objects.all(), many=True)),
            'SOCRATESFirst',
            'Первичная диагностика/SOCRATES'
        )
        # return testAndRes(0, TestSOCRATESSerializers(TestSOCRATES.objects.all(), many=True),
        #                   InterpretationSOCRATESSerializers(InterpretationSOCRATES.objects.all(), many=True))
    elif value == "12":
        if (len(TestBoykoSerializers(TestBoyko.objects.all(), many=True).data) == 0):
            return []
        return makeMarking(
            testAndRes(1, TestBoykoSerializers(TestBoyko.objects.all(), many=True),
                       InterpretationBoykoSerializers(InterpretationBoyko.objects.all(), many=True)),
            'boykoSecond',
            'Вторичная диагностика/Бойко'
        )
        # return testAndRes(1, TestBoykoSerializers(TestBoyko.objects.all(), many=True),
        #                   InterpretationBoykoSerializers(InterpretationBoyko.objects.all(), many=True))
    elif value == "13":
        if (len(TestGAGESerializers(TestGAGE.objects.all(), many=True).data) == 0):
            return []
        return makeMarking(
            testAndRes(1, TestGAGESerializers(TestGAGE.objects.all(), many=True),
                       InterpretationGAGESerializers(InterpretationGAGE.objects.all(), many=True)),
            'GAGESecond',
            'Вторичная диагностика/GAGE'
        )
        # return testAndRes(1, TestGAGESerializers(TestGAGE.objects.all(), many=True),
        #                   InterpretationGAGESerializers(InterpretationGAGE.objects.all(), many=True))
    elif value == "14":
        if (len(TestSOCRATESSerializers(TestSOCRATES.objects.all(), many=True).data) == 0):
            return []
        return makeMarking(
            testAndRes(1, TestSOCRATESSerializers(TestSOCRATES.objects.all(), many=True),
                       InterpretationSOCRATESSerializers(InterpretationSOCRATES.objects.all(), many=True)),
            'SOCRATESSecond',
            'Вторичная диагностика/SOCRATES'
        )
        # return testAndRes(1, TestSOCRATESSerializers(TestSOCRATES.objects.all(), many=True),
        #                   InterpretationSOCRATESSerializers(InterpretationSOCRATES.objects.all(), many=True))
    else:
        return -1


class Table:
    __size = 0
    __id_array = None
    __parent_id = None
    __labels = None
    __serializer = None
    __parent_table = None
    __table_body = None

    def __init__(self, **kwargs):
        self.serializer = kwargs.get("serializer")
        self.parent_table = kwargs.get("parent_table")

    #############################################
    #############################################
    ###||||||||||||||||||||||||||||||||||||||
    #############################################
    #############################################
    def __set_labels(self, labels):
        if labels is not None:
            print("__set_labels")
            self.__labels = labels

    def __get_labels(self):
        print("__get_labels")
        return self.__labels

    def __set_serializer(self, serializer):
        if serializer is not None and len(serializer.data) > 0:
            print("__set_serializer")
            self.__serializer = serializer
            self.labels = serializer.data[0].get('labels')

    def __get_serializer(self):
        print("__get_serializer")
        return self.__serializer

    def __set_parent_table(self, parent_table):
        if parent_table is not None:
            print("__set_parent_table")
            self.__parent_table = parent_table

    def __get_parent_table(self):
        print("__get_parent_table")
        return self.__parent_table

    ############################
    ############################
    ### дописать функционал, чтобы при установки списка id, дописывались новые данные в список(все null)
    def __set_id_array(self, id_array):
        if id_array is not None:
            print("__set_id_array")
            self.__id_array = id_array

    def __get_id_array(self):
        print("__get_id_array")
        return self.__id_array

    labels = property(__get_labels, __set_labels)
    serializer = property(__get_serializer, __set_serializer)
    id_array = property(__get_id_array, __set_id_array)
    parent_table = property(__get_parent_table, __set_parent_table)

    def __get_body(self):
        if self.serializer is not None:
            # print(self.serializer)
            for value in self.serializer.data:
                print(value)

    def __get_id_array(self):
        self.__id_array = self.__get_and_delete_special_field(self.serializer.data, ["id"])

    def __get_special_fields(self, list, fields):
        if list is not None:
            array = []
            for value in list:
                buf_array = []
                for field in fields:
                    buf_array.append(value.get(field))
                array.append(buf_array)
            return array
        else:
            return None

    def __delete_special_fields(self, list, fields):
        if list is not None:
            for value in list:
                for field in fields:
                    value.pop(field)

    def __get_and_delete_special_field(self, list, fields):
        if list is not None:
            array = []
            for value in list:
                buf_array = []
                for field in fields:
                    buf_array.append(value.get(field))
                    value.pop(field)
                array.append(buf_array)
            return array
        else:
            return None

    def start(self):
        self.labels.pop("id")

        for i in self.__get_special_fields(self.serializer.data, self.labels):
            print(i)
        # print(self.__get_special_fields(self.serializer.data,self.labels))
        # self.__get_body()
        # self.__get_id_array()
        # print(self.__id_array)
    # def __comparison(self):

    # def __parse_labels_from_serializer(self):
    #     return


class GetTable(APIView):

    def get(self, request):
        # print(ChronicDiseaseSerializers(ChronicDisease.objects.all(), many=True).data)

        # table = Table(serializer=ClientSerializers(Client.objects.all(), many=True))
        # table.start()
        #
        # return Response([])

        dataArray = getIDFN(ClientSerializers(Client.objects.all(), many=True))
        dataArray.append({
            'fio': {
                'nameRUS': 'ФИО',
                'firstPoint': 0,
                'lastPoint': 0,
                'lenLabels': 1
            }
        })
        for num in request.GET.get("tables").split(","):
            # print(type(num))
            # print(num)
            ar = mySwitch(num)
            if (len(ar) != 0):
                lastPoint = len(dataArray[0])
                dataArray[0].extend(ar[0])

                # lastPoint=dataArray[2]
                updateMarking(lastPoint, ar[2])
                # for dict in ar[2].values():
                #         dict.update({'firstPoint':lastPoint})
                #         dict.update({'lastPoint':dict.get('firstPoint')+dict.get('lenLabels')-1})
                #         lastPoint=dict.get('lastPoint')+1
                dataArray[2].update(ar[2])
                for key in ar[1].keys():
                    dataArray[1].get(key).extend(ar[1].get(key))
                count = len(dataArray[0])
                for key in dataArray[1].keys():
                    if len(dataArray[1].get(key)) < count:
                        difference = count - len(dataArray[1].get(key))
                        while (difference > 0):
                            difference = difference - 1
                            dataArray[1].get(key).append("")

        print('len:' + str(len(dataArray[0])))
        return Response(dataArray)


class TestsAnswers(APIView):
    def get(self, request):
        dict = {'boyko': {}}
        fileds = ['aggressiveness',
                  'alarm',
                  'memory_disorder',
                  'criticism',
                  'self_service',
                  'work_activity',
                  'friends',
                  'family_relation',
                  'child_parent',
                  'leisure']
        num = 1
        for filed in fileds:
            name = TestBoyko._meta.get_field(filed).verbose_name
            dict.get('boyko').update({num: {}})
            dict.get('boyko').get(num).update({'label': name})
            choices = []
            for choice in TestBoyko._meta.get_field(filed).choices:
                choices.append(choice[1])
            dict.get('boyko').get(num).update({
                'answers': choices
            })
            num = num + 1
        return Response(dict)

