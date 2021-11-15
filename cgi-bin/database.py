#!/usr/bin/python3
# -*- coding: utf-8 -*-
import html

import pymysql
import hashlib

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

class Food:
    def __init__(self, user, password):
        self.conn = pymysql.connect(
            db='cc500207_db',
            user=user,
            password=password,
            host='localhost',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def add_evento(self, data):
        # data = (region(0), comuna(1), sector(2), nombre(3),
        #         email(4), celular(5), red-social(6),
        #         red-id(7), dia-hora-inicio(8), dia-hora-termino(9),
        #         descripcion-evento(10), tipo-comida(11), foto-comida(12))

        com_id = self.get_comuna_id(data['comuna'].value)

        # se inserta el evento a tabla evento con proteccion contra inyeccion de codigo en campos necesarios
        sql = """
        INSERT INTO evento (comuna_id, sector, nombre, email, celular, 
            dia_hora_inicio, dia_hora_termino, descripcion, tipo) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        self.cursor.execute(sql, (com_id, html.escape(data['sector'].value), data['nombre'].value,
                                  data['email'].value, data['celular'].value, data['dia-hora-inicio'].value,
                                  data['dia-hora-termino'].value, html.escape(data['descripcion-evento'].value),
                                  data['tipo-comida'].value))
        self.conn.commit()
        event_id = self.cursor.lastrowid

        # se insertan las fotos del evento a tabla foto
        file_obj = data['foto-comida']
        if not isinstance(file_obj, list):
            file_obj = [data['foto-comida']]

        for file_elem in file_obj:
            filename = file_elem.filename

            if not filename:
                continue

            sql = """
            SELECT count(id)
            FROM foto
            """
            self.cursor.execute(sql)
            total = self.cursor.fetchall()[0][0]

            file_hash = str(total) + hashlib.sha1(filename.encode('utf-8')).hexdigest()

            #open('../media/' + file_hash, 'wb').write(file_elem.file.read())
            open('media/' + file_hash, 'wb').write(file_elem.file.read())

            sql = f"""
            INSERT INTO foto (ruta_archivo, nombre_archivo, evento_id)
            VALUES (%s, %s, %s);
            """
            self.cursor.execute(sql, (file_hash, filename, event_id))
            self.conn.commit()

        # se insertan las redes sociales a la tabla red_social
        redes = data.getlist('red-social')
        red_ids = data.getlist('red-id')
        for redKey in range(len(redes)):
            if redes[redKey] == "":
                continue
            sql = f"""
            INSERT INTO red_social (nombre, identificador, evento_id)
            VALUES (%s, %s, %s);
            """
            self.cursor.execute(sql, (redes[redKey], red_ids[redKey], event_id))
            self.conn.commit()

    def get_comuna_id(self, nombre):
        sql = """
        SELECT id
        FROM comuna
        WHERE nombre = %s;
        """
        self.cursor.execute(sql, nombre)
        return self.cursor.fetchall()[0][0]

    def get_comuna_name_by_id(self, c_id):
        sql = """
        SELECT nombre
        FROM comuna
        WHERE id = %s;
        """
        self.cursor.execute(sql, c_id)
        return self.cursor.fetchall()[0][0]

    def get_regiones(self):
        sql = """
        SELECT nombre
        FROM region;
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comunas(self):
        sql = """
        SELECT nombre
        FROM comuna;
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_one_region(self, number):
        sql = f"""
        SELECT nombre
        FROM region
        WHERE id = {number};
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_comunas_of_region(self, region):
        sql = f"""
        SELECT nombre
        FROM comuna
        WHERE region_id IN
            (SELECT id
            FROM region
            WHERE nombre = '{region}');
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_last_5_events(self):
        sql = """
        SELECT id, dia_hora_inicio, dia_hora_termino, comuna_id, sector, descripcion, tipo
        FROM evento 
        ORDER BY dia_hora_inicio DESC
        LIMIT 5;
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_all_events(self):
        sql = """
        SELECT *
        FROM evento
        ORDER BY dia_hora_inicio DESC;
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_region_id_by_comuna_id(self, comuna_id):
        sql = f"""
        SELECT region_id
        FROM comuna
        WHERE id = {comuna_id};
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_region_by_id(self, region_id):
        sql = f"""
        SELECT nombre
        FROM region
        WHERE id = {region_id};
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0][0]

    def get_all_event_redes(self, e_id):
        sql = f"""
        SELECT nombre, identificador
        FROM red_social
        WHERE evento_id = {e_id};
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_all_event_fotos(self, e_id):
        sql = f"""
        SELECT ruta_archivo
        FROM foto
        WHERE evento_id = {e_id};
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
