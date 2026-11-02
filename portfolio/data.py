PROFILE_DATA = {
    "name":"Aadi Nagpal",
    "title": "Computer Engineering Student",
    "profession":"web developer",
    "college":"Seth Jai Parkash Polytechnic, Damla",
    "branch":"Computer Engg.",
    "email":"aadinagpal46@gmail.com",
    "location":"Yamunanagar, India",
    "introduction":"I enjoy turning ideas into clean, useful, and thoughtfully designed web applications. I'm constantly learning, building, and refining with every single release.",
    "availability":"online",
    "social_links": [
        {
            "name": "LinkedIn",
            "icon": "fa-brands fa-linkedin-in",
            "url": "https://www.linkedin.com/in/your-profile/",
        },
        {
            "name": "GitHub",
            "icon": "fa-brands fa-github",
            "url": "https://github.com/aadi-alpha",
        },
        {
            "name": "Instagram",
            "icon": "fa-brands fa-instagram",
            "url": "https://www.instagram.com/your-profile/",
        },
        {
            "name": "Email",
            "icon": "fa-solid fa-envelope",
            "url": "mailto:aadinagpal46@gmail.com",
        },
    ],

}


# SILLS CATEGORIES DETAILED
SKILL_CATEGORIES = [
    {
        "id": 1,
        "name": "Frontend Development",
        "slug": "frontend",
        "number": "01",
        "description": "Building responsive and interactive user interfaces.",
        "icon": "fa-solid fa-code",
        "note": "Focus on component architecture, CSS Flexbox/Grid, semantic markup, responsive layouts, and clean DOM manipulation.",

        "skills": [
            {
                "name": "HTML5",
                "level": "Proficient",
                "icon": "fa-brands fa-html5",
                "color": "#E34F26",
                "is_featured" : True
            },
            {
                "name": "CSS3",
                "level": "Proficient",
                "icon": "fa-brands fa-css3-alt",
                "color": "#1572B6",
                "is_featured":True
            },
            {
                "name": "JavaScript",
                "level": "Intermediate",
                "icon": "fa-brands fa-js",
                "color": "#F7DF1E",
                "is_featured":True
            },
            {
                "name": "React",
                "level": "Learning",
                "icon": "fa-brands fa-react",
                "color": "#61DAFB",
                "is_featured": False,
            }
        ]
    },

    {
        "id": 2,
        "name": "Backend Development",
        "slug": "backend",
        "number": "02",
        "description": "Developing APIs and server-side application logic.",
        "icon": "fa-solid fa-server",
        "note": "Focus on server-side logic, RESTful API development, request handling, authentication, and building scalable application structures.",

        "skills": [
            {
                "name": "Python",
                "level": "Intermediate",
                "icon": "fa-brands fa-python",
                "color": "#3776AB",
                "is_featured":True
            },
            {
                "name": "Django",
                "level": "Learning",
                "icon": "fa-solid fa-leaf",
                "color": "#092E20",
                "is_featured":True
            },
            {
                "name": "Node.js",
                "level": "Intermediate",
                "icon": "fa-brands fa-node-js",
                "color": "#339933",
                "is_featured":False
            },
            {
                "name": "Express.js",
                "level": "Intermediate",
                "icon": "fa-solid fa-route",
                "color": "#8B8B8B",
                "is_featured":False

            }
        ]
    },

    {
        "id": 3,
        "name": "Databases",
        "slug": "databases",
        "number": "03",
        "description": "Working with structured and document-based data.",
        "icon": "fa-solid fa-database",
        "note": "Focus on database design, CRUD operations, data modeling, schema relationships, and efficient data storage and retrieval.",

        "skills": [
            {
                "name": "MongoDB",
                "level": "Intermediate",
                "icon": "fa-solid fa-leaf",
                "color": "#47A248",
                "is_featured":False
            },
            {
                "name": "PostgreSQL",
                "level": "Learning",
                "icon": "fa-solid fa-database",
                "color": "#4169E1",
                "is_featured":False
            },
            {
                "name": "Mongoose",
                "level": "Intermediate",
                "icon": "fa-solid fa-cubes",
                "color": "#880000"
            }
        ]
    },

    {
        "id": 4,
        "name": "Tools & Workflow",
        "slug": "tools",
        "number": "04",
        "description": "Developer tools and version control workflows.",
        "icon": "fa-solid fa-screwdriver-wrench",
        "note": "Focus on version control, collaborative development, API testing, debugging, and maintaining efficient development workflows.",

        "skills": [
            {
                "name": "Git",
                "level": "Intermediate",
                "icon": "fa-brands fa-git-alt",
                "color": "#F05032",
                "is_featured":False
            },
            {
                "name": "GitHub",
                "level": "Intermediate",
                "icon": "fa-brands fa-github",
                "color": "#181717",
                "is_featured":True
            },
            {
                "name": "VS Code",
                "level": "Proficient",
                "icon": "fa-solid fa-code",
                "color": "#007ACC",
                "is_featured":True
            },
            {
                "name": "Postman",
                "level": "Intermediate",
                "icon": "fa-solid fa-paper-plane",
                "color": "#FF6C37",
                "is_featured":True
            }
        ]
    },
    
    {
        "id": 5,
        "name": "Cloud & Backend Services",
        "slug": "firebase",
        "number": "05",
        "description": "Building applications with cloud-based backend services.",
        "icon": "fa-solid fa-cloud",
        "note": "Focus on cloud integration, Firebase Authentication, Firestore database operations, real-time data synchronization, and backend services.",

        "skills": [
            {
                "name": "Firebase",
                "level": "Intermediate",
                "icon": "fa-solid fa-fire",
                "color": "#FFCA28",
                "is_featured": True
            }
        ]
    },

    {
        "id": 6,
        "name": "App Development",
        "slug": "app-development",
        "number": "06",
        "description": "Building cross-platform mobile applications.",
        "icon": "fa-solid fa-mobile-screen-button",
        "note": "Focus on cross-platform development, Flutter widgets, Dart fundamentals, responsive mobile layouts, and building interactive user interfaces.",
        "skills": [
            {
                "name": "Flutter",
                "level": "Learning",
                "icon": "fa-brands fa-flutter",
                "color": "#02569B",
                "is_featured": True
            }
        ]
    }

]


# ABOUT INTRODUCTION
ABOUT_INTRODUCTION = {
    "profile_image": "images/aadi_nagpal.jpg",
    "profile_tag": "Computer Engineering Student",

  

   

    "highlight": (
        "I'm pursuing a Diploma in Computer Engineering (Aided) "
        "at Seth Jai Parkash Polytechnic, Damla. I'm passionate "
        "about web development and enjoy exploring how technology "
        "can be used to solve practical problems."
    ),

    "points": [
        {
            "title": "Full-Stack Web Development",
            "icon": "fa-solid fa-battery-full",
            "description": (
                "I love bringing concepts to life across the entire stack. "
                "From building fluid, responsive interfaces that respect "
                "user attention to designing dependable server endpoints "
                "and database queries, my goal is always seamless coherence."
            )
        },
        {
            "title": "Deepening Backend Horizons with Python & Django",
            "icon": "fa-regular fa-square",
            "description": (
                "Lately, I've been expanding serious focus into the "
                "Python ecosystem—specifically Django. I appreciate "
                "its structured architecture, solid ORM capabilities, "
                "and pragmatic design philosophy for architecting "
                "data-intensive web services."
            )
        },
        {
            "title": "Pragmatic, Useful Projects",
            "icon": "fa-solid fa-crosshairs",
            "description": (
                "Theory solidifies only when tested in real situations. "
                "I prioritize building tools that solve actual community "
                "workflows—student management tools, college trackers, "
                "and workflow automation helpers that deliver tangible utility."
            )
        },
        {
            "title": "Lifelong Curiosity & Systematic Learning",
            "icon": "fa-solid fa-tree",
            "description": (
                "Whether pouring over standard library documentation, "
                "dissecting open-source codebases, or understanding "
                "memory allocation and networking primitives, I treat "
                "software engineering as an evolving craft requiring "
                "continuous collaborative practice."
            )
        }
    ],

    "quote": {
        "text": (
            "Real software mastery isn't about memorizing syntax; "
            "it's about breaking down messy problems into "
            "straightforward, reliable solutions."
        ),
        "author": "AADI'S ENGINEERING MINDSET"
    }
}


# EDUCATION JOURNEY
EDUCATION = [
    {
        "id": 1,
        "period": "2023 – Present",
        "status": "Ongoing",
        "is_completed": False,
        "title": "Diploma in Computer Engineering (Aided)",
        "institution": "Seth Jai Parkash Polytechnic, Damla",
        "institution_url": "https://www.sjpdamla.ac.in/",
        "description": (
            "Engaging in a systematic technical coursework covering "
            "algorithms, relational database administration, computer "
            "networks and full-stack software development. Active "
            "participation in departmental tech initiatives and "
            "peer development circles."
        ),
        "tags": [
            "Data Structures",
            "Web Technologies",
            "DBMS"
        ],
        "timeline_position": "left",
        "icon": "fa-solid fa-graduation-cap"
    },

    {
        "id": 2,
        "period": "Secondary School",
        "status": "Completed",
        "is_completed": True,
        "title": "Secondary School Certificate (10th Standard)",
        "institution": "S.D. Public School, Jagadhri",
        "institution_url": "https://www.sdpsjagadhri.com/",
        "description": (
            "Completed with strong academic foundations in Mathematics, "
            "Science, and logical reasoning, sparking an early interest "
            "in computing and structured problem-solving."
        ),
        "tags": [
            "Mathematics",
            "Science",
            "English",
            "Hindi",
            
        ],
        "timeline_position": "right",
        "icon": "fa-solid fa-school"
    }
]


# PERSONAL PRINCIPLES
PRINCIPLES = [

    {
        "id": 1,
        "title": "Building Useful Things",
        "icon": "fa-solid fa-hammer",
        "description": (
            "Passionate about software that genuinely helps organizations "
            "and people automate tasks and solve real-world daily friction. "
            "For me, utility is the highest mark of engineering success."
        ),
        "link_text": "Practical utility →"
    },
    {
        "id": 2,
        "title": "Learning Deeply",
        "icon": "fa-solid fa-diamond",
        "description": (
            "Curiosity for understanding how frameworks, databases, and "
            "network protocols work beneath high-level abstractions. "
            "True confidence comes from knowing the mechanics underneath."
        ),
        "link_text": "First principles →"
    },
    {
        "id": 3,
        "title": "Teamwork & Collaboration",
        "icon": "fa-solid fa-hand-holding-hand",
        "description": (
            "Enjoying hackathons, group ideation, peer code reviews, "
            "and shared technical activities. Software is fundamentally "
            "a collaborative craft elevated by collective intelligence."
        ),
        "link_text": "Community first →"
    }
]


PROJECTS = [
  {
    "id": 1,
    "title": "Takshila IMS — Multi-Branch Institute Management System",
    "slug": "takshila-ims",
    "category": "Full-Stack Enterprise",
    "number": "01",
    "label": "INSTITUTE MANAGEMENT",
    "status": "Featured Project",
    "status_type": "featured",
    "short_description": "A comprehensive cloud platform designed for multi-branch academic institutions to manage student lifecycles, role-based access, course enrollment, attendance and fee tracking.",
    "description": "A comprehensive cloud platform designed for multi-branch academic institutions to orchestrate student lifecycles, role-based access control (RBAC), multi-campus course enrollment, attendance pipelines, and fee tracking with real-time analytics.",
    "features": [
      {
        "number": "01",
        "title": "Isolation",
        "description": "Multi-branch data isolation with centralized control."
      },
      {
        "number": "02",
        "title": "RBAC Flow",
        "description": "Admin, Faculty, Student and Registrar roles."
      },
      {
        "number": "03",
        "title": "Analytics",
        "description": "Automated reports and management insights."
      }
    ],
    "technologies": [
      "React.js",
      "Node.js",
      "Express.js",
      "MongoDB",
      "JWT Auth",
      "Tailwind CSS"
    ],
    "technical_note": "RESTful APIs with modular controllers, indexed MongoDB schemas and secure JWT authentication.",
    "note_icon": "fa-solid fa-code",
    "image": "images/takshila-demo.jpg",
    "image_alt": "Takshila Institute Management System preview",
    "image_caption": "Takshila IMS — Application Preview",
    "live_url": "",
    "github_url": "hello",
    "architecture_url": "",
    "featured": True
  },
  {
    "id": 2,
    "title": "JanSetu — Digital Society Governance",
    "slug": "jansetu",
    "category": "Python / Django & Civic Tech",
    "number": "02",
    "label": "DIGITAL GOVERNANCE",
    "status": "Concept Development",
    "status_type": "planning",
    "short_description": "A transparent digital governance concept connecting municipal authorities, department workflows and local residents.",
    "description": "A transparent digital governance concept bridging communication between municipal authorities, department workflows, and local residents through a structured complaint management system, notification pipelines, and municipal issue resolution.",
    "features": [
      {
        "number": "01",
        "title": "Governance",
        "description": "Structured state, district, municipal and ward hierarchy."
      },
      {
        "number": "02",
        "title": "Complaint System",
        "description": "Department-wise complaint assignment and resolution tracking."
      },
      {
        "number": "03",
        "title": "Community",
        "description": "Citizen participation, events and local announcements."
      }
    ],
    "technologies": [
      "Python",
      "Django",
      "PostgreSQL",
      "REST API",
      "JavaScript"
    ],
    "technical_note": "Designed around role-based access, hierarchical administration and transparent complaint workflows.",
    "note_icon": "fa-solid fa-diagram-project",
    "image": "images/jansetu-demo.jpg",
    "image_alt": "JanSetu Digital Society application preview",
    "image_caption": "JanSetu — Application Preview",
    "live_url": "...",
    "github_url": "",
    
    "featured": True
  }
]


ACHIEVEMENTS = [
  {
    "id": 1,
    "position": 1,
    "date": "May 2026",
    "category": "Computer Engineering (Aided) Dept.",
    "title": "Department Project Exhibition",
    "badge": "First Position",
    "project_tag": "Multi Branch IMS Project",
    "description": "Awarded top honor for developing the Multi-Branch Institute Management System, recognized for architectural scalability and role-based access control.",
    "highlights": ["Architecture", "RBAC", "Full Stack"],
    "image": "images/achievements/project-exhibition.jpg",
    "image_alt": "Department Project Exhibition certificate",
    "certificate_url": "",
    "is_featured":True
  },
  {
    "id": 2,
    "position": 2,
    "date": "2026",
    "category": "Entrepreneurship Development Cell",
    "title": "ED Cell Ideathon",
    "badge": "First Position",
    "project_tag": "Team Innovation Project",
    "description": "Clinched first place in the college-level ideathon by presenting an impactful tech solution addressing real-world challenges.",
    "highlights": ["Innovation", "Product Strategy", "Ideation"],
    "image": "images/achievements/ed-cell-ideathon.jpg",
    "image_alt": "ED Cell Ideathon certificate",
    "certificate_url": "",
    "is_featured":True
  },
  {
    "id": 3,
    "position": 3,
    "date": "Frontend Sprint",
    "category": "TIMT",
    "title": "TIMT Web Craft",
    "badge": "Second Position",
    "project_tag": "Web Design & Development Competition",
    "description": "Secured second position in a rapid front-end engineering challenge, evaluated on UI responsiveness, accessibility and clean code standards.",
    "highlights": ["UI/UX", "Responsive Design", "HTML & CSS"],
    "image": "images/achievements/timt-webcraft.jpg",
    "image_alt": "TIMT Web Craft certificate",
    "certificate_url": "",
    "is_featured":False
  },
  {
    "id": 4,
    "position": 1,
    "date": "2024",
    "category": "District Youth Festival",
    "title": "Science Mela",
    "badge": "First Position",
    "project_tag": "Team & Individual Participation",
    "description": "Secured first position in both team and solo categories at the District Youth Festival Science Mela.",
    "highlights": ["Science", "Innovation", "Presentation"],
    "image": "images/achievements/district-youth-festival.jpg",
    "image_alt": "District Youth Festival certificate",
    "certificate_url": "",
    "is_featured":True
  },
  {
    "id": 5,
    "position": 2,
    "date": "Community Impact",
    "category": "National Service Scheme",
    "title": "NSS Active Volunteer",
    "badge": "Active Volunteer",
    "project_tag": "Community Service",
    "description": "Contributed as an NSS volunteer, participating in activities focused on community engagement and social responsibility.",
    "highlights": ["Volunteering", "Social Service", "Community"],
    "image": "images/achievements/nss-certificate.jpg",
    "image_alt": "NSS volunteer certificate",
    "certificate_url": "",
    "is_featured":False
  },
  {
    "id": 6,
    "position": 3,
    "date": "Academic Immersion",
    "category": "Remarkskill & IIT Roorkee",
    "title": "AI & ML Workshop",
    "badge": "Technical Workshop",
    "project_tag": "Artificial Intelligence & Machine Learning",
    "description": "Participated in an AI and Machine Learning workshop organized through Remarkskill in association with IIT Roorkee.",
    "highlights": ["Artificial Intelligence", "Machine Learning", "Technical Learning"],
    "image": "images/achievements/iit-roorkee-workshop.jpg",
    "image_alt": "IIT Roorkee AI and ML workshop certificate",
    "certificate_url": "",
    "is_featured":False

  }
]




CERTIFICATES =[
  {
    "id": 1,
    "title": "Python Programming Certification",
    "provider": "TuteDude Academy",
    "year": 2024,
    "type": "Certificate",
    "description": "Rigorous fundamentals program focusing on building robust backend systems, data pipelines, and object-oriented scripts.",
    "topics": [
      "Python Core",
      "OOPs",
      "Data Structures",
      "Scripting"
    ],
    "image": "images/certificates/python-certificate.jpg",
    "image_alt": "Python Programming Certificate",
    "certificate_url": "",
    "certificate_label": "View Certificate",
    "is_featured":True
  },
  {
    "id": 2,
    "title": "AI & Machine Learning Workshop",
    "provider": "Remarkskill & IIT Roorkee",
    "year": 2025,
    "type": "Workshop Certificate",
    "description": "Participated in a technical workshop focused on Artificial Intelligence and Machine Learning concepts, tools and practical applications.",
    "topics": [
      "Artificial Intelligence",
      "Machine Learning",
      "Technical Workshop"
    ],
    "image": "images/certificates/aiml-workshop.jpg",
    "image_alt": "AI and Machine Learning Workshop Certificate",
    "certificate_url": "",
    "certificate_label": "View Certificate",
    "is_featured":True



  },
  {
    "id": 3,
    "title": "Web Designing Training",
    "provider": "Contriverz",
    "year": 2024,
    "type": "Training Certificate",
    "description": "Completed a 45-day web designing training program covering the fundamentals of frontend development and website creation.",
    "topics": [
      "HTML",
      "CSS",
      "JavaScript",
      "Web Design"
    ],
    "image": "images/certificates/web-designing.jpg",
    "image_alt": "Web Designing Training Certificate",
    "certificate_url": "",
    "certificate_label": "View Certificate",
    "is_featured":True
  }
]