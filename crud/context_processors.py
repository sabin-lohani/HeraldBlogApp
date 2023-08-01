from .models import FooterContent, FooterLink

def footer_data(request):
    footer_content = FooterContent.objects.first()
    footer_links = FooterLink.objects.all()
    return {
        'footer_content': footer_content,
        'footer_links': footer_links,
    }