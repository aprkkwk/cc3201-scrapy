# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DatabasesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #Datos del anime
    Titulo = scrapy.Field()
    Titulo_Japones = scrapy.Field()
    Tipo = scrapy.Field()
    Estado = scrapy.Field()
    Episodios = scrapy.Field()
    Periodo_Emision = scrapy.Field()
    Temporada = scrapy.Field()
    Horario = scrapy.Field()
    Peoductores = scrapy.Field()
    Licenciantes = scrapy.Field()
    Estudio = scrapy.Field()
    Fuente = scrapy.Field()
    Genero = scrapy.Field()
    Duracion_episodio = scrapy.Field()
    Rating=scrapy.Field()

    pass
