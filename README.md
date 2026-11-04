# Aadi Nagpal | Personal Portfolio

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
</p>

<p align="center">
  <strong>A modern, responsive, and dynamic personal portfolio built with Django.</strong>
</p>

<p align="center">
  <a href="https://aadi-nagpal-portfolio.onrender.com/">Live Portfolio</a> •
  <a href="https://github.com/aadi-alpha">GitHub</a> •
  <a href="https://www.linkedin.com/in/aadi-nagpal-7a635333a/">LinkedIn</a>
</p>

---

## 📌 About the Project

This is my personal portfolio website, developed to showcase my technical skills, educational background, projects, achievements, and certifications.

The website combines a clean frontend design with Django's backend capabilities to provide a dynamic and maintainable portfolio experience.

The project also serves as a practical learning experience in Django development, database integration, template rendering, and deployment.

## ✨ Features

- **Personal Introduction:** Professional introduction and profile information.
- **About Me:** Background, interests, and development journey.
- **Education:** Academic background and educational timeline.
- **Technical Skills:** Organized skills and technology categories.
- **Projects:** Showcase of personal and academic projects.
- **Achievements:** Highlights of competitions and accomplishments.
- **Certificates:** Display of certifications and workshops.
- **Contact:** Contact information and social links.
- **Django Admin:** Manage portfolio content through the administration panel.
- **Dynamic Content:** Portfolio information managed through Django models.
- **Responsive Design:** Designed to provide a consistent experience across different screen sizes.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| Django Templates | Dynamic HTML rendering |
| HTML5 | Website structure |
| CSS3 | Styling and responsive layouts |
| JavaScript | Frontend interactions |
| PostgreSQL | Database |
| Django ORM | Database operations |
| Django Unfold | Enhanced administration interface |
| Git & GitHub | Version control |
| PythonAnywhere | Deployment |

## 📂 Project Structure

```text
aadi-nagpal-portfolio/
│
├── portfolio_django/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── portfolio/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── ...
│
├── templates/
│   └── portfolio/
│       ├── base.html
│       ├── home.html
│       ├── about.html
│       ├── skills.html
│       ├── projects.html
│       ├── certificates.html
│       └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/aadi-alpha/aadi-nagpal-portfolio.git
```

### 2. Navigate to the Project Directory

```bash
cd aadi-nagpal-portfolio
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root and configure the required environment variables.

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

Configure your database credentials if required by your Django settings.

**Never commit your actual secret key, database passwords, or production credentials.**

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the website:

```text
http://127.0.0.1:8000/
```

Access the Django administration panel:

```text
http://127.0.0.1:8000/admin/
```

## 🧑‍💻 Development Highlights

While developing this project, I worked with:

- Django models and relationships
- Django ORM and database queries
- Template inheritance and reusable components
- Static files and asset management
- Django administration customization
- Environment variables and configuration
- PostgreSQL database integration
- Deployment and production configuration

## 🔮 Future Improvements

- Improve website performance and accessibility.
- Add more interactive portfolio sections.
- Enhance project filtering and navigation.
- Continue refining the design and user experience.
- Expand portfolio content as new projects and achievements are completed.

## 👨‍💻 About Me

I'm **Aadi Nagpal**, a Computer Engineering student and aspiring full-stack developer from Haryana, India.

I enjoy building practical web applications, exploring new technologies, and continuously improving my development skills.

### Connect With Me

<p align="center">
  <a href="https://github.com/aadi-alpha">GitHub</a> •
  <a href="https://www.linkedin.com/in/aadi-nagpal-7a635333a/">LinkedIn</a> •
  <a href="https://aadi-nagpal-portfolio.onrender.com/">Portfolio</a>
</p>

---

<p align="center">
  <i>Designed and developed with curiosity, creativity, and continuous learning.</i>
</p>
