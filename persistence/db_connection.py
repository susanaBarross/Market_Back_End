import psycopg2

class ConnectionDb:

    def connect(self):        
        conn = None
        try:
            conn = psycopg2.connect(
                       host="localhost",
                       database="market",
                       user="postgres", 
                       password="1234")

            return conn

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)