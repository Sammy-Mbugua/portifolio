from django.core.management.base import BaseCommand
from portfolio.models import *
from datetime import date
# Management command to populate portfolio with sample data
class Command(BaseCommand):
    help = 'Populate portfolio with sample data from CV'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating portfolio data...')
        
        # Create Profile
        Profile.objects.all().delete()
        profile = Profile.objects.create(
            name="Sammy Gicheha Mbugua",
            title="Software Developer | Business Intelligence Enthusiast | Network Specialist",
            email="msammy542@gmail.com",
            phone="+254 757 255 028",
            location="Nairobi, Kenya",
            github_url="https://github.com/sammy-mbugua",
            linkedin_url="https://www.linkedin.com/in/sammymbugua-407b9533a",
            about="A computer science professional with a strong foundation in software development, networking, and business intelligence. Experienced in working with modern frameworks and tools like Laravel, Livewire, Power BI, and Python, delivering reliable solutions in fast-paced, team-oriented environments. Excellent at troubleshooting, collaborating in teams, and translating complex problems into smart software solutions."
        )
        self.stdout.write(self.style.SUCCESS(f'Created profile: {profile.name}'))
        
        # Create Education
        Education.objects.all().delete()
        edu = Education.objects.create(
            degree="Bachelor of Science in Computer Science",
            institution="University of Embu",
            start_date=date(2019, 8, 1),
            end_date=date(2023, 8, 31),
            location="Embu, Kenya"
        )
        self.stdout.write(self.style.SUCCESS(f'Created education: {edu.degree}'))
        
        # Create Experiences
        Experience.objects.all().delete()
        
        exp1 = Experience.objects.create(
            title="Software Developer Intern",
            company="Quest Developers Company",
            start_date=date(2024, 7, 1),
            end_date=date(2025, 3, 31),
            description="Internship focused on PHP development, BI, and machine learning"
        )
        achievements1 = [
            "Developed PHP projects using Laravel and Livewire (e.g., hover.com)",
            "Built interactive dashboards using Power BI",
            "Created machine learning models, including Swahili-English spam detection",
            "Designed frontend themes using HTML, Tailwind CSS, Alpine.js",
            "Collaborated on database migrations with MySQL"
        ]
        for i, desc in enumerate(achievements1, 1):
            Achievement.objects.create(experience=exp1, description=desc, order=i)
        
        exp2 = Experience.objects.create(
            title="Software Engineer",
            company="Nairobi Institute of Software Development",
            start_date=date(2023, 6, 1),
            end_date=date(2024, 5, 31),
            description="Full-stack development and teaching programming"
        )
        achievements2 = [
            "Delivered full-stack development projects and taught programming (Python, Laravel, JS)",
            "Conducted software/hardware troubleshooting and maintenance",
            "Led classes in graphics design and AutoCAD",
            "Improved system stability and team development capacity"
        ]
        for i, desc in enumerate(achievements2, 1):
            Achievement.objects.create(experience=exp2, description=desc, order=i)
        
        exp3 = Experience.objects.create(
            title="Project Developer",
            company="Online Competition",
            start_date=date(2022, 11, 1),
            end_date=date(2023, 4, 30),
            description="Competitive IT project development"
        )
        achievements3 = [
            "Co-created various IT projects in diverse languages",
            "Collaborated with team members in coding and troubleshooting",
            "Improved project management and real-world problem-solving skills"
        ]
        for i, desc in enumerate(achievements3, 1):
            Achievement.objects.create(experience=exp3, description=desc, order=i)
        
        exp4 = Experience.objects.create(
            title="Software Developer Attachment",
            company="Milestone College",
            start_date=date(2022, 4, 1),
            end_date=date(2022, 9, 30),
            description="Database development and IT instruction"
        )
        achievements4 = [
            "Assisted in database planning and development",
            "Delivered IT instruction and technical support services",
            "Participated in Python-based software development and code reviews",
            "Designed and deployed basic websites"
        ]
        for i, desc in enumerate(achievements4, 1):
            Achievement.objects.create(experience=exp4, description=desc, order=i)
        
        self.stdout.write(self.style.SUCCESS(f'Created {Experience.objects.count()} experiences'))
        
        # Create Skill Categories and Skills
        SkillCategory.objects.all().delete()
        Skill.objects.all().delete()
        
        skills_data = {
            'Programming Languages': ['Python', 'PHP'],
            'Frameworks & Tools': ['Laravel', 'Livewire', 'React', 'Alpine.js', 'Tailwind CSS', 'Power BI'],
            'Databases': ['MySQL'],
            'Networking': ['TCP/IP', 'DNS', 'Subnetting', 'Switching', 'Routing', 'Network Security'],
            'BI & Reporting': ['Power BI', 'Excel'],
        }
        
        for order, (category_name, skills) in enumerate(skills_data.items(), 1):
            category = SkillCategory.objects.create(name=category_name, order=order)
            for skill_order, skill_name in enumerate(skills, 1):
                Skill.objects.create(
                    name=skill_name,
                    category=category,
                    proficiency=85,
                    order=skill_order
                )
            self.stdout.write(self.style.SUCCESS(f'Created category: {category_name} with {len(skills)} skills'))
        
        # Create Projects
        Project.objects.all().delete()
        
        projects_data = [
            {
                'title': 'PHP Laravel Web Application',
                'description': 'Developed using Laravel, Livewire, Tailwind CSS, Alpine.js, HTML, MySQL. Improved company-client communication via integrated feedback modules.',
                'technologies': 'Laravel, Livewire, Tailwind CSS, Alpine.js, HTML, MySQL',
                'featured': True,
                'order': 1
            },
            {
                'title': 'Ethereum Blockchain Platform',
                'description': 'Created a decentralized platform with smart contract functionality. Ensured secure data verification using blockchain architecture.',
                'technologies': 'Ethereum, Solidity, Web3.js, Smart Contracts',
                'featured': True,
                'order': 2
            },
            {
                'title': 'Java Game Development',
                'description': 'Designed a playable, interactive game with graphics and smooth controls. Implemented core game logic and UI feedback systems.',
                'technologies': 'Java, JavaFX, Game Development',
                'featured': True,
                'order': 3
            },
        ]
        
        for project_data in projects_data:
            Project.objects.create(**project_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {Project.objects.count()} projects'))
        
        self.stdout.write(self.style.SUCCESS('Portfolio data populated successfully!'))