from django.core.management.base import BaseCommand
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience, Project

class Command(BaseCommand):
    help = 'Seed portfolio data'

    def handle(self, *args, **kwargs):
        if Bio.objects.exists():
            self.stdout.write('Data already seeded.')
            return

        Bio.objects.create(
            name="Talha Ijaz",
            job_title="CS Student & Aspiring Software Developer",
            description="I'm a 3rd-year Computer Science student at UMT with a passion for backend development, cloud computing, and building clean, functional web applications. Currently exploring the intersection of software engineering and modern cloud infrastructure.",
            email="talha.ijaz@example.com",
            github="https://github.com/talhajaz",
            linkedin="https://linkedin.com/in/talhajaz"
        )

        Education.objects.create(
            degree="Bachelor of Science in Computer Science",
            institution="University of Management and Technology (UMT)",
            start_year="2023",
            end_year="Present",
            description="Currently in 6th Semester. Coursework includes Web Technologies, Data Structures, Algorithms, Operating Systems, and Database Systems."
        )

        for name, cat, pct in [
            ("HTML","technical",90),("CSS","technical",85),
            ("JavaScript","technical",80),("Python","technical",85),
            ("Django","technical",78),("Linux","technical",75),
            ("Communication","professional",85),
            ("Problem Solving","professional",88),
            ("Team Collaboration","professional",82),
        ]:
            Skill.objects.create(name=name, category=cat, proficiency=pct)

        Experience.objects.create(
            title="Marketing Intern", organization="BizzUPro",
            start_date="Feb 2026", end_date="Present",
            description="Supporting digital marketing campaigns, assisting in content strategy, and gaining hands-on experience in brand communications and online outreach."
        )

        Project.objects.create(
            title="Portfolio Website",
            description="A fully dynamic personal portfolio website built with Django featuring a custom MVT architecture with separate apps for Bio, Education, Skills, Experience, and Projects.",
            tech_stack="Python, Django, HTML, CSS, JavaScript, SQLite", link=""
        )
        Project.objects.create(
            title="Todo List Application",
            description="A task management web application that allows users to create, update, and delete tasks with a clean minimal interface.",
            tech_stack="Python, Django, HTML, CSS, JavaScript", link=""
        )

        self.stdout.write(self.style.SUCCESS('✅ Portfolio data seeded!'))
