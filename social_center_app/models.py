from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

YESNO = [(1, 'да'), (2, 'нет')]
YES_NO_DONTKNOW = [(1, 'да'), (2, 'нет'), (3, 'не знаю')]


class Client(models.Model):
    """
    Социальная диагностика
    ======================

    1. Сведения о клиенте
    ---------------------

    1.1. Общая информация
    """
    FORM_OF_REFERRAL = [
        (1, 'самообращение'),
        (2, 'КДН и ЗП'),
        (3, 'органы опеки и попечительства'),
        (4, 'образовательные учреждения'),
        (5, 'дом ребёнка'),
        (6, 'родильный дом'),
        (7, 'женская консультация'),
        (8, 'детская поликлиника'),
        (9, 'центр СПИД'),
        (10, 'отдел полиции'),
        (11, 'УФСИН'),
        (12, 'перевод'),
        (13, 'СО НКО')
    ]

    MUNICIPAL_DISTRICT = [
        (1, 'Юго-Запад'),
        (2, 'Южно-Приморский'),
        (3, 'Сосновая Поляна'),
        (4, 'Урицк'),
        (5, 'Константиновское'),
        (6, 'Горелово'),
        (7, 'г.Красное Село')
    ]

    DEPENDENCE = [
        (1, 'алкогольная'),
        (2, 'наркотическая'),
        (3, 'опыт употребления'),
        (4, 'созависимость')
    ]
    STATE_OF_DEPENDENCE = [
        (1, 'активное потребление'),
        (2, 'ремиссия')
    ]

    SEX = [(1, "мужской"), (2, "женский")]

    WORK_PLACE = [(1, "постоянное"),
                  (2, "временное"),
                  (3, "эпизодическое"),
                  (4, "не работает"),
                  (5, "состоит в центре занятости населения в качестве безработного")]

    CITYZENSHIP = [(1, "Россия"),
                   (2, "страна СНГ")]

    REGISTRATION = [(1, "постоянная"),
                    (2, "временная")]

    PLACE_OF_REGISTRATION = [(1, "Санкт-Петербург"),
                             (2, "Ленинградская область"),
                             (3, "другой регион РФ"),
                             (4, "страна СНГ")]

    EDUCATION = [(1, "высшее"),
                 (2, "неоконченное высшее"),
                 (3, "среднее специальное"),
                 (4, "начальное профессиональное"),
                 (5, "обучается"),
                 (6, "полное среднее (11 классов)"),
                 (7, "общее среднее (9 классов)"),
                 (8, "неоконченное общее среднее"),
                 (9, "начальная школа")]

    FAMILIES_CATEGORY = [
        (1, 'полная семья'),
        (2, 'одинокий родитель'),
        (3, 'многодетная семья'),
        (4, 'разведённые'),
        (5, 'беженцы / переселенцы'),
        (6, 'несовершеннолетние родители'),
        (7, 'замещающая семья'),
        (8, 'семья с инвалидом'),
        (9, 'другое')
    ]

    ESCORT = [
        (1, "интенсивное"),
        (2, "поддерживающее"),
        (3, "мониторинг")
    ]

    PLACEMENT_SOCIAL_SUPPORT = [
        (1, "консилиум"),
        (2, "приказ")
    ]

    dateOfInterview = models.DateField("Дата проведения интервью", null=True, blank=True)
    code = models.TextField(verbose_name='Код клиента', null=True, blank=True)
    formOfReferral = models.IntegerField("Форма обращения", choices=FORM_OF_REFERRAL, null=True, blank=True)
    placementSocialSupport = models.IntegerField("Постановка на социальное сопровождение",
                                                 choices=PLACEMENT_SOCIAL_SUPPORT, null=True, blank=True)
    DateOfCreationIPSO = models.DateField("Дата разработки ИППСУ", null=True, blank=True)
    IPPSNumber = models.TextField(verbose_name='Номер ИППСУ', null=True, blank=True)
    ContractPeriod = models.DateField("Срок действия договора", null=True, blank=True)
    contractNumber = models.TextField(verbose_name='Номер договора', null=True, blank=True)
    full_name = models.TextField(verbose_name='ФИО клиента', null=True, blank=True)
    sex = models.IntegerField("Пол",
                              choices=SEX, null=True, blank=True)
    dod = models.DateField("Дата рождения", null=True, blank=True)
    age = models.IntegerField("Возраст", null=True, blank=True)
    passSeries = models.IntegerField("Серия паспорта", null=True, blank=True)
    passNumber = models.IntegerField("Номер паспорта", null=True, blank=True)
    passFromWhomIssue = models.TextField(verbose_name='Выдан', null=True, blank=True)
    passDateIssue = models.DateField("Дата выдачи", null=True, blank=True)
    registrationAddressCity = models.TextField(verbose_name='Населенный пункт (АР)', null=True, blank=True)
    registrationAddressStreet = models.TextField(verbose_name='Улица (АР)', null=True, blank=True)
    registrationAddressHouseNum = models.TextField(verbose_name='Дом (АР)', null=True, blank=True)
    registrationAddressApNum = models.TextField(verbose_name='Номер квартиры (АР)', null=True, blank=True)
    registrationAddressIndex = models.IntegerField("Почтовый индекс (АР)", null=True, blank=True)
    registrationMunicipalDistrict = models.IntegerField("Муниципальный округ (АР)",
                                                        choices=MUNICIPAL_DISTRICT, null=True, blank=True)
    actualAddressCity = models.TextField(verbose_name='Населенный пункт (АФП)', null=True, blank=True)
    actualAddressStreet = models.TextField(verbose_name='Улица (АФП)', null=True, blank=True)
    actualAddressHouseNum = models.TextField(verbose_name='Дом (АФП)', null=True, blank=True)
    actualAddressApNum = models.TextField(verbose_name='Номер квартиры (АФП)', null=True, blank=True)
    actualAddressIndex = models.IntegerField("Почтовый индекс (АФП)", null=True, blank=True)
    actualMunicipalDistrict = models.IntegerField("Муниципальный округ (АФП)",
                                                  choices=MUNICIPAL_DISTRICT, null=True, blank=True)
    phoneNumber = models.TextField(verbose_name='Номер телефона', max_length=15, null=True, blank=True)
    dependence = models.IntegerField("Зависимость",
                                     choices=DEPENDENCE, null=True, blank=True)
    stateOfDependence = models.IntegerField("Состояние зависимости",
                                            choices=STATE_OF_DEPENDENCE, null=True, blank=True)
    adultsCount = models.IntegerField("Кол-во взрослых", null=True, blank=True,
                                      validators=[
                                          MinValueValidator(0)
                                      ])
    minorsCount = models.IntegerField("Кол-во несовершеннолетних", null=True, blank=True,
                                      validators=[
                                          MinValueValidator(0)
                                      ])
    workPlace = models.IntegerField("Место работы",
                                    choices=WORK_PLACE, null=True, blank=True)
    aboutWork = models.TextField("Где, кем работает (при наличии работы)",
                                 null=True,
                                 blank=True)
    aboutNoWork = models.TextField("Причина, по которой не работает",
                                   null=True,
                                   blank=True)
    avDoc = models.IntegerField("Наличие документов",
                                choices=YESNO, null=True, blank=True)
    cityzenship = models.IntegerField("Гражданство",
                                      choices=CITYZENSHIP, null=True, blank=True)
    registration = models.IntegerField("Регистрация",
                                       choices=REGISTRATION, null=True, blank=True)
    placeOfRegistration = models.IntegerField("Место регистрации",
                                              choices=PLACE_OF_REGISTRATION, null=True, blank=True)
    education = models.IntegerField("Образование",
                                    choices=EDUCATION, null=True, blank=True)
    familiesCategory = models.IntegerField("Категория семей",
                                           choices=FAMILIES_CATEGORY, null=True, blank=True)
    disability = models.IntegerField("Инвалидность",
                                     choices=YESNO, null=True,
                                     blank=True)
    escort = models.IntegerField("Какое сопровождение", choices=ESCORT, null=True, blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Child(models.Model):
    """
    Социальная диагностика
    ======================

    2. Сведения о детях
    -------------------

    2.1 Общая информация
    2.2 Информация о состоянии здоровья ребёнка
    """
    SEX = [(1, 'мужской'), (2, 'женский')]
    STATUS = [(1, 'родной'), (2, 'усыновлен'), (3, 'оформлена опека'),
              (4, 'оставшийся без попечения родителей/лишение родительских прав'), (5, 'сирота'), (6, 'инвалидность')]
    LOCATION = [(1, 'в семье'), (2, 'больница'), (3, 'социальное учреждение')]
    EDUCATE = [(1, 'да'), (2, 'нет'), (3, 'подписала временный отказ'), (4, 'подписала полный отказ'),
               (5, 'ушла из родильного дома'), (6, 'собирается подписывать временный отказ'),
               (7, 'собирается подписывать полный отказ')]
    REASON = [(1, 'отсутствие жилья'), (2, 'употребление наркотиков'), (3, 'низкая материальная обеспеченность'),
              (4, 'физическое или психическое заболевание'), (5, 'отсутствие семейной поддержки'),
              (6, 'нежелательная беременность')]

    DEPENDENCE = [
        (1, 'алкогольная'),
        (2, 'наркотическая'),
        (3, 'опыт употребления'),
        (4, 'созависимость')
    ]

    PLACEMENT_SOCIAL_SUPPORT = [
        (1, "консилиум"),
        (2, "приказ")
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    placementSocialSupport = models.IntegerField("Постановка на социальное сопровождение",
                                                 choices=PLACEMENT_SOCIAL_SUPPORT, null=True, blank=True)
    DateOfCreationIPSO = models.DateField("Дата разработки ИППСУ", null=True, blank=True)
    IPPSNumber = models.TextField(verbose_name='Номер ИППСУ', null=True, blank=True)
    ContractPeriod = models.DateField("Срок действия договора", null=True, blank=True)
    contractNumber = models.TextField(verbose_name='Номер договора', null=True, blank=True)

    full_name = models.TextField(verbose_name='ФИО', null=True, blank=True)
    sex = models.IntegerField(verbose_name='Пол', choices=SEX, null=True, blank=True)
    birthdate = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    age = models.IntegerField(verbose_name='Возраст', null=True, blank=True)
    status = models.IntegerField(verbose_name='Статус ребенка', choices=STATUS, null=True, blank=True)
    location = models.IntegerField(verbose_name='Место нахождения ребенка', choices=LOCATION, null=True, blank=True)
    documents = models.IntegerField(verbose_name='Наличие документов у ребенка', choices=YESNO, null=True, blank=True)
    fatherhood = models.IntegerField(verbose_name='Установлено ли отцовство на ребенка', choices=YESNO, null=True,
                                     blank=True)
    education = models.IntegerField(verbose_name='Посещает ли образовательное учреждение', choices=YESNO, null=True,
                                    blank=True)
    educational_institution = models.TextField(verbose_name='Какое образовательное учреждение', null=True, blank=True)
    educate_child = models.IntegerField(verbose_name='Планирует ли воспитывать ребенка', choices=EDUCATE, null=True,
                                        blank=True)
    reason_refusal = models.IntegerField(verbose_name='Возможные причины отказа', choices=REASON, null=True, blank=True)

    HIV = [(1, 'ВИЧ-положительный'), (2, 'ВИЧ-отрицательный'), (3, 'не установлен')]
    HIV_PREVENTION = [(1, 'во время родов'), (2, 'после родов'), (3, 'не знает')]

    health = models.IntegerField(verbose_name='Ребенок родился здоровым', choices=YESNO, null=True, blank=True)
    withdrawal_symptoms = models.IntegerField(verbose_name='В абстинентном синдроме', choices=YES_NO_DONTKNOW,
                                              null=True,
                                              blank=True)
    with_mother = models.IntegerField(verbose_name='Ребенок выписан из родильного отделения вместе с матерью',
                                      choices=YES_NO_DONTKNOW, null=True, blank=True)
    hiv_status_child = models.IntegerField(verbose_name='ВИЧ-статус ребенка', choices=HIV, null=True, blank=True)
    hiv_plus = models.IntegerField(verbose_name='Родился после установления ВИЧ-положительного статуса клиента',
                                   choices=YESNO, null=True, blank=True)
    center_aids = models.IntegerField(verbose_name='Учет в центре СПИД', choices=YESNO, null=True, blank=True)
    hiv_prevention = models.IntegerField(verbose_name='Получал ли профилактику ВИЧ', choices=YES_NO_DONTKNOW, null=True,
                                         blank=True)
    dependence = models.IntegerField("Зависимость", choices=DEPENDENCE, null=True, blank=True)

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'


class SocialLivingCondition(models.Model):
    """
    Социальная диагностика
    ======================

    4. Сведения о социально-бытовом и социально-экономическом положении
    -------------------------------------------------------------------

    4.1 Социально-бытовые условия
    """
    TYPE = [(1, 'жилой дом'), (2, 'отдельная квартира'), (3, 'комната в коммунальной квартире'),
            (4, 'комната в общежитии'), (5, 'отсутствует')]
    SANITARY_CONDITION = [(1, 'хорошее'), (2, 'удовлетворительное'), (3, 'антисанитарное'),
                          (4, 'признаки аварийности жилого помещения')]
    OWNERSHIP = [(1, 'договор по найму жилья'), (2, 'собственность клиента'), (3, 'собственность родственников')]
    PAYMENT = [(1, 'своевременно в полном объеме'), (2, 'незначительная задолженность'),
               (3, 'значительная задолженность')]
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    type_room = models.IntegerField(verbose_name='Вид жилого помещения', choices=TYPE, null=True,
                                    blank=True)
    sanitary_condition = models.IntegerField(
        verbose_name='Санитарно-гигиеническое и техническое состояние жилого помещения', choices=SANITARY_CONDITION,
        null=True, blank=True)
    room_area = models.FloatField(verbose_name='Жилая площадь (кв.м.)', null=True,
                                  blank=True)
    ownership = models.IntegerField(verbose_name='Право собственности,владения и пользования', choices=OWNERSHIP,
                                    null=True, blank=True)
    payment = models.IntegerField(verbose_name='Оплата за жилье и коммунальные услуги', choices=PAYMENT, null=True,
                                  blank=True)

    class Meta:
        verbose_name = 'Социально бытовые условия'
        verbose_name_plural = 'Социально бытовые условия'


class SocialEconomicCondition(models.Model):
    """
    Социальная диагностика
    ======================

    4. Сведения о социально-бытовом и социально-экономическом положении
    -------------------------------------------------------------------

    4.2 Социально-экономические условия проживания
    """
    LEVEL = [(1, 'высокий уровень'), (2, 'около двух прожиточных минимумов на человека'),
             (3, 'на уровне прожиточного минимума'), (4, 'ниже прожиточного минимума'), (5, 'нет дохода')]
    CONFIRMATION = [(1, 'возможно подтвердить документально'), (2, 'необходим сбор документов'),
                    (3, 'невозможно подтвердить документально')]
    SECURITY = [(1, 'достаточное с учетом возраста и потребностей ребенка'), (2, 'удовлетворительное'),
                (3, 'недостаточное')]
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    income_level = models.IntegerField(verbose_name='Уровень доходов клиента', choices=LEVEL, null=True,
                                       blank=True)
    income_confirmation = models.IntegerField(
        verbose_name='Возможность подтверждения дохода ниже прожиточного минимума', choices=CONFIRMATION, null=True,
        blank=True)
    client_security = models.IntegerField(
        verbose_name='Обеспеченность клиентки и ее детей полноценным питанием,одеждой,обувью,предметами личной гигиены',
        choices=SECURITY, null=True, blank=True)

    class Meta:
        verbose_name = 'Социально экономические условия проживания'
        verbose_name_plural = 'Социально экономические условия проживания'


class SourceIncome(models.Model):
    """
    Социальная диагностика
    ======================

    4. Сведения о социально-бытовом и социально-экономическом положении
    -------------------------------------------------------------------

    4.2 Социально-экономические условия проживания
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Источники дохода
    """
    SALARY = [(1, 'постоянно'), (2, 'переодически'), (3, 'редко')]
    MEANS = [(1, 'родственниками'), (2, 'партнером'), (3, 'мужем')]
    RENT = [(1, 'комнаты'), (2, 'оборудования'), (3, 'участка')]
    economic_condition = models.OneToOneField(SocialEconomicCondition, on_delete=models.CASCADE)
    salary = models.IntegerField(verbose_name='Заработная плата', choices=SALARY, null=True, blank=True)
    alimony = models.IntegerField(verbose_name='Алименты/нотариальное соглашение о содержании ребенка', choices=YESNO,
                                  null=True, blank=True)
    material_means = models.IntegerField(verbose_name='Предоставление материальных средств', choices=MEANS, null=True,
                                         blank=True)
    rent = models.IntegerField(verbose_name='Сдача в аренду', choices=RENT, null=True, blank=True)
    benefits = models.IntegerField(verbose_name='Льготы по коммунальным услугам', choices=YESNO, null=True, blank=True)

    class Meta:
        verbose_name = 'Источники дохода'
        verbose_name_plural = 'Источники дохода'


BASIS = [(1, 'нет оснований для оформления выплаты'), (2, 'имеется право на выплату'), (3, 'требует оформления'),
         (4, 'находится в стадии оформления'), (5, 'выплачивается')]


class SocialPayment(models.Model):
    """
    Социальная диагностика
    ======================

    4. Сведения о социально-бытовом и социально-экономическом положении
    -------------------------------------------------------------------

    4.2 Социально-экономические условия проживания
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Социальные выплаты
    """
    PENSION = [(1, 'по старости'), (2, 'по потере кормильца'), (3, 'по инвалидности')]
    TYPE_SOCIAL_PAYMENT = [(1, 'единовременные выплаты'), (2, 'ежемесячные выплаты'),
                           (3, 'государственная социальная помощь,доплата до прожиточного минимума'),
                           (4, 'государственная социальная помощь в трудной жизненной ситуации')]
    economic_condition = models.OneToOneField(SocialEconomicCondition, on_delete=models.CASCADE)
    basis_social_payments = models.IntegerField(verbose_name='Основания для социальных выплат', choices=BASIS,
                                                null=True, blank=True)
    pension = models.IntegerField(verbose_name='Пенсия', choices=PENSION, null=True, blank=True)
    type_social_payment = models.IntegerField(verbose_name='Вид социальной выплаты', choices=TYPE_SOCIAL_PAYMENT,
                                              null=True, blank=True)

    class Meta:
        verbose_name = 'Социальные выплаты'
        verbose_name_plural = 'Социальные выплаты'


class ChildAllowanceAndCompensation(models.Model):
    """
    Социальная диагностика
    ======================

    4. Сведения о социально-бытовом и социально-экономическом положении
    -------------------------------------------------------------------

    4.2 Социально-экономические условия проживания
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Детские пособия и компенсационные выплаты
    """
    TYPE_BENEFIT_PAYMENT = [(1, 'единовременная компенсационная выплата при рождении ребенка (СПБ)'),
                            (2, 'единовременное пособие при рождении ребенка (РФ)'),
                            (3, 'ежемесячное пособие на ребёнка в возрасте от рождения до 1 года (СПб)'),
                            (4, 'ежемесячное пособие на ребёнка в возрасте от 1 года до 7 лет (СПб)'),
                            (5, 'ежемесячное пособие на детей школьного возраста (СПб)'),
                            (6, 'пособие по беременности и родам (РФ)'),
                            (7, 'единовременное пособие женщинам, вставшим на учёт в ранние сроки (РФ)'),
                            (8, 'ежемесячное пособие по уходу за ребёнком (РФ)'),
                            (9, 'сертификат на получение материнского (семейного) капитала')]
    economic_condition = models.OneToOneField(SocialEconomicCondition, on_delete=models.CASCADE)
    basis_payments = models.IntegerField(verbose_name='Основания для выплаты', choices=BASIS, null=True, blank=True)
    type_benefit_payment = models.IntegerField(verbose_name='Вид пособия/компенсационной выплаты',
                                               choices=TYPE_BENEFIT_PAYMENT, null=True, blank=True)

    class Meta:
        verbose_name = 'Детские пособия и компенсационные выплаты'
        verbose_name_plural = 'Детские пособия и компенсационные выплаты'


class Facilities(models.Model):
    """
    Социальная диагностика
    ======================

    4. Сведения о социально-бытовом и социально-экономическом положении
    -------------------------------------------------------------------

    4.2 Социально-экономические условия проживания
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Льготы и меры социальной поддержки, предусмотренные для определённых категорий
    """
    STAGE = [(1, 'оформлено полностью'), (2, 'частично оформлено'), (3, 'в стадии оформления'), (4, 'не оформлено')]
    economic_condition = models.OneToOneField(SocialEconomicCondition, on_delete=models.CASCADE)
    basis_facilities = models.IntegerField(verbose_name='Основания для льгот', choices=YESNO, null=True, blank=True)
    right_facilities = models.IntegerField(verbose_name='Имеет право на льготы (указать)', choices=YESNO, null=True,
                                           blank=True)
    stage_registration_facilities = models.IntegerField(verbose_name='Стадия оформления льгот', choices=STAGE,
                                                        null=True, blank=True)
    reason = models.TextField(verbose_name='Причина,по которой не оформлены льготы', null=True, blank=True)

    class Meta:
        verbose_name = 'Льготы и меры социальной поддержки,предусмотренные для определенных категорий'
        verbose_name_plural = 'Льготы и меры социальной поддержки,предусмотренные для определенных категорий'


class ASocialBehavior(models.Model):
    """
    Социальная диагностика
    ======================

    1. Сведения о клиенте
    ---------------------

    1.2 Информация о противоправных действиях, правонарушениях, употреблении наркотиков, алкоголя
    """
    FREQUENCY_OF_DRUGS_USE = [(1, "ежедневно"),
                              (2, "раз в два-три дня"),
                              (3, "раз в неделю"),
                              (4, "раз в месяц"),
                              (5, "реже одного раза в месяц")]
    ALCOHOL_DRINKS_TYPE = [(1, "слабоалкогольные"),
                           (2, "сильноалкогольные")]

    FROM_WHOM = [(1, 'муж/партнёр'),
                 (2, 'другого родственника')]

    TREATMENT_WAS_A = [
        (1, 'да'),
        (2, 'нет'),
        (3, 'химическая защита')
    ]

    CRIMINAL_RECORD = [
        (1, 'условная'),
        (2, 'отсрочка приговора'),
        (3, 'из мест лишения свободы'),
        (4, 'под следствием'),
        (5, 'нет'),
    ]

    client = models.OneToOneField(Client, on_delete=models.CASCADE)

    drugUse = models.IntegerField("Употребление наркотиков",
                                  choices=YESNO, null=True, blank=True)
    frequencyOfDrugsUse = models.IntegerField("Частота употребления наркотиков",
                                              choices=FREQUENCY_OF_DRUGS_USE,
                                              null=True,
                                              blank=True)
    durationOfUse = models.DecimalField("Длительность употребления (в годах)",
                                        max_digits=3,
                                        decimal_places=1,
                                        null=True,
                                        blank=True)
    kindOfDrug = models.TextField("Вид наркотика",
                                  null=True,
                                  blank=True)
    theTreatmentWasD = models.IntegerField("Проходил ли лечение(наркотики)",
                                           choices=YESNO,
                                           null=True,
                                           blank=True)
    psychologicalRehabilitationWasD = models.IntegerField("Проходил ли психологическую реабилитацию(наркотики)",
                                                          choices=YESNO,
                                                          null=True,
                                                          blank=True)
    wherePsyRehWasD = models.TextField("Где проходил реабилитацию(наркотики)?",
                                       null=True,
                                       blank=True)
    durationOfRemissionD = models.DecimalField("Длительность ремиссии (в годах)(наркотики)",
                                               max_digits=3,
                                               decimal_places=1,
                                               null=True,
                                               blank=True)
    alcoholUse = models.IntegerField("Употребление алкоголя",
                                     choices=YESNO, null=True, blank=True)
    frequencyOfAlcoholUse = models.IntegerField("Частота употребления алкоголя",
                                                choices=FREQUENCY_OF_DRUGS_USE,
                                                null=True,
                                                blank=True)
    alcoholDrinksType = models.IntegerField("Вид алкогольных напитков",
                                            choices=ALCOHOL_DRINKS_TYPE,
                                            null=True,
                                            blank=True)
    theTreatmentWasA = models.IntegerField("Проходил ли лечение(алкоголь)",
                                           choices=TREATMENT_WAS_A,
                                           null=True,
                                           blank=True)
    psychologicalRehabilitationWasA = models.IntegerField("Проходил ли психологическую реабилитацию(алкоголь)",
                                                          choices=YESNO,
                                                          null=True,
                                                          blank=True)
    wherePsyRehWasA = models.TextField("Где проходил реабилитацию(алкоголь)?",
                                       null=True,
                                       blank=True)
    durationOfRemissionA = models.DecimalField("Длительность ремиссии (в годах)(алкоголь)",
                                               max_digits=3,
                                               decimal_places=1,
                                               null=True,
                                               blank=True)
    accountingInNarcologicalClinic = models.IntegerField("Учёт в наркологическом диспансере",
                                                         choices=YESNO, null=True, blank=True)
    criminalRecord = models.IntegerField("Наличие судимости",
                                         choices=CRIMINAL_RECORD, null=True, blank=True)
    accountingInODN_RUVD = models.IntegerField("Состоит на учёте в ОДН РУВД",
                                               choices=YES_NO_DONTKNOW, null=True, blank=True)
    caseExaminedInKDN_ZP = models.IntegerField("Рассматривалось дело на КДН и ЗП",
                                               choices=YES_NO_DONTKNOW, null=True, blank=True)

    dateOfResolutionIPR = models.DateField("Дата постановления ИПР", null=True, blank=True)
    resolutionNumber = models.TextField("Номер постановления", null=True, blank=True)
    DateOfTerminationIPR = models.DateField("Дата прекращения ИПР", null=True, blank=True)
    terminationNumber = models.TextField("Номер прекращения", null=True, blank=True)

    commercialSexExperience = models.IntegerField("Опыт коммерческого секса",
                                                  choices=YESNO, null=True, blank=True)
    physicalAbuseExperience = models.IntegerField("Опыт физического насилия",
                                                  choices=YESNO, null=True, blank=True)
    fromHwomPhysical = models.IntegerField("Со стороны кого",
                                           choices=FROM_WHOM,
                                           null=True,
                                           blank=True)
    experienceSexualAbuse = models.IntegerField("Опыт сексуального насилия",
                                                choices=YESNO, null=True, blank=True)
    fromHwomSexual = models.IntegerField("Со стороны кого",
                                         choices=FROM_WHOM,
                                         null=True,
                                         blank=True)

    class Meta:
        verbose_name = 'Информация о противоправных действиях, правонарушениях, употреблении наркотиков, алкоголя'
        verbose_name_plural = 'Информация о противоправных действиях, правонарушениях, употреблении наркотиков, алкоголя'


class ChronicDisease(models.Model):
    """
    Социальная диагностика
    ======================

    1. Сведения о клиенте
    ---------------------

    1.3 Информация о наличии хронического заболевания
    """
    DISEASE = [(1, 'есть'), (2, 'нет')]
    TYPE_INVASION = [(1, 'половой'),
                     (2, 'инъекционный'),
                     (3, 'неизвестно')]

    HIV_TREATMENT = [(1, 'да, регулярно'),
                     (2, 'да, не регулярно'),
                     (3, 'нет')]

    HIV_FAMILY_AWARENESS = [(1, 'да'),
                            (2, 'нет'),
                            (3, 'подозревают'),
                            (4, 'планирует рассказать')]

    VISIT_AIDS = [
        (1, 'раз в 3 месяца'),
        (2, 'раз в полгода'),
        (3, 'раз в год'),
        (4, 'нет')
    ]

    client = models.OneToOneField(Client, on_delete=models.CASCADE)

    hepatitisC = models.IntegerField("Гепатит С",
                                     choices=DISEASE, null=True, blank=True)
    HIVStatus = models.IntegerField("ВИЧ-статус",
                                    choices=DISEASE, null=True, blank=True)
    estimatedTimeOfInfection = models.DecimalField("Когда узнал о диагнозе (в годах)",
                                                   max_digits=3,
                                                   decimal_places=1,
                                                   null=True,
                                                   blank=True)
    estimatedRouteOfInfection = models.IntegerField("Предположительный путь заражения",
                                                    choices=TYPE_INVASION,
                                                    null=True,
                                                    blank=True)
    AIDSCenter = models.IntegerField("Учёт в центре СПИД",
                                     choices=YESNO,
                                     null=True,
                                     blank=True)
    doesCenterVisitAIDS = models.IntegerField("Посещает ли центр СПИД",
                                              choices=VISIT_AIDS,
                                              null=True,
                                              blank=True)
    receivedChemoprophylaxis = models.IntegerField("Получал ли химиопрофилактику",
                                                   choices=YESNO,
                                                   null=True,
                                                   blank=True)
    HIVGetTreatment = models.IntegerField("Получает ли лечение по ВИЧ",
                                          choices=HIV_TREATMENT,
                                          null=True,
                                          blank=True)
    reasonForNotGettingTreatment = models.TextField("Причина, по которой не получает лечение ВИЧ",
                                                    null=True,
                                                    blank=True)
    whoKnow = models.IntegerField("Кто из членов семьи знает о ВИЧ-статусе клиента",
                                  choices=HIV_FAMILY_AWARENESS,
                                  null=True,
                                  blank=True)

    class Meta:
        verbose_name = 'Информация о наличии хронического заболевания'
        verbose_name_plural = 'Информация о наличии хронического заболевания'


class FamilyMembersInformation(models.Model):
    """
    Социальная диагностика
    ======================

    3. Сведения о членах семьи
    --------------------------

    3.1 Общие сведения
    """
    MARITAL_STATUS = [(1, 'не замужем/не женат'),
                      (2, 'сожительство'),
                      (3, 'замужем/женат'),
                      (4, 'в разводе'),
                      (5, 'вдова/вдовец')]

    LIVING_WITH_WHOM = [(1, 'одна/один'),
                        (2, 'со своими родителями'),
                        (3, 'с родителями партнёра (мужа/жены)'),
                        (4, 'с семьёй (партнёр и дети)'),
                        (5, 'с родственниками')]

    client = models.OneToOneField(Client, on_delete=models.CASCADE)

    maritalStatus = models.IntegerField("Семейное положение", choices=MARITAL_STATUS, null=True, blank=True)
    withWhomLiving = models.IntegerField("С кем проживает", choices=LIVING_WITH_WHOM, null=True, blank=True)

    class Meta:
        verbose_name = 'Сведения о членах семьи'
        verbose_name_plural = 'Сведения о членах семьи'


class HusbandInformation(models.Model):
    """
    Социальная диагностика
    ======================

    3. Сведения о членах семьи
    --------------------------

    3.2 Информация о муже/партнёре
    """
    WORK_PLACE = [(1, "постоянное"),
                  (2, "временное"),
                  (3, "эпизодическое"),
                  (4, "не работает"),
                  (5, "состоит в центре занятости населения в качестве безработного")]

    CITYZENSHIP = [(1, 'Россия'),
                   (2, 'страна СНГ')]

    REGISTRATION = [(1, 'постоянная'),
                    (2, 'временная')]

    PLACE_OF_REGISTRATION = [(1, "Санкт-Петербург"),
                             (2, "Ленинградская область"),
                             (3, "другой регион РФ"),
                             (4, "страна СНГ")]

    EDUCATION = [(1, "высшее"),
                 (2, "неоконченное высшее"),
                 (3, "среднее специальное"),
                 (4, "начальное профессиональное"),
                 (5, "обучается"),
                 (6, "полное среднее (11 классов)"),
                 (7, "общее среднее (9 классов)"),
                 (8, "неоконченное общее среднее"),
                 (9, "начальная школа")]

    CATEGORY_FAMILIES = [(1, "полная семья"),
                         (2, "одинокий родитель"),
                         (3, "многодетная семья"),
                         (4, "разведённые"),
                         (5, "беженцы/переселенцы"),
                         (6, "несовершеннолетние родители"),
                         (7, "замещающая семья"),
                         (8, "семья с инвалидом"),
                         (9, "другое")]

    FREQUENCY_OF_DRUGS_USE = [(1, "ежедневно"),
                              (2, "раз в два-три дня"),
                              (3, "раз в неделю"),
                              (4, "раз в месяц"),
                              (5, "реже одного раза в месяц")]

    ALCOHOL_DRINKS_TYPE = [(1, "слабоалкогольные"),
                           (2, "сильноалкогольные")]

    THE_TREATMENT_WAS_A = [(1, "да"),
                           (2, "нет"),
                           (3, "химическая защита")]

    PLACEMENT_SOCIAL_SUPPORT = [
        (1, "консилиум"),
        (2, "приказ")
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    placementSocialSupport = models.IntegerField("Постановка на социальное сопровождение",
                                                 choices=PLACEMENT_SOCIAL_SUPPORT, null=True, blank=True)
    DateOfCreationIPSO = models.DateField("Дата разработки ИППСУ", null=True, blank=True)
    IPPSNumber = models.TextField(verbose_name='Номер ИППСУ', null=True, blank=True)
    ContractPeriod = models.DateField("Срок действия договора", null=True, blank=True)
    contractNumber = models.TextField(verbose_name='Номер договора', null=True, blank=True)
    fullName = models.TextField("ФИО партнёра (мужа/жены)", null=True, blank=True)
    address = models.TextField("Адрес", null=True, blank=True)
    telephoneNumber = models.TextField("Телефон",
                                       max_length=15, null=True, blank=True)
    dod = models.DateField("Дата рождения", null=True, blank=True)
    age = models.IntegerField("Возраст", null=True, blank=True)
    workPlace = models.IntegerField("Место работы",
                                    choices=WORK_PLACE, null=True, blank=True)
    aboutWork = models.TextField("Где, кем работает (при наличии работы)",
                                 null=True,
                                 blank=True)
    aboutNoWork = models.TextField("Причина, по которой не работает",
                                   null=True,
                                   blank=True)
    avDoc = models.IntegerField("Наличие документов",
                                choices=YESNO, null=True, blank=True)
    cityzenship = models.IntegerField("Гражданство",
                                      choices=CITYZENSHIP, null=True, blank=True)
    registration = models.IntegerField("Регистрация",
                                       choices=REGISTRATION, null=True, blank=True)
    placeOfRegistration = models.IntegerField("Место регистрации",
                                              choices=PLACE_OF_REGISTRATION, null=True, blank=True)
    education = models.IntegerField("Образование",
                                    choices=EDUCATION, null=True, blank=True)
    categoryFamilies = models.IntegerField("Категория семей",
                                           choices=CATEGORY_FAMILIES,
                                           null=True,
                                           blank=True)
    disability = models.IntegerField("Инвалидность",
                                     choices=YESNO,
                                     null=True,
                                     blank=True)
    drugUse = models.IntegerField("Употребление наркотиков",
                                  choices=YESNO, null=True, blank=True)
    frequencyOfDrugsUse = models.IntegerField("Частота употребления наркотиков",
                                              choices=FREQUENCY_OF_DRUGS_USE,
                                              null=True,
                                              blank=True)
    durationOfUse = models.DecimalField("Длительность употребления (в годах)",
                                        max_digits=3,
                                        decimal_places=1,
                                        null=True,
                                        blank=True)
    kindOfDrug = models.TextField("Вид наркотика",
                                  null=True,
                                  blank=True)
    theTreatmentWasD = models.IntegerField("Проходил ли лечение(наркотики)",
                                           choices=YESNO,
                                           null=True,
                                           blank=True)
    psychologicalRehabilitationWasD = models.IntegerField("Проходил ли психологическую реабилитацию(наркотики)",
                                                          choices=YESNO,
                                                          null=True,
                                                          blank=True)
    durationOfRemissionD = models.DecimalField("Длительность ремиссии (в годах)(наркотики)",
                                               max_digits=3,
                                               decimal_places=1,
                                               null=True,
                                               blank=True)
    alcoholUse = models.IntegerField("Употребление алкоголя",
                                     choices=YESNO, null=True, blank=True)
    frequencyOfAlcoholUse = models.IntegerField("Частота употрбления алкоголя",
                                                choices=FREQUENCY_OF_DRUGS_USE,
                                                null=True,
                                                blank=True)
    alcoholDrinksType = models.IntegerField("Вид алкогольных напитков",
                                            choices=ALCOHOL_DRINKS_TYPE,
                                            null=True,
                                            blank=True)
    theTreatmentWasA = models.IntegerField("Проходил ли лечение(алкоголь)",
                                           choices=THE_TREATMENT_WAS_A,
                                           null=True,
                                           blank=True)
    psychologicalRehabilitationWasA = models.IntegerField("Проходил ли психологическую реабилитацию(алкоголь)",
                                                          choices=YESNO,
                                                          null=True,
                                                          blank=True)
    durationOfRemissionA = models.DecimalField("Длительность ремиссии (в годах)(алкоголь)",
                                               max_digits=3,
                                               decimal_places=1,
                                               null=True,
                                               blank=True)
    accountingInNarcologicalClinic = models.IntegerField("Учёт в наркологическом диспансере",
                                                         choices=YESNO, null=True, blank=True)
    criminalRecord = models.IntegerField("Наличие судимости",
                                         choices=YESNO, null=True, blank=True)

    class Meta:
        verbose_name = 'Информация о муже/партнёре'
        verbose_name_plural = 'Информация о муже/партнёре'


class User(AbstractUser):
    patronymic = models.CharField("Отчество",
                                  max_length=60, null=True, blank=True)
    position = models.CharField("Должность",
                                max_length=80, null=True, blank=True)


class ExpertOpinion(models.Model):
    """
    Социальная диагностика
    ======================

    5. Заключение специалиста
    """
    client = models.OneToOneField(Client,
                                  on_delete=models.CASCADE)
    specialist = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.PROTECT)
    otherInformation = models.TextField(
        "Другие сведения о клиенте и членах семьи, сообщённые во время диагностического интервью", null=True,
        blank=True)
    expectations = models.TextField(
        "Ожидания клиента от помощи социальной службы (запрос)", null=True, blank=True)
    personaImpressions = models.TextField(
        "Личные впечатления специалиста от взаимодействия с клиентом", null=True, blank=True)

    class Meta:
        verbose_name = 'Заключение специалиста'
        verbose_name_plural = 'Заключения специалиста'


ATTEMPT = [
    (1, 'Первичная'),
    (2, 'Вторичная')
]


class TestBoyko(models.Model):
    """Тест Бойко"""
    AGGRESS = [
        (0, 'дружелюбен, не наносит вреда себе и другим'),
        (1, 'грубоват, замкнут, но не наносит вреда себе и другим'),
        (2, 'грубо, фамильярно разговаривает, публично оскорбляет других,'
            ' ломает или портит вещи, попадает в аварии, случайно наносит себе порезы, травмы'),
        (3, 'высказывает угрозы, дерётся; когда волнуется, может сам себя порезать, прижечь сигаретой;'
            ' может быть статья за неумышленное нанесение повреждений людям или имуществу (115 или 118 УК РФ)'),
        (4, 'частые угрозы, драки, причинение другим и себе физического вреда'
            ' (БДСМ практики, самопорезы, употребление алкоголя с целью «убить печень» и т.д.);'
            ' может быть статья за умышленное причинение вреда другим людям или порчи имущества (111 УК РФ)')]
    ALARM = [
        (0, 'ровный фон настроения'),
        (1, 'настроение немного снижено, лёгкая тревога или раздражительность; не жалуется на плохое настроение,'
            ' но при расспросе оно выявляется'),
        (2, 'жалуется на возникающее время от времени плохое настроение, тревогу, раздражительность'),
        (3, 'плохое настроение, тревога, резкие колебания настроения, страдание на лице, в мимике, позе'),
        (4, 'постоянно плохое настроение («все плохо», «все черное»), плохое самочувствие, плохой сон, аппетит,'
            ' сильная тревога, апатия («все безразлично», «ничего не хочу»), лицо без мимики, подавленный вид и голос')
    ]
    MEMORY_DISORDER = [
        (0, 'ясное мышление, хорошая память, хорошее понимание речи специалиста и умственная работоспособность'),
        (1, 'ухудшение памяти и мышления при долгой нагрузке, забывает важную информацию и не может ее вспомнить,'
            ' отвлекается, «выпадает» из беседы '),
        (2, 'вялое мышление, много говорит о несущественных деталях, нарушена память на текущие события или на'
            ' события прошлого, утомляется при нагрузке'),
        (3, 'застревает на одной мысли и постоянное ее повторяет, или постоянно перескакивает с мысли на мысль;'
            ' временами не понимает, что говорит специалист; теряется, когда надо проанализировать и решить ситуацию;'
            ' примитивно судит о жизни'),
        (4, 'не может вспомнить недавние события, с трудом запоминает новую информацию; не может сосредоточить'
            ' внимание, понять, что ему говорит специалист; ошибочно размышляет или вообще не способен к размышлению;'
            ' ведет себя так, словно не понимает, где находится и что происходит; не может планировать даже ближайшее'
            ' будущее')
    ]
    CRITICISM = [
        (0, 'полностью осознает свое состояние; может смотреть на себя и свою зависимость со стороны;'
            ' видит последствия своих действий'),
        (1, 'частично понимает своё состояния, поведение и заболевание; не всегда может посмотреть на себя со стороны;'
            ' не видит связи между своими действиями и последствиями'),
        (2, 'поверхностное понимание своего положения: на словах может говорить о своей ответственности и анализировать'
            ' свое поведение, но это мало влияет на результат'),
        (3, 'сниженное понимание своего состояния и поведения; не видит связи между своим поведением'
            ' и его последствиями'),
        (4, 'стойкая утрата понимания своего состояния и поведения')
    ]
    SELF_SERVICE = [
        (0, 'содержит себя, свою одежду, жилище в чистоте и порядке'),
        (1, 'кратковременные затруднения в самообслуживании, о которых известно только очень близким людям'),
        (2, 'способен к самообслуживанию, но делает это по минимуму: одежда может быть с небольшими пятнами и измятой,'
            ' волосы не расчесаны, но относительно чистые, запаха нет'),
        (3, 'периодически возникают трудности в самообслуживании, одежда и внешний вид не опрятные, но '
            'базовые навыки гигиены сохранны'),
        (4, 'не соблюдает правил гигиены и не поддерживает порядок в жилище, не справляется с самообслуживанием и'
            ' нуждается в помощи других людей')
    ]
    WORK_ACTIVITY = [
        (0, 'есть постоянная работа, понимает необходимость работать, положительно оценивается коллегами'),
        (1, 'есть постоянная работа, понимает необходимость работать; если затруднения в работе возникают, то они'
            ' кратковременны и о них известно только близким людям'),
        (2, 'конфликты с коллегами по работе, не приводящие к потере работы; периодические прогулы на работе '
            '(в том числе из-за похмелья); с трудом удерживается на работе, часто меняет работу, но не'
            ' остается без неё'),
        (3, 'выбирает работу в «пьющем» коллективе или не способен сохранить рабочее место; вместо постоянной работы'
            ' разовые подработки'),
        (4, 'нет работы, не способен её самостоятельно найти и выполнять')
    ]
    FRIENDS = [
        (0, 'поддерживает контакты с друзьями/знакомыми, способен к эмоциональной привязанности'),
        (1, 'временные затруднения в контактах с друзьями/знакомыми, хотя есть эмоциональная привязанность'),
        (2, 'сужение контактов, общается с людьми, злоупотребляющими алкоголем или наркотиками, проблемы очевидны'
            ' любому человеку'),
        (3, 'частые конфликты с друзьями/знакомыми, родственниками; круг общения снижен до уровня необходимого'
            ' (чаще потребительского)'),
        (4, 'не способен поддерживать контакты с друзьями, знакомыми; отсутствуют социальные связи')
    ]
    FAMILY_RELATION = [
        (0, 'есть семья, желание её иметь и сохранять'),
        (1, 'есть семья и желание её сохранить, хотя имеются кратковременные трудности в отношениях'),
        (2, 'конфликты с родственниками, членами семьи, не приводящие к потере контакта с семьей'),
        (3, 'частые конфликты с членами семьи и близкими, приводящие к долгой разлуке, потере семьи'),
        (4, 'нет семьи; отсутствует желание иметь и сохранять семью')
    ]
    CHILD_PARENT = [
        (0, 'поддерживает престарелых родителей/несовершеннолетних детей финансово и психологически'),
        (1, 'есть кратковременные трудности в отношениях с родителями/детьми, о которых известно только очень'
            ' близким людям'),
        (2, 'отношение к родителям/детям противоречивое: то заботится, то как будто «забывает» о '
            'своей ответственности'),
        (3, 'формальное отношение к родителям/детям, нет эмоциональной привязанности к ним, тратит деньги '
            'только на свои нужды'),
        (4, 'нет семьи; не заботится о членах семьи, детях даже на минимальном уровне')
    ]
    LEISURE = [
        (0, 'в свободное время занимается разнообразными социально-приемлемыми интересами и деятельностью'),
        (1, 'способен планировать свое свободное время, имеет стабильные интересы, а затруднения в этом носят '
            'кратковременный характер'),
        (2, 'довольно бедная сфера  интересов, снижен познавательный интерес, нет стойких интересов, отдых в основном '
            'пассивный и однообразный'),
        (3, 'свободное время проводит пассивно (например, просмотр телевизора), не знает, чем себя занять; иногда может'
            ' употреблять алкоголь или наркотики, курить, чтобы занять время; говорит о необходимости «убивать время»'),
        (4, 'свободное время посвящено поиску и употреблению алкоголя или наркотиков, другие интересы и увлечения'
            ' отсутствуют')
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    aggressiveness = models.IntegerField(verbose_name='1. Агрессивность/аутоагрессивность', choices=AGGRESS)
    alarm = models.IntegerField(verbose_name='2. Тревога и депрессия', choices=ALARM)
    memory_disorder = models.IntegerField(verbose_name='3. Нарушения памяти, мышления, истощаемость',
                                          choices=MEMORY_DISORDER)
    criticism = models.IntegerField(verbose_name='4.Способность критически воспринимать свое состояние и поведение',
                                    choices=CRITICISM)
    self_service = models.IntegerField(verbose_name='5. Способности к самообслуживанию', choices=SELF_SERVICE)
    work_activity = models.IntegerField(verbose_name='6. Трудовая (профессиональная) деятельность',
                                        choices=WORK_ACTIVITY)
    friends = models.IntegerField(verbose_name='7. Контакты с друзьями, знакомыми', choices=FRIENDS)
    family_relation = models.IntegerField(verbose_name='8. Семейные отношения', choices=FAMILY_RELATION)
    child_parent = models.IntegerField(verbose_name='9. Забота о детях/родителях', choices=CHILD_PARENT)
    leisure = models.IntegerField(verbose_name='10. Сфера досуга', choices=LEISURE)
    attempt = models.IntegerField(verbose_name='Диагностика', choices=ATTEMPT)

    class Meta:
        verbose_name = 'Тест Бойко'
        verbose_name_plural = 'Тесты Бойко'


class InterpretationBoyko(models.Model):
    """Интерпретация теста Бойко"""
    AGGRESS = [
        (0, 'проблемы не выявлены'),
        (1, 'проблемы не выявлены'),
        (2, 'средняя агрессивность'),
        (3, 'сильная агрессивность'),
        (4, 'очень сильная агрессивность')
    ]
    ALARM = [
        (0, 'проблемы не выявлены'),
        (1, 'проблемы не выявлены'),
        (2, 'средняя тревога и депрессия'),
        (3, 'сильная тревога и депрессия'),
        (4, 'очень сильная тревога и депрессия')
    ]
    MEMORY_DISORDER = [
        (0, 'проблемы не выявлены'),
        (1, 'проблемы не выявлены'),
        (2, 'средне выраженные нарушения памяти, мышления, внимания'),
        (3, 'сильно выраженные нарушения памяти, мышления, внимания'),
        (4, 'очень сильно выраженные нарушения памяти, мышления, внимания')
    ]
    CRITICISM = [
        (0, 'проблемы не выявлены'),
        (1, 'проблемы не выявлены'),
        (2, 'поверхностное понимание своего положения'),
        (3, 'сниженное понимание своего положения'),
        (4, 'стойкая утрата понимания своего положения')
    ]
    SELF_SERVICE = [
        (0, 'проблемы не выявлены'),
        (1, 'проблемы не выявлены'),
        (2, 'обслуживает себя минимально'),
        (3, 'трудности самообслуживания'),
        (4, 'не справляется с самообслуживанием')
    ]
    WORK_ACTIVITY = [
        (0, 'проблемы не выявлены'),
        (1, 'проблемы не выявлены'),
        (2, 'выраженные проблемы на работе, но не приводящие к её потере'),
        (3, 'серьёзные проблемы при работе, не позволяющие её сохранить'),
        (4, 'нет работы, не способен её самостоятельно найти и выполнять')
    ]
    FRIENDS = [
        (0, 'проблемы не выявлены'),
        (1, 'проблемы не выявлены'),
        (2, 'сужение контактов с людьми'),
        (3, 'суженый круг общения, часты конфликты c окружающими'),
        (4, 'отсутствие социальных связей')
    ]
    FAMILY_RELATION = [
        (0, 'проблемы не выявлены'),
        (1, 'проблемы не выявлены'),
        (2, 'конфликтные отношения с родственниками'),
        (3, 'серьёзные конфликты с родственниками, приводящие к разрывам отношений'),
        (4, 'нет желания иметь/сохранять семью')
    ]
    CHILD_PARENT = [
        (0, 'проблемы не выявлены'),
        (1, 'проблемы не выявлены'),
        (2, 'нестабильно проявляет заботу о детях'),
        (3, 'недостаточно заботится о детях'),
        (4, 'не заботится о детях')
    ]
    LEISURE = [
        (0, 'проблемы не выявлены'),
        (1, 'проблемы не выявлены'),
        (2, 'бедная сфера интересов'),
        (3, 'пассивный досуг ("убивает время")'),
        (4, 'отсутствие досуга, всё время посвящено употреблению')
    ]
    OVERALL_ASSESSMENT = [
        (0, 'нормализация клинических и социальных показателей, стабильное социальное функционирование'),
        (11,
         'частичная нормализация клинических и социальных показателей, средний уровень социального функционирования'),
        (21, 'частичное улучшение клинических и социальных показателей, низкий уровень социального функционирования'),
        (31, 'без изменений клинических и социальных показателей, крайне низкий уровень социального функционирования')
    ]
    test = models.OneToOneField(TestBoyko, on_delete=models.CASCADE)
    aggressiveness = models.IntegerField(verbose_name='Агрессивность/аутоагрессивность', choices=AGGRESS, null=True,
                                         blank=True)
    alarm = models.IntegerField(verbose_name='Тревога и депрессия', choices=ALARM, null=True, blank=True)
    memory_disorder = models.IntegerField(verbose_name='Нарушения памяти, мышления, истощаемость',
                                          choices=MEMORY_DISORDER, null=True, blank=True)
    criticism = models.IntegerField(verbose_name='Способность критически воспринимать свое состояние и поведение',
                                    choices=CRITICISM, null=True, blank=True)
    self_service = models.IntegerField(verbose_name='Способности к самообслуживанию', choices=SELF_SERVICE, null=True,
                                       blank=True)
    work_activity = models.IntegerField(verbose_name='Трудовая (профессиональная) деятельность', choices=WORK_ACTIVITY,
                                        null=True, blank=True)
    friends = models.IntegerField(verbose_name='Контакты с друзьями, знакомыми', choices=FRIENDS, null=True, blank=True)
    family_relation = models.IntegerField(verbose_name='Семейные отношения', choices=FAMILY_RELATION, null=True,
                                          blank=True)
    child_parent = models.IntegerField(verbose_name='Забота о детях/родителях', choices=CHILD_PARENT, null=True,
                                       blank=True)
    leisure = models.IntegerField(verbose_name='Сфера досуга', choices=LEISURE, null=True, blank=True)
    overall_points = models.IntegerField(verbose_name='Общее количество баллов')
    overall_assessment = models.IntegerField(verbose_name='Общая оценка социального функционирования',
                                             choices=OVERALL_ASSESSMENT)
    date = models.DateTimeField(verbose_name='Дата и время прохождения теста', default=timezone.now)

    class Meta:
        verbose_name = 'Интерпретация теста Бойко'
        verbose_name_plural = 'Интерпретации теста Бойко'


GAGE_YESNO = [(0, 'Нет'), (1, 'Да')]


class TestGAGE(models.Model):
    """Тест GAGE"""
    SUBSTANCES = [
        (0, 'Нет'),
        (1, 'Да (за исключением лекарств, выписанные врачом)')
    ]
    LOSS_DOCUMENTS_WHEN = [
        (0, 'Больше года назад'),
        (1, 'За последний год ')
    ]
    LOSS_DOCUMENTS_TIME = [
        (0, 'Один раз'),
        (2, 'Больше одного')
    ]
    DO_NOT_WORK_WHEN = [
        (0, 'Больше года назад'),
        (1, 'Меньше года назад')
    ]
    INJURIES = [
        (0, 'Нет'),
        (1, 'Травмы серьезнее синяков'),
        (3, 'Попадал в больницу из-за травм, полученных в состоянии опьянения')
    ]
    LOTS_ALCOHOL_TIME = [
        (0, 'Менее одного раза в полгода'),
        (1, 'Более одного раза в полгода, реже раза в неделю'),
        (2, 'Каждую неделю'),
        (3, 'Каждый день')
    ]
    DRINK_ALCOHOL_TIME = [
        (0, 'Реже одного раза в неделю'),
        (1, 'Чаще одного раза в неделю'),
        (2, 'Каждый день или «почти каждый день»')
    ]
    TRY_SUBSTANCES = [
        (1, 'Одно наименование'),
        (2, 'Два и более наименований')
    ]
    HOW_USE = [
        (1, 'Курил, нюхал, глотал'),
        (2, 'Внутримышечные инъекции'),
        (3, 'Внутривенные инъекции'),
        (3, 'Всё выше перечисленное')
    ]
    POOR_HEALTH = [
        (0, 'Нет'),
        (1, 'Да'),
        (3, 'Да, требовалась медицинская помощь')
    ]
    COMPANY = [
        (1, 'В компании'),
        (2, 'В одиночку'),
        (2, 'В компании и в одиночку')
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    alcohol = models.IntegerField(verbose_name='1. Злоупотребляли ли Вы алкоголем?', choices=GAGE_YESNO)
    substances = models.IntegerField(verbose_name='2. Пробовали ли Вы какие-нибудь вещества,'
                                                  ' изменяющие настроение и состояние, кроме алкоголя?',
                                     choices=SUBSTANCES)
    loss_documents = models.IntegerField(verbose_name='3.1. Бывали ли в Вашей жизни ситуации,'
                                                      ' когда вы теряли документы и(или) деньги, когда выпьете или'
                                                      ' употребите другие вещества, меняющие состояние?',
                                         choices=GAGE_YESNO, null=True, blank=True)
    loss_documents_when = models.IntegerField(verbose_name='3.1.1. Когда последний раз?', choices=LOSS_DOCUMENTS_WHEN,
                                              null=True, blank=True)
    loss_documents_time = models.IntegerField(verbose_name='3.1.2. Было ли такое один раз в вашей жизни?',
                                              choices=LOSS_DOCUMENTS_TIME, null=True, blank=True)
    do_not_work = models.IntegerField(verbose_name='3.2. Бывали ли в Вашей жизни ситуации, когда Вы не могли выйти на '
                                                   'работу из-за похмелья или состояния опьянения?', choices=GAGE_YESNO,
                                      null=True, blank=True)
    do_not_work_when = models.IntegerField(verbose_name='3.2.1. Когда последний раз?', choices=DO_NOT_WORK_WHEN,
                                           null=True, blank=True)
    loss_loved_ones = models.IntegerField(verbose_name='3.3. Теряли ли Вы отношения с друзьями или любовные,'
                                                       ' потому что Ваш друг или партнер были недовольны вашими '
                                                       'отношениями с алкоголем?',
                                          choices=GAGE_YESNO, null=True, blank=True)
    fight = models.IntegerField(verbose_name='3.4. Бывало ли, что Вы вступали в драку или Вас били, когда Вы были в'
                                             ' состоянии алкогольного опьянения?', choices=GAGE_YESNO, null=True,
                                blank=True)
    injuries = models.IntegerField(verbose_name='3.5. Получали ли Вы травмы в состоянии алкогольного опьянения?',
                                   choices=INJURIES, null=True, blank=True)
    lots_alcohol = models.IntegerField(verbose_name='3.6. Бывало ли, что Вы выпивали больше полбутылки водки,'
                                                    ' или бутылки вина или полутора литров пива за '
                                                    'один раз (за один вечер)?', choices=GAGE_YESNO, null=True,
                                       blank=True)
    lots_alcohol_time = models.IntegerField(verbose_name='3.6.1. Как часто такое случается?', choices=LOTS_ALCOHOL_TIME,
                                            null=True, blank=True)
    drink_alcohol_time = models.IntegerField(verbose_name='3.7. Как часто Вы пьете алкогольные напитки,'
                                                          ' хотя бы чуть-чуть?', choices=DRINK_ALCOHOL_TIME, null=True,
                                             blank=True)
    try_substances = models.TextField(verbose_name='3.8. Какие вещества, влияющие на настроение и изменяющие '
                                                   'сознание, кроме алкоголя Вы пробовали?', null=True, blank=True)
    try_substances_choice = models.IntegerField(verbose_name='Какое количество наименований?', choices=TRY_SUBSTANCES,
                                                null=True, blank=True)
    how_use = models.IntegerField(verbose_name='3.9. Каким способом Вы употребляли наркотические или '
                                               'токсические вещества'
                                               ' (назвать то, что клиент отвечал на вопрос 3.8.)?', choices=HOW_USE,
                                  null=True, blank=True)
    difficulties = models.IntegerField(verbose_name='3.10. Бывали ли трудности на работе или в личных отношениях, когда'
                                                    ' Вы были под действием веществ или  потому, что другие люди были'
                                                    ' слишком обеспокоены Вашей увлеченностью наркотическим веществом?',
                                       choices=GAGE_YESNO, null=True, blank=True)
    poor_health = models.IntegerField(verbose_name='3.11. Бывало ли, что Вы себя плохо чувствовали после употребления'
                                                   ' наркотического вещества (в момент опьянения или после выхода)'
                                                   ' (сильное сердцебиение, слабость, головная боль, тошнота,'
                                                   ' дискомфорт в ЖКТ)?', choices=POOR_HEALTH, null=True, blank=True)
    company = models.IntegerField(verbose_name='3.12. употребляли ли Вы вещества, меняющие настроение,'
                                               ' один или в компании?', choices=COMPANY, null=True, blank=True)
    dose_reduction = models.IntegerField(verbose_name='4.1. Вы думали когда-нибудь о том, чтобы уменьшить'
                                                      '  количество употребляемого алкоголя (наркотических веществ)?',
                                         choices=GAGE_YESNO, null=True, blank=True)
    irritation = models.IntegerField(verbose_name='4.2. Вас раздражает, если люди критикуют Вас за употребление'
                                                  ' алкоголя (употребление наркотиков)?', choices=GAGE_YESNO, null=True,
                                     blank=True)
    fault = models.IntegerField(
        verbose_name='4.3. Вы испытывали когда-нибудь чувство вины по поводу употребления алкоголя (наркотиков)?',
        choices=GAGE_YESNO, null=True, blank=True)
    tone = models.IntegerField(verbose_name='4.4. Вы когда-нибудь употребляли алкоголь (наркотические вещества)'
                                            ' для поднятия тонуса утром или с похмелья?', choices=GAGE_YESNO, null=True,
                               blank=True)
    attempt = models.IntegerField(verbose_name='Диагностика', choices=ATTEMPT)

    class Meta:
        verbose_name = 'Тест GAGE'
        verbose_name_plural = 'Тесты GAGE'


class InterpretationGAGE(models.Model):
    """Интерпретация теста GAGE"""
    RISK_ABUSE = [
        (0, 'проблемы не выявлены'),
        (3, 'выраженные признаки злоупотребления')
    ]
    RISK_DEPENDENCY = [
        (0, 'проблемы не выявлены'),
        (2, 'имеются признаки зависимости')
    ]
    test = models.OneToOneField(TestGAGE, on_delete=models.CASCADE)
    overall_points_risk_abuse = models.IntegerField(
        verbose_name='Общее количество баллов риска злоупотребления')
    risk_abuse = models.IntegerField(verbose_name='Риск злоупотребления', choices=RISK_ABUSE)
    overall_points_risk_dependency = models.IntegerField(
        verbose_name='Общее количество баллов риска зависимости')
    risk_dependency = models.IntegerField(verbose_name='Риск зависимости', choices=RISK_DEPENDENCY)
    date = models.DateTimeField(verbose_name='Дата и время прохождения теста', default=timezone.now)

    class Meta:
        verbose_name = 'Интерпретация теста GAGE'
        verbose_name_plural = 'Интерпретации теста GAGE'


class TestSOCRATES(models.Model):
    """Тест SOCRATES"""
    FORM = [
        (1, 'Полностью не согласен'),
        (2, 'Не согласен'),
        (3, 'Не уверен'),
        (4, 'Согласен'),
        (5, 'Полностью согласен')
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    changes = models.IntegerField(verbose_name='1. Я действительно хочу внести изменения, связанные с '
                                               'употреблением алкоголя/наркотиков, в свой образ жизни', choices=FORM)
    doubt = models.IntegerField(verbose_name='2. Иногда я сомневаюсь, действительно ли я алкоголик/наркоман',
                                choices=FORM)
    aggravation = models.IntegerField(verbose_name='3. Если я не изменю свой образ жизни, связанный с употреблением'
                                                   ' алкоголя/наркотиков, в ближайшее время, мои проблемы'
                                                   ' могут усугубиться', choices=FORM)
    make_changes = models.IntegerField(verbose_name='4. Я уже начал вносить изменения, связанные с употреблением'
                                                    ' алкоголя/наркотиков, в свой образ жизни', choices=FORM)
    too_much = models.IntegerField(verbose_name='5. Одно время я употреблял слишком много алкоголя/наркотиков,'
                                                ' но мне удалось с этим справиться', choices=FORM)
    harm = models.IntegerField(verbose_name='6. Иногда меня интересует, приношу ли я, употребляя алкоголь/наркотики,'
                                            ' вред другим людям', choices=FORM)
    serious_problem = models.IntegerField(verbose_name='7. У меня серьёзные проблемы алкоголем/наркотиками',
                                          choices=FORM)
    changes_lifestyle = models.IntegerField(verbose_name='8. Я не только думаю об изменениях в образе жизни, связанных'
                                                         ' с употреблением алкоголя/наркотиков, но уже кое-что делаю',
                                            choices=FORM)
    hold = models.IntegerField(verbose_name='9. Я уже изменил свой образ жизни, связанный с употреблением '
                                            'алкоголя/наркотиков, и ищу способы, как удержаться от возвращения'
                                            ' к старым привычкам', choices=FORM)
    know_trouble = models.IntegerField(verbose_name='10. Я знаю, что у меня проблемы с алкоголем/наркотиками',
                                       choices=FORM)
    control = models.IntegerField(verbose_name='11. Иногда я задаю себе вопрос, контролирую ли я употребление '
                                               'мной алкоголя/наркотиков', choices=FORM)
    much_harm = models.IntegerField(verbose_name='12. Мой образ жизни, связанный с употреблением алкоголя/наркотиков,'
                                                 ' приносит много вреда', choices=FORM)
    reduce_stop = models.IntegerField(verbose_name='13. Сейчас я предпринимаю активные попытки сократить или прекратить'
                                                   ' употребление алкоголя/наркотиков', choices=FORM)
    help = models.IntegerField(verbose_name='14. Я хочу получить помощь, чтобы не возвращаться к проблемам, которые'
                                            ' я ранее имел из-за алкоголя/наркотиков', choices=FORM)
    have_problem = models.IntegerField(verbose_name='15. У меня проблемы с алкоголем/наркотиками', choices=FORM)
    use_lot = models.IntegerField(verbose_name='16. Иногда я задаю себе вопрос, не употребляю ли я слишком'
                                               ' много алкоголя/наркотиков', choices=FORM)
    alcoholic = models.IntegerField(verbose_name='17. Я – алкоголик/наркоман', choices=FORM)
    try_my_best = models.IntegerField(verbose_name='18. Я стараюсь изо всех сил, чтобы изменить свой образ жизни,'
                                                   ' связанный с употреблением алкоголя/наркотиков', choices=FORM)
    move_on = models.IntegerField(verbose_name='19. Я уже внёс изменения, связанные с употреблением алкоголя/наркотиков'
                                               ' в мой образ жизни, и я нуждаюсь в помощи, чтобы двигаться в этом'
                                               ' направлении дальше', choices=FORM)
    attempt = models.IntegerField(verbose_name='Диагностика', choices=ATTEMPT)

    class Meta:
        verbose_name = 'Тест SOCRATES'
        verbose_name_plural = 'Тесты SOCRATES'


class InterpretationSOCRATES(models.Model):
    """Интерпретация теста SOCRATES"""
    REALIZATION = [
        (35, 'высокое осознание проблем с алкоголем/наркотиками, признаёт проблемы с употреблением ПАВ, '
             'желает измениться и осознаёт, что вред от употребления ПАВ будет продолжаться, '
             'если не наступят изменения'),
        (31, 'среднее осознание проблем с алкоголем/наркотиками'),
        (27, 'низкое осознание проблем с алкоголем/наркотиками, отрицает проблемы с ПАВ, не принимает диагноз'
             ' «зависимость», отсутствует желание меняться'),
        (7, 'очень низкое осознание проблем с алкоголем/наркотиками, отрицает проблемы с ПАВ, не принимает диагноз'
            ' «зависимость», отсутствует желание меняться')
    ]
    AMBIVALENCE = [
        (19, 'очень высокая амбивалентность, клиент иногда задается вопросом, управляют ли он своим употреблением ПАВ,'
             ' причиняет ли он другим людям боль своим употреблением, является ли он зависимым, что отражают некоторую'
             ' открытость и готовность к изменениям'),
        (17, 'высокая амбивалентность, клиент иногда задается вопросом, управляют ли он своим употреблением ПАВ,'
             ' причиняет ли он другим людям боль своим употреблением, является ли он зависимым, что отражают '
             'некоторую открытость и готовность к изменениям'),
        (14, 'средняя амбивалентность в отношении к алкоголю/наркотикам, редко могут возникать мысли о вреде ПАВ'),
        (9, 'низкая амбивалентность, клиент не задается вопросом, является ли его употребление ПАВ проблемой, не '
            'имеет сомнений и размышлений относительно своего употребления'),
        (4, 'очень низкая амбивалентность, клиент не задается вопросом, является ли его употребление ПАВ проблемой, '
            'не имеет сомнений и размышлений относительно своего употребления')
    ]
    ACTION = [
        (39, 'очень высокая готовность к действию, клиент уже предпринимает шаги для того, чтобы произвести '
             'положительные изменения в своем употреблении ПАВ и, возможно, уже имеет некоторый успех в этом; изменения'
             ' находятся в стадии реализации, и клиент нуждается в поддержке или предотвращении срыва;'
             ' можно говорить о положительном прогнозе'),
        (36, 'высокая готовность к действию, клиент уже предпринимает шаги для того, чтобы произвести положительные'
             ' изменения в своем употреблении ПАВ и, возможно, уже имеет некоторый успех в этом; изменения находятся в'
             ' стадии реализации, и клиент нуждается в поддержке или предотвращении срыва; можно говорить о '
             'положительном прогнозе'),
        (31,
         'средняя готовность к действию, может предпринимать отдельные попытки к изменению в своём употреблении ПАВ'),
        (26, 'низкая готовность к действию, отсутствуют конкретных действий по изменению своего употребления ПАВ и '
             'малая вероятность совершения подобных действий в ближайшем будущем'),
        (8, 'очень низкая готовность к действию, отсутствуют конкретных действий по изменению своего употребления ПАВ'
            ' и малая вероятность совершения подобных действий в ближайшем будущем')
    ]
    READY_CHANGE = [
        (19, 'в целом готовность к изменениям низкая'),
        (48, 'в целом готовность к изменениям ниже среднего'),
        (56, 'в целом готовность к изменениям средняя'),
        (78, 'в целом готовность к изменениям выше среднего'),
        (87, 'в целом готовность к изменениям высокая')
    ]
    test = models.OneToOneField(TestSOCRATES, on_delete=models.CASCADE)
    overall_points_realization = models.IntegerField(verbose_name='Общее количество баллов Осознания')
    realization = models.IntegerField(verbose_name='Осознание', choices=REALIZATION)
    overall_points_ambivalence = models.IntegerField(verbose_name='Общее количество баллов Амбивалентности')
    ambivalence = models.IntegerField(verbose_name='Амбивалентность', choices=AMBIVALENCE)
    overall_points_action = models.IntegerField(verbose_name='Общее количество баллов Действия')
    action = models.IntegerField(verbose_name='Действие', choices=ACTION)
    overall_points = models.IntegerField(verbose_name='Общее количество баллов')
    ready_change = models.IntegerField(verbose_name='Готовность к изменениям', choices=READY_CHANGE)
    date = models.DateTimeField(verbose_name='Дата и время прохождения теста', default=timezone.now)

    class Meta:
        verbose_name = 'Интерпретация теста SOCRATES'
        verbose_name_plural = 'Интерпретации теста SOCRATES'


class TypologicalGroup(models.Model):
    """Типологическая группа"""
    GROUP = [
        (0, 'Клиент не может быть относен к типологической группе потребителей ПАВ'),
        (1, 'Группа 1 «Женщины, активно употребляющие ПАВ, противопоставляющие себя социуму»'),
        (2, 'Группа 2 «Женщины, употребляющие ПАВ с более развитым коммуникативным потенциалом»')
    ]
    SUBGROUP = [
        (1, 'Группа 2.1 «Молодые женщины с социально-бытовыми проблемами в период неактивного употребления ПАВ»'),
        (2, 'Группа 2.2 «Женщины с длительным стажем употребления ПАВ и сопутствующими '
            'социально-медицинскими проблемами»')
    ]
    test = models.OneToOneField(TestBoyko, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    group = models.IntegerField(verbose_name='Основная типологическая группа', choices=GROUP)
    subgroup = models.IntegerField(verbose_name='Подгруппа типологической группы 2', choices=SUBGROUP, null=True,
                                   blank=True)

    class Meta:
        verbose_name = 'Типологическая группа'
        verbose_name_plural = 'Типологические группы'
