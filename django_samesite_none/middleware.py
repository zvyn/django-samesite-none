import re
from http import cookies

cookies.Morsel._reserved["samesite"] = "SameSite"
OLD_CHROME_REGEX = r"(Chrome|Chromium)\/((5[1-9])|6[0-6])"


class SameSiteNoneMiddleware:
    """Set SameSite="None" if it was None before (workaround for django#30862)

    This middleware will be obsolete when your app will start using Django 3.1.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # same-site = None introduced for Chrome 80 breaks for Chrome 51-66
        # Refer (https://www.chromium.org/updates/same-site/incompatible-clients)
        user_agent = request.META.get("HTTP_USER_AGENT")
        if not (user_agent and re.search(OLD_CHROME_REGEX, user_agent)):
            for name, value in response.cookies.items():
                if not value.get("samesite"):
                    value["samesite"] = "None"
                    value["secure"] = True  # fixes plain set_cookie(name, value)

        return response
