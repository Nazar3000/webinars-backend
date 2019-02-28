from contextlib import suppress
from datetime import datetime
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError

from users.models import DeviceData


class DeviceDataMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            ip = self.get_client_ip(request)
            device, created = DeviceData.objects.get_or_create(
                user=request.user,
                ip_address=ip,
                user_agent=request.META['HTTP_USER_AGENT']
            )

            g = GeoIP2()
            with suppress(AddressNotFoundError):
                city_dict = g.city(ip)

                device.country = city_dict['country_name']
                device.region = city_dict['region']

                request.user.timezone = city_dict['time_zone']
                request.user.save()
            device.save()

        return response