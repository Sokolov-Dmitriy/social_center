from rest_framework import serializers
from social_center_app.models import *
from rest_framework.fields import SerializerMethodField


class MyModelSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода описаний полей"""

    def __init__(self, *args, **kwargs):
        super(MyModelSerializer, self).__init__(*args, **kwargs)

        if 'labels' in self.fields:
            raise RuntimeError(
                'You cant have labels field defined '
                'while using MyModelSerializer'
            )

        self.fields['labels'] = SerializerMethodField()

    def get_labels(self, *args):
        """
        Функция для получения словаря labels с названием поля и его описанием

        :param args: Аргументы
        :return: Словарь labels
        """
        labels = {}

        for field in self.Meta.model._meta.get_fields():
            if field.name in self.fields:
                labels[field.name] = field.verbose_name

        return labels


class ChoiceField(serializers.ChoiceField):
    """Вывод вариантов полей"""

    def to_representation(self, obj):
        """
        Функция для получения вариантов поля

        :param obj: Объект, содержащий выборку
        :return: Список полей
        """
        return self._choices[obj]


class ClientListForMainWindow(serializers.ModelSerializer):
    """Информация о клиенте для главного окна"""

    class Meta:
        model = Client
        fields = ("contractNumber", "code", "full_name")


class ClientSerializers(MyModelSerializer):
    """Клиент"""
    formOfReferral = ChoiceField(choices=Client.FORM_OF_REFERRAL)
    placementSocialSupport = ChoiceField(choices=Client.PLACEMENT_SOCIAL_SUPPORT)
    sex = ChoiceField(choices=Client.SEX)
    registrationMunicipalDistrict = ChoiceField(choices=Client.MUNICIPAL_DISTRICT)
    actualMunicipalDistrict = ChoiceField(choices=Client.MUNICIPAL_DISTRICT)
    dependence = ChoiceField(choices=Client.DEPENDENCE)
    stateOfDependence = ChoiceField(choices=Client.STATE_OF_DEPENDENCE)
    workPlace = ChoiceField(choices=Client.WORK_PLACE)
    avDoc = ChoiceField(choices=YESNO)
    cityzenship = ChoiceField(choices=Client.CITYZENSHIP)
    registration = ChoiceField(choices=Client.REGISTRATION)
    placeOfRegistration = ChoiceField(choices=Client.PLACE_OF_REGISTRATION)
    education = ChoiceField(choices=Client.EDUCATION)
    familiesCategory = ChoiceField(choices=Client.FAMILIES_CATEGORY)
    disability = ChoiceField(choices=YESNO)
    escort = ChoiceField(choices=Client.ESCORT)

    class Meta:
        model = Client
        fields = '__all__'


class ClientCRUDSerializers(serializers.ModelSerializer):
    """Клиент без обозначений и вариантов полей"""

    class Meta:
        model = Client
        fields = '__all__'


class ChildListSerializers(serializers.ModelSerializer):
    """Список детей клиента"""
    sex = ChoiceField(choices=Child.SEX)

    class Meta:
        model = Child
        fields = ('full_name', 'sex', 'age')


class ChildSerializers(MyModelSerializer):
    """Ребенок"""
    placementSocialSupport = ChoiceField(choices=Child.PLACEMENT_SOCIAL_SUPPORT)
    sex = ChoiceField(choices=Child.SEX)
    status = ChoiceField(choices=Child.STATUS)
    location = ChoiceField(choices=Child.LOCATION)
    documents = ChoiceField(choices=YESNO)
    fatherhood = ChoiceField(choices=YESNO)
    education = ChoiceField(choices=YESNO)
    educate_child = ChoiceField(choices=Child.EDUCATE)
    reason_refusal = ChoiceField(choices=Child.REASON)

    health = ChoiceField(choices=YESNO)
    withdrawal_symptoms = ChoiceField(choices=YES_NO_DONTKNOW)
    with_mother = ChoiceField(choices=YES_NO_DONTKNOW)
    hiv_status_child = ChoiceField(choices=Child.HIV)
    hiv_plus = ChoiceField(choices=YESNO)
    center_aids = ChoiceField(choices=YESNO)
    hiv_prevention = ChoiceField(choices=YES_NO_DONTKNOW)
    dependence = ChoiceField(choices=Child.DEPENDENCE)

    class Meta:
        model = Child
        fields = '__all__'


class ChildCRUDSerializers(serializers.ModelSerializer):
    """Информация о ребенке без обозначений и вариантов полей"""

    class Meta:
        model = Child
        fields = '__all__'


class SocialLivingConditionSerializers(MyModelSerializer):
    """Социально бытовые условия"""
    type_room = ChoiceField(choices=SocialLivingCondition.TYPE)
    sanitary_condition = ChoiceField(choices=SocialLivingCondition.SANITARY_CONDITION)
    ownership = ChoiceField(choices=SocialLivingCondition.OWNERSHIP)
    payment = ChoiceField(choices=SocialLivingCondition.PAYMENT)

    class Meta:
        model = SocialLivingCondition
        fields = '__all__'


class SocialLivingConditionCRUDSerializers(serializers.ModelSerializer):
    """Социально бытовые условия без обозначений и вариантов полей"""

    class Meta:
        model = SocialLivingCondition
        fields = '__all__'


class SocialEconomicConditionSerializers(MyModelSerializer):
    """Социально экономические условия проживания"""
    income_level = ChoiceField(choices=SocialEconomicCondition.LEVEL)
    income_confirmation = ChoiceField(choices=SocialEconomicCondition.CONFIRMATION)
    client_security = ChoiceField(choices=SocialEconomicCondition.SECURITY)
    # Источники дохода
    salary = ChoiceField(choices=SocialEconomicCondition.SALARY)
    alimony = ChoiceField(choices=YESNO)
    material_means = ChoiceField(choices=SocialEconomicCondition.MEANS)
    rent = ChoiceField(choices=SocialEconomicCondition.RENT)
    benefits = ChoiceField(choices=YESNO)
    # Социальные выплаты
    basis_social_payments = ChoiceField(choices=SocialEconomicCondition.BASIS)
    pension = ChoiceField(choices=SocialEconomicCondition.PENSION)
    type_social_payment = ChoiceField(choices=SocialEconomicCondition.TYPE_SOCIAL_PAYMENT)
    # Детские пособия и компенсационные выплаты
    basis_payments = ChoiceField(choices=SocialEconomicCondition.BASIS)
    type_benefit_payment = ChoiceField(choices=SocialEconomicCondition.TYPE_BENEFIT_PAYMENT)
    # Льготы и меры социальной поддержки,предусмотренные для определенных категорий
    basis_facilities = ChoiceField(choices=YESNO)
    right_facilities = ChoiceField(choices=YESNO)
    stage_registration_facilities = ChoiceField(choices=SocialEconomicCondition.STAGE)

    class Meta:
        model = SocialEconomicCondition
        fields = '__all__'


class SocialEconomicConditionCRUDSerializers(serializers.ModelSerializer):
    """Социально экономические условия проживания без обозначений и вариантов полей"""

    class Meta:
        model = SocialEconomicCondition
        fields = '__all__'


class ASocialBehaviorSerializers(MyModelSerializer):
    """Информация о противоправных действиях, правонарушениях, употреблении наркотиков, алкоголя"""
    drugUse = ChoiceField(choices=YESNO)
    frequencyOfDrugsUse = ChoiceField(choices=ASocialBehavior.FREQUENCY_OF_DRUGS_USE)
    theTreatmentWasD = ChoiceField(choices=YESNO)
    psychologicalRehabilitationWasD = ChoiceField(choices=YESNO)
    alcoholUse = ChoiceField(choices=YESNO)
    frequencyOfAlcoholUse = ChoiceField(choices=ASocialBehavior.FREQUENCY_OF_DRUGS_USE)
    alcoholDrinksType = ChoiceField(choices=ASocialBehavior.ALCOHOL_DRINKS_TYPE)
    theTreatmentWasA = ChoiceField(choices=ASocialBehavior.TREATMENT_WAS_A)
    psychologicalRehabilitationWasA = ChoiceField(choices=YESNO)
    accountingInNarcologicalClinic = ChoiceField(choices=YESNO)
    criminalRecord = ChoiceField(choices=ASocialBehavior.CRIMINAL_RECORD)
    accountingInODN_RUVD = ChoiceField(choices=YES_NO_DONTKNOW)
    caseExaminedInKDN_ZP = ChoiceField(choices=YES_NO_DONTKNOW)
    commercialSexExperience = ChoiceField(choices=YESNO)
    physicalAbuseExperience = ChoiceField(choices=YESNO)
    fromHwomPhysical = ChoiceField(choices=ASocialBehavior.FROM_WHOM)
    experienceSexualAbuse = ChoiceField(choices=YESNO)
    fromHwomSexual = ChoiceField(choices=ASocialBehavior.FROM_WHOM)

    class Meta:
        model = ASocialBehavior
        fields = '__all__'


class ASocialBehaviorCRUDSerializers(serializers.ModelSerializer):
    """Информация о противоправных действиях, правонарушениях, употреблении наркотиков, алкоголя без обозначений и вариантов полей"""

    class Meta:
        model = ASocialBehavior
        fields = '__all__'


class ChronicDiseaseSerializers(MyModelSerializer):
    """Информация о наличии хронического заболевания"""

    hepatitisC = ChoiceField(choices=ChronicDisease.DISEASE)
    HIVStatus = ChoiceField(choices=ChronicDisease.DISEASE)
    estimatedRouteOfInfection = ChoiceField(choices=ChronicDisease.TYPE_INVASION)
    AIDSCenter = ChoiceField(choices=YESNO)
    doesCenterVisitAIDS = ChoiceField(choices=ChronicDisease.VISIT_AIDS)
    receivedChemoprophylaxis = ChoiceField(choices=YESNO)
    HIVGetTreatment = ChoiceField(choices=ChronicDisease.HIV_TREATMENT)
    whoKnow = ChoiceField(choices=ChronicDisease.HIV_FAMILY_AWARENESS)

    class Meta:
        model = ChronicDisease
        fields = '__all__'


class ChronicDiseaseCRUDSerializers(serializers.ModelSerializer):
    """Информация о наличии хронического заболевания без обозначений и вариантов полей"""

    class Meta:
        model = ChronicDisease
        fields = '__all__'


class FamilyMembersInformationSerializers(MyModelSerializer):
    """Сведения о членах семьи"""
    maritalStatus = ChoiceField(choices=FamilyMembersInformation.MARITAL_STATUS)
    withWhomLiving = ChoiceField(choices=FamilyMembersInformation.LIVING_WITH_WHOM)

    class Meta:
        model = FamilyMembersInformation
        fields = '__all__'


class FamilyMembersInformationCRUDSerializers(serializers.ModelSerializer):
    """Сведения о членах семьи без обозначений и вариантов полей"""

    class Meta:
        model = FamilyMembersInformation
        fields = '__all__'


class HusbandListSerializers(serializers.ModelSerializer):
    """Список мужей/партнеров"""

    class Meta:
        model = HusbandInformation
        fields = ('fullName', 'age')


class HusbandInformationSerializers(MyModelSerializer):
    """Информация о муже/партнёре"""
    placementSocialSupport = ChoiceField(choices=HusbandInformation.PLACEMENT_SOCIAL_SUPPORT)
    registrationMunicipalDistrict = ChoiceField(choices=HusbandInformation.MUNICIPAL_DISTRICT)
    actualMunicipalDistrict = ChoiceField(choices=HusbandInformation.MUNICIPAL_DISTRICT)
    workPlace = ChoiceField(choices=HusbandInformation.WORK_PLACE)
    avDoc = ChoiceField(choices=YESNO)
    cityzenship = ChoiceField(choices=HusbandInformation.CITYZENSHIP)
    registration = ChoiceField(choices=HusbandInformation.REGISTRATION)
    placeOfRegistration = ChoiceField(choices=HusbandInformation.PLACE_OF_REGISTRATION)
    education = ChoiceField(choices=HusbandInformation.EDUCATION)
    categoryFamilies = ChoiceField(choices=HusbandInformation.CATEGORY_FAMILIES)
    disability = ChoiceField(choices=YESNO)
    drugUse = ChoiceField(choices=YESNO)
    frequencyOfDrugsUse = ChoiceField(choices=HusbandInformation.FREQUENCY_OF_DRUGS_USE)
    theTreatmentWasD = ChoiceField(choices=YESNO)
    psychologicalRehabilitationWasD = ChoiceField(choices=YESNO)
    alcoholUse = ChoiceField(choices=YESNO)
    frequencyOfAlcoholUse = ChoiceField(choices=HusbandInformation.FREQUENCY_OF_DRUGS_USE)
    alcoholDrinksType = ChoiceField(choices=HusbandInformation.ALCOHOL_DRINKS_TYPE)
    theTreatmentWasA = ChoiceField(choices=HusbandInformation.THE_TREATMENT_WAS_A)
    psychologicalRehabilitationWasA = ChoiceField(choices=YESNO)
    accountingInNarcologicalClinic = ChoiceField(choices=YESNO)
    criminalRecord = ChoiceField(choices=YESNO)

    class Meta:
        model = HusbandInformation
        fields = '__all__'


class HusbandInformationCRUDSerializers(serializers.ModelSerializer):
    """Информация о муже/партнёре без обозначений и вариантов полей"""

    class Meta:
        model = HusbandInformation
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    """Специалист"""

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "patronymic", "position", "email")


class ExpertOpinionSerializers(MyModelSerializer):
    """Заключение специалиста"""

    class Meta:
        model = ExpertOpinion
        fields = '__all__'


class ExpertOpinionCRUDSerializers(serializers.ModelSerializer):
    """Заключение специалиста без обозначений и вариантов полей"""

    class Meta:
        model = ExpertOpinion
        fields = ('client', 'otherInformation', 'expectations', 'personaImpressions')


class TestBoykoListSerializers(serializers.ModelSerializer):
    """Список тестов Бойко"""

    class Meta:
        model = TestBoyko
        fields = ('id', 'attempt')


class TestBoykoSerializers(MyModelSerializer):
    """Тест Бойко"""
    aggressiveness = ChoiceField(choices=TestBoyko.AGGRESS)
    alarm = ChoiceField(choices=TestBoyko.ALARM)
    memory_disorder = ChoiceField(choices=TestBoyko.MEMORY_DISORDER)
    criticism = ChoiceField(choices=TestBoyko.CRITICISM)
    self_service = ChoiceField(choices=TestBoyko.SELF_SERVICE)
    work_activity = ChoiceField(choices=TestBoyko.WORK_ACTIVITY)
    friends = ChoiceField(choices=TestBoyko.FRIENDS)
    family_relation = ChoiceField(choices=TestBoyko.FAMILY_RELATION)
    child_parent = ChoiceField(choices=TestBoyko.CHILD_PARENT)
    leisure = ChoiceField(choices=TestBoyko.LEISURE)
    attempt = ChoiceField(choices=ATTEMPT)

    class Meta:
        model = TestBoyko
        fields = '__all__'


class TestBoykoCRUDSerializers(serializers.ModelSerializer):
    """Тест Бойко без обозначений и вариантов полей"""

    class Meta:
        model = TestBoyko
        fields = '__all__'


class InterpretationBoykoSerializers(MyModelSerializer):
    """Интерпретация теста Бойко"""
    aggressiveness = ChoiceField(choices=InterpretationBoyko.AGGRESS)
    alarm = ChoiceField(choices=InterpretationBoyko.ALARM)
    memory_disorder = ChoiceField(choices=InterpretationBoyko.MEMORY_DISORDER)
    criticism = ChoiceField(choices=InterpretationBoyko.CRITICISM)
    self_service = ChoiceField(choices=InterpretationBoyko.SELF_SERVICE)
    work_activity = ChoiceField(choices=InterpretationBoyko.WORK_ACTIVITY)
    friends = ChoiceField(choices=InterpretationBoyko.FRIENDS)
    family_relation = ChoiceField(choices=InterpretationBoyko.FAMILY_RELATION)
    child_parent = ChoiceField(choices=InterpretationBoyko.CHILD_PARENT)
    leisure = ChoiceField(choices=InterpretationBoyko.LEISURE)
    overall_assessment = ChoiceField(choices=InterpretationBoyko.OVERALL_ASSESSMENT)

    class Meta:
        model = InterpretationBoyko
        fields = '__all__'


class InterpretationBoykoCRUDSerializers(serializers.ModelSerializer):
    """Интерпретация теста Бойко без обозначений и вариантов полей"""

    class Meta:
        model = InterpretationBoyko
        fields = '__all__'


class TestGAGEListSerializers(serializers.ModelSerializer):
    """Список тестов GAGE"""

    class Meta:
        model = TestGAGE
        fields = ('id', 'attempt')


class TestGAGESerializers(MyModelSerializer):
    """Тест GAGE"""
    alcohol = ChoiceField(choices=GAGE_YESNO)
    substances = ChoiceField(choices=TestGAGE.SUBSTANCES)
    loss_documents = ChoiceField(choices=GAGE_YESNO)
    loss_documents_when = ChoiceField(choices=TestGAGE.LOSS_DOCUMENTS_WHEN)
    loss_documents_time = ChoiceField(choices=TestGAGE.LOSS_DOCUMENTS_TIME)
    do_not_work = ChoiceField(choices=GAGE_YESNO)
    do_not_work_when = ChoiceField(choices=TestGAGE.DO_NOT_WORK_WHEN)
    loss_loved_ones = ChoiceField(choices=GAGE_YESNO)
    fight = ChoiceField(choices=GAGE_YESNO)
    injuries = ChoiceField(choices=TestGAGE.INJURIES)
    lots_alcohol = ChoiceField(choices=GAGE_YESNO)
    lots_alcohol_time = ChoiceField(choices=TestGAGE.LOTS_ALCOHOL_TIME)
    drink_alcohol_time = ChoiceField(choices=TestGAGE.DRINK_ALCOHOL_TIME)
    try_substances_choice = ChoiceField(choices=TestGAGE.TRY_SUBSTANCES)
    how_use = ChoiceField(choices=TestGAGE.HOW_USE)
    difficulties = ChoiceField(choices=GAGE_YESNO)
    poor_health = ChoiceField(choices=TestGAGE.POOR_HEALTH)
    company = ChoiceField(choices=TestGAGE.COMPANY)
    dose_reduction = ChoiceField(choices=GAGE_YESNO)
    irritation = ChoiceField(choices=GAGE_YESNO)
    fault = ChoiceField(choices=GAGE_YESNO)
    tone = ChoiceField(choices=GAGE_YESNO)
    attempt = ChoiceField(choices=ATTEMPT)

    class Meta:
        model = TestGAGE
        fields = '__all__'


class TestGAGECRUDSerializers(serializers.ModelSerializer):
    """Тест GAGE без обозначений и вариантов полей"""

    class Meta:
        model = TestGAGE
        fields = '__all__'


class InterpretationGAGESerializers(MyModelSerializer):
    """Интерпретация теста GAGE"""
    risk_abuse = ChoiceField(choices=InterpretationGAGE.RISK_ABUSE)
    risk_dependency = ChoiceField(choices=InterpretationGAGE.RISK_DEPENDENCY)

    class Meta:
        model = InterpretationGAGE
        fields = '__all__'


class InterpretationGAGECRUDSerializers(serializers.ModelSerializer):
    """Интерпретация теста GAGE без обозначений и вариантов полей"""

    class Meta:
        model = InterpretationGAGE
        fields = '__all__'


class TestSOCRATESListSerializers(serializers.ModelSerializer):
    """Список тестов SOCRATES"""

    class Meta:
        model = TestSOCRATES
        fields = ('id', 'attempt')


class TestSOCRATESSerializers(MyModelSerializer):
    """Тест SOCRATES"""
    changes = ChoiceField(choices=TestSOCRATES.FORM)
    doubt = ChoiceField(choices=TestSOCRATES.FORM)
    aggravation = ChoiceField(choices=TestSOCRATES.FORM)
    make_changes = ChoiceField(choices=TestSOCRATES.FORM)
    too_much = ChoiceField(choices=TestSOCRATES.FORM)
    harm = ChoiceField(choices=TestSOCRATES.FORM)
    serious_problem = ChoiceField(choices=TestSOCRATES.FORM)
    changes_lifestyle = ChoiceField(choices=TestSOCRATES.FORM)
    hold = ChoiceField(choices=TestSOCRATES.FORM)
    know_trouble = ChoiceField(choices=TestSOCRATES.FORM)
    control = ChoiceField(choices=TestSOCRATES.FORM)
    much_harm = ChoiceField(choices=TestSOCRATES.FORM)
    reduce_stop = ChoiceField(choices=TestSOCRATES.FORM)
    help = ChoiceField(choices=TestSOCRATES.FORM)
    have_problem = ChoiceField(choices=TestSOCRATES.FORM)
    use_lot = ChoiceField(choices=TestSOCRATES.FORM)
    alcoholic = ChoiceField(choices=TestSOCRATES.FORM)
    try_my_best = ChoiceField(choices=TestSOCRATES.FORM)
    move_on = ChoiceField(choices=TestSOCRATES.FORM)
    attempt = ChoiceField(choices=ATTEMPT)

    class Meta:
        model = TestSOCRATES
        fields = '__all__'


class TestSOCRATESCRUDSerializers(serializers.ModelSerializer):
    """Тест SOCRATES без обозначений и вариантов полей"""

    class Meta:
        model = TestSOCRATES
        fields = '__all__'


class InterpretationSOCRATESSerializers(MyModelSerializer):
    """Интерпретация тестов SOCRATES"""
    realization = ChoiceField(choices=InterpretationSOCRATES.REALIZATION)
    ambivalence = ChoiceField(choices=InterpretationSOCRATES.AMBIVALENCE)
    action = ChoiceField(choices=InterpretationSOCRATES.ACTION)
    ready_change = ChoiceField(choices=InterpretationSOCRATES.READY_CHANGE)

    class Meta:
        model = InterpretationSOCRATES
        fields = '__all__'


class InterpretationSOCRATESCRUDSerializers(serializers.ModelSerializer):
    """Интерпретация тестов SOCRATES без обозначений и вариантов полей"""

    class Meta:
        model = InterpretationSOCRATES
        fields = '__all__'


class TypologicalGroupListSerializers(serializers.ModelSerializer):
    """Список типологических групп"""
    test = TestBoykoListSerializers()

    class Meta:
        model = TypologicalGroup
        fields = ('id', 'test')


class TypologicalGroupSerializers(MyModelSerializer):
    """Типологическая группа"""
    group = ChoiceField(choices=TypologicalGroup.GROUP)

    class Meta:
        model = TypologicalGroup
        fields = '__all__'


class TypologicalGroupCRUDSerializers(serializers.ModelSerializer):
    """Типологическая группа без обозначений и вариантов полей"""

    class Meta:
        model = TypologicalGroup
        fields = '__all__'


class GroupASocialBehaviorSerializers(serializers.ModelSerializer):
    """Поля Информации о противоправных действиях для определения типологической группы"""

    class Meta:
        model = ASocialBehavior
        fields = ('id', 'caseExaminedInKDN_ZP')


class GroupTestBoykoSerializers(serializers.ModelSerializer):
    """Поля Теста Бойко для определения типологической группы"""

    class Meta:
        model = TestBoyko
        fields = ('id', 'aggressiveness')


class GroupClientSerializers(serializers.ModelSerializer):
    """Поля Общей информации о клиенте для определения типологической группы"""

    class Meta:
        model = Client
        fields = ('id', 'age')


class GroupChronicDiseaseSerializers(serializers.ModelSerializer):
    """Поля Информации о наличии хронического заболевания для определения типологической группы"""

    class Meta:
        model = ChronicDisease
        fields = ('id', 'hepatitisC', 'HIVStatus')


class FamilyMemberSpecial(serializers.ModelSerializer):
    """Определенные поля для Общих сведений о членах семьи"""

    class Meta:
        model = FamilyMembersInformation
        fields = ('id', 'client')
        # fields = '__all__'


class ExpertForTable(serializers.ModelSerializer):
    """Имя и фамилия специалиста для отображения в общей таблице"""

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")
