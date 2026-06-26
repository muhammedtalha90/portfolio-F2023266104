import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

import shutil
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience, Project

# Clear existing
Bio.objects.all().delete()
Education.objects.all().delete()
Skill.objects.all().delete()
Experience.objects.all().delete()
Project.objects.all().delete()

# Copy profile image to media
os.makedirs('media/profile', exist_ok=True)
shutil.copy('static/images/profile.jpg', 'media/profile/profile.jpg')

# Bio
Bio.objects.create(
    name="Talha Ijaz",
    job_title="CS Student & Aspiring Software Developer",
    description="I'm a 3rd-year Computer Science student at UMT with a passion for backend development, cloud computing, and building clean, functional web applications. Currently exploring the intersection of software engineering and modern cloud infrastructure.",
    profile_picture="profile/profile.jpg",
    email="talha.ijaz@example.com",
    github="https://github.com/talhajaz",
    linkedin="https://linkedin.com/in/talhajaz"
)

# Education
Education.objects.create(
    degree="Bachelor of Science in Computer Science",
    institution="University of Management and Technology (UMT)",
    start_year="2023",
    end_year="Present",
    description="Currently in 6th Semester. Coursework includes Web Technologies, Data Structures, Algorithms, Operating Systems, and Database Systems."
)

# Skills
skills_data = [
    ("HTML", "technical", 90),
    ("CSS", "technical", 85),
    ("JavaScript", "technical", 80),
    ("Python", "technical", 85),
    ("Django", "technical", 78),
    ("Linux", "technical", 75),
    ("Communication", "professional", 85),
    ("Problem Solving", "professional", 88),
    ("Team Collaboration", "professional", 82),
]
for name, cat, pct in skills_data:
    Skill.objects.create(name=name, category=cat, proficiency=pct)

# Experience
Experience.objects.create(
    title="Marketing Intern",
    organization="BizzUPro",
    start_date="Feb 2026",
    end_date="Present",
    description="Supporting digital marketing campaigns, assisting in content strategy, and gaining hands-on experience in brand communications and online outreach for a growing startup."
)

# Projects
Project.objects.create(
    title="Portfolio Website",
    description="A fully dynamic personal portfolio website built with Django. Features a custom MVT architecture with separate apps for Bio, Education, Skills, Experience, and Projects — all data driven from a SQLite database.",
    tech_stack="Python, Django, HTML, CSS, JavaScript, SQLite",
    link=""
)
Project.objects.create(
    title="Todo List Application",
    description="A task management web application that allows users to create, update, and delete tasks. Built with Django on the backend with a clean, minimal frontend interface.",
    tech_stack="Python, Django, HTML, CSS, JavaScript",
    link=""
)

print("✅ Data seeded successfully!")
