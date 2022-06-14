from verify_ip.ext.db import db
from verify_ip.ext.models.ips import Ips
from verify_ip.ext.controllers.utils import slack_notification
import requests

def select_ip():
    ip = Ips.query.filter_by(ip_status=True).first()
    return ip


def verify_ip(old_ip):
    r = requests.get("http://ifconfig.me/ip")
    ip_actual = r.text
    
    if old_ip:
        if ip_actual == old_ip.ip_number:
            slack_notification(
            title="Your IP has changed",
            service="IP check service",
            author="J. Jefferson N. do Vale",
            type="NOT CHANGED",
            message="IP HAS NOT CHANGED"
            )
            return "IP HAS NOT CHANGED"
        else:
            try:
                new_ip = Ips(ip_number=ip_actual, ip_status=True)
                old_ip.ip_status = False
                db.session.add(new_ip)
                db.session.add(old_ip)
                db.session.commit()                
            except Exception as error:
                return error
            finally:
                slack_notification(
                    title="Your IP has changed",
                    service="IP check service",
                    author="J. Jefferson N. do Vale",
                    type="CHANGED",
                    message=f"Your IP has changed for {new_ip}"
                    )
                return "Updated IP"
    else:
        try:
            new_ip = Ips(ip_number=ip_actual, ip_status=True)
            db.session.add(new_ip)
            db.session.commit()
        except Exception as error:
            return error
        finally:
            slack_notification(
                title="Your IP has changed",
                service="IP check service",
                author="J. Jefferson N. do Vale",
                type="IP INSERTED",
                message=f"Insert new IP in database. IP: {new_ip}"
                )
            return "INSERT IP IN DATABASE"
