
from io import BytesIO
import cStringIO as StringIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class Render:
    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        res = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), res)
        if not pdf.err:
            return HttpResponse(res.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)



# from io import StringIO
# # import cStringIO as StringIO
# from xhtml2pdf import pisa
# from django.template.loader import get_template
# from django.template import Context
# from django.http import HttpResponse
# from cgi import escape


# def render(path: str, params: dict):
#     template = get_template(path)
#     context = Context(params)
#     html  = template.render(context)
#     res = StringIO.StringIO()

#     pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), res)
#     if not pdf.err:
#         return HttpResponse(res.getvalue(), content_type='application/pdf')
#     return HttpResponse("Error Rendering PDF", status=400)