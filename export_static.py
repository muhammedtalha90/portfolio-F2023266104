"""
Generates a fully static HTML copy of the portfolio for Netlify deployment.
Run: python export_static.py
Output goes to: dist/  (upload dist/ to Netlify)
"""
import django, os, shutil
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.test import RequestFactory
from django.template.loader import render_to_string
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience, Project

OUTPUT = 'dist'
shutil.rmtree(OUTPUT, ignore_errors=True)
os.makedirs(OUTPUT)

# Copy static files
if os.path.exists('staticfiles'):
    shutil.copytree('staticfiles', os.path.join(OUTPUT, 'static'))
if os.path.exists('media'):
    shutil.copytree('media', os.path.join(OUTPUT, 'media'))

# Render HTML
context = {
    'bio': Bio.objects.first(),
    'educations': Education.objects.all(),
    'technical_skills': Skill.objects.filter(category='technical'),
    'professional_skills': Skill.objects.filter(category='professional'),
    'experiences': Experience.objects.all(),
    'projects': Project.objects.all(),
    'STATIC_URL': '/static/',
    'MEDIA_URL': '/media/',
}

# Patch static/media URLs for static export
from django.conf import settings
settings.STATIC_URL = '/static/'
settings.MEDIA_URL = '/media/'

html = render_to_string('index.html', context)
# Fix static URLs in rendered HTML
html = html.replace('/static/', '/static/')

with open(os.path.join(OUTPUT, 'index.html'), 'w') as f:
    f.write(html)

print(f"✅ Static site exported to ./{OUTPUT}/")
print(f"   Upload the '{OUTPUT}' folder to Netlify as your site.")
