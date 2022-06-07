import requests
import connection_db

ip_old = connection_db.consult("SELECT ip_number FROM ip WHERE ip_active = 1 limit 1;")
def verify_ip(ip_old):
    r = requests.get('http://ifconfig.me/ip')
    ip_actual = r.text
    
    if ip_old:
        if ip_actual == ip_old[0][0]:
            return("IP HAS NOT CHANGED")
        else:
            try:
                print(ip_actual, ip_old[0][0])
                insert_new_ip = connection_db.alterData(f"INSERT INTO ip(ip_number, ip_active) VALUES('{ip_actual}', 1)")
                inactive_old_ip = connection_db.alterData(f"UPDATE ip SET ip_active = 0 WHERE ip_number = '{ip_old[0][0]}'")
            except Exception as error:
                return error
            finally:
                if insert_new_ip and inactive_old_ip:
                    return("Updated IP")
    else:
        try:
            insert_new_ip = connection_db.alterData(f"INSERT INTO ip(ip_number, ip_active) VALUES('{ip_actual}', 1)")
        except Exception as error:
            return error
        finally:
            return("INSERT IP IN DATABASE")
            
result = verify_ip(ip_old)
print(result)