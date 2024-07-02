from app.database import get_db

class User:
    #CONSTRUCTOR
    def __init__(self,id_user=None,email=None,password=None,nombre=None,apellido=None,pais=None,nacional=None,
                 phone=None,fechaN=None):
        self.id_user = id_user
        self.nombre= nombre
        self.apellido = apellido
        self.email = email
        self.password = password    
        self.pais = pais
        self.nacional = nacional
        self.phone = phone
        self.fechaN = fechaN

    @staticmethod
    def get_by_id(iduser):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE idUser = %s ", (iduser,))
        row = cursor.fetchone()
        cursor.close()
        if row:     
           return User(id_user=row[0], nombre=row[1], apellido=row[2], email=row[3],password=row[4],pais=row[5],nacional=row[6],phone=row[7],fechaN=row[8])            
        return None

    @staticmethod
    def get_by_user(iduser,idpass):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE idUser = %s and UserPassword = %s", (iduser,idpass,))
        row = cursor.fetchone()
        cursor.close()
        if row:     
          return User(id_user=row[0], nombre=row[1], apellido=row[2], email=row[3],password=row[4],pais=row[5],nacional=row[6],phone=row[7],fechaN=row[8])       
        return None



    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        usuarios = [User(id_user=row[0], nombre=row[1], apellido=row[2], email=row[3], password=row[4],pais=row[5],nacional=row[6],phone=row[7],fechaN=row[8]) for row in rows]
        cursor.close()
        return usuarios



    def newsave(self):

        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
        UPDATE users SET  UserName = %s  WHERE idUser = %s
        """, (self.nombre,self.id_user,))
        db.commit()
        cursor.close()
            

    def save(self):

        db = get_db()
        cursor = db.cursor()

        if self.id_user:
            cursor.execute("""
            INSERT INTO users (idUser, UserName, UserSurname, UserEmail, UserPassword,UserPais, UserNaciona,UserPhone, UserFechaN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (self.id_user, self.nombre,self.apellido,self.email,self.password,self.pais,self.nacional,self.phone,self.fechaN))
            self.id_user = cursor.lastrowid
            db.commit()
            cursor.close()
        # else:
            
        #     cursor.execute("""
        #     UPDATE users SET  UserName = %s  WHERE idUser = %s
        #     """, (self.nombre,self.id_user,))
            
    
    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM users WHERE idUser = %s", (self.id_user,))
        db.commit()
        cursor.close()


    def serialize(self):
        return {
            'id_user': self.id_user,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'password': self.password,            
            'pais': self.pais,
            'nacional': self.nacional,
            'phone': self.phone,
            'fechaN': self.fechaN,
        }
    def Nombre(self):
        return {
            'nombre': self.nombre,   
            'apellido': self.apellido,      
        }
  


