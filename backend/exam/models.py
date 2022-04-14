from django.db import models
from django.utils.translation import gettext_lazy as _


def medica_specialty():
    '''
    Tipos de especialidade medica 
    '''
    choice = [
        (1, _('Alergia e Imunologia')),
        (2, _('Anestesiologia')),
        (3, _('Angiologia')),
        (4, _('Cardiologia')),
        (5, _('Cirurgia Cardiovascular')),
        (6, _('Cirurgia da Mão')),
        (7, _('Cirurgia de cabeça e pescoço')),
        (8, _('Cirurgia do Aparelho Digestivo')),
        (9, _('Cirurgia Geral')),
        (10, _('Cirurgia Pediátrica')),
        (11, _('Cirurgia Plástica')),
        (12, _('Cirurgia Torácica')),
        (13, _('Cirurgia Vascular')),
        (14, _('Clínica Médica')),
        (15, _('Coloproctologia')),
        (16, _('Dermatologia')),
        (17, _('Endocrinologia e Metabologia')),
        (18, _('Endoscopia')),
        (19, _('Gastroenterologia')),
        (20, _('Genética médica')),
        (21, _('Geriatria')),
        (22, _('Ginecologia e obstetrícia')),
        (23, _('Hematologia e Hemoterapia')),
        (24, _('Homeopatia')),
        (25, _('Infectologia')),
        (26, _('Mastologia')),
        (27, _('Medicina de Família e Comunidade')),
        (28, _('Medicina de Emergência')),
        (29, _('Medicina do Trabalho')),
        (30, _('Medicina do Tráfego')),
        (31, _('Medicina Esportiva')),
        (32, _('Medicina Física e Reabilitação')),
        (33, _('Medicina Intensiva')),
        (34, _('Medicina Legal e Perícia Médica')),
        (35, _('Medicina Nuclear')),
        (36, _('Medicina Preventiva e Social')),
        (37, _('Nefrologia')),
        (38, _('Neurocirurgia')),
        (39, _('Neurologia')),
        (40, _('Nutrologia')),
        (41, _('Obstetrícia')),
        (42, _('Oftalmologia')),
        (43, _('Ortopedia e Traumatologia')),
        (44, _('Otorrinolaringologia')),
        (45, _('Patologia')),
        (46, _('Patologia Clínica/Medicina laboratorial')),
        (47, _('Pediatria')),
        (48, _('Pneumologia')),
        (49, _('Psiquiatria')),
        (50, _('Radiologia e Diagnóstico por Imagem')),
        (51, _('Radioterapia')),
        (52, _('Reumatologia')),
        (53, _('Toxicologia médica')),
        (54, _('Urologia')),
    ]
    return choice

# TODO como ter um id diferenciado por exemplo para medico MD01.


class Doctor(models.Model):
    specialty = models.CharField(max_length=3, choices=medica_specialty())
    price_consultation = models.DecimalField(max_digits=8, decimal_places=2)
