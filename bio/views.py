from django.shortcuts import render
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience, Project

def index(request):
    bio = Bio.objects.first()
    educations = Education.objects.all()
    technical_skills = Skill.objects.filter(category='technical')
    professional_skills = Skill.objects.filter(category='professional')
    experiences = Experience.objects.all()
    projects = Project.objects.all()

    context = {
        'bio': bio,
        'educations': educations,
        'technical_skills': technical_skills,
        'professional_skills': professional_skills,
        'experiences': experiences,
        'projects': projects,
    }
    return render(request, 'index.html', context)
