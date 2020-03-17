import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',  # si es base de datos remota se coloca la ip
            user='root',
            password='1234',
            db='conectadapython'
        )
        self.cursor = self.connection.cursor()
        print('Conexion establecida exitosamente')

    def select_user(self, id):
        sql = f'SELECT id, username, email FROM users WHERE id = {id}'
        try:
            self.cursor.execute(sql)
            # fetchone es para recibir el primer resultado o mejor un solo resultado
            user = self.cursor.fetchone()
            print('Id:', user[0])
            print('Username:', user[1])
            print('Email:', user[2])
        except Exception as e:
            raise

    def select_all_user(self):
        sql = 'SELECT id,username,email FROM users'
        try:
            self.cursor.execute(sql)
            # fetchall es para recibir todos los registros que la base de datos encuentre
            users = self.cursor.fetchall()
            for user in users:
                print('Id:', user[0])
                print('Username:', user[1])
                print('Email:', user[2])
                print('_______________\n')
        except Exception as e:
            raise

    def update_user(self, id, username):
        sql = f"UPDATE users SET username = '{username}' WHERE id = {id}"
        try:
            self.cursor.execute(sql)
            self.connection.commit()  # Esto hace que cualquier cambio hecho quede bien hecho en la base de datos, esto se usa al instertar, actualizar o eliminar algun registro de la base de datos
            # NOTA: si no se hace el commit, en la base de datos no se efectuara correctamente el cambio
        except Exception as e:
            pass

    def close(self):
        # Esto cierra la conexion a la base de datos
        self.connection.close()


database = DataBase()
# database.select_user(1)
# database.select_all_user()
database.select_user(1)
database.update_user(1, 'Cambio de nombre')
database.select_user(1)
database.close()
