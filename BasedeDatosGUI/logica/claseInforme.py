from logica.clasedatos import *


class informeBase(BaseDatos):
    def informeUsuario(self, cursor):
        #select  u.nickname,u.nombre,u.correo,sum(t.monto)
    #from transaccion t, usuario u  where
    #    t.usr_nickname=u.nickname
    #group by (u.nickname)  order by sum(t.monto) desc;
        try:
            cursor.execute("""select  u.nickname,u.nombre,u.correo,sum(t.monto) from transaccion t, usuario u  where t.usr_nickname=u.nickname group by (u.nickname) order by sum(t.monto) desc""")
            datos = cursor.fetchall()
            return datos
        except:
            return []

    def informeJuego(self, cursor):
        try:
            cursor.execute("SELECT v.id,v.jgo_nombre,v.plt_nombre,p.modelo,sum(t.monto) FROM transaccion t,pago pa,version v,plataforma p WHERE pa.vrs_id=v.id AND pa.nombre=t.pgo_nombre AND v.plt_nombre=p.nombre GROUP BY (v.id,v.jgo_nombre,p.nombre,p.modelo ) ORDER BY sum(t.monto) DESC ;")
            datos = cursor.fetchall()
            return datos
        except:
            return []