<h1>Introduction</h1>

This project is a backend system for an online exam platform designed to provide secure and efficient interactions between users and the platform. In the **Accounting** section, **OTP** and **JWT** are used for authentication and enhanced security.  
The **Exam** module supports two main roles: students can take exams, view their scores, and check rankings, while instructors can create and manage exams. Features such as **nested routers** and **throttle** are implemented to optimize performance and improve user experience.  
With a focus on security, scalability, and user-centric design, this system offers a reliable platform for online assessments.

<h1>db Diagram</h1>

![db Diagram](https://github.com/Mohamad-bigdeli/DRF-OnlineExam/docs/exam.png)

<h1>Technologies</h1>

![Django Rest Frameworke](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=json-web-tokens&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Flake8](https://img.shields.io/badge/Flake8-000000?style=for-the-badge&logo=flake8&logoColor=white)
![Black](https://img.shields.io/badge/Black-000000?style=for-the-badge&logo=black&logoColor=white)

<h1>Project Overview</h1>

**This project leverages a robust stack of technologies to ensure efficient development, testing, deployment, and monitoring. Below is a breakdown of the key technologies used:**

- Python : The primary programming language for backend development.

- Django : A high-level web framework for building secure and maintainable web applications.

- GitHub Actions : Used for CI/CD automation, enabling seamless testing and deployment workflows.

- Docker : Containerization tool to create consistent development and deployment environments.

- Pytest : A powerful testing framework to ensure code reliability and quality.

- PostgreSQL: A powerful, open-source relational database management system used in this project for data storage and management.

- Redis : Serves as both a caching layer and message broker for Celery.

- Swagger : Provides interactive API documentation for easy testing and integration.

- JWT : JSON Web Tokens for secure user authentication and authorization.

- Nginx : Acts as a web server and reverse proxy to manage incoming traffic.

- Flake8 & Black : Tools for code linting and automatic code formatting to maintain code quality.

## 🚀 Project Setup

To set up the project, follow the steps below:

### Prerequisites
- **Docker**: If you don't have Docker and Docker Compose installed, follow the [Docker installation guide](https://docs.docker.com/get-docker/) and the [Docker Compose installation guide](https://docs.docker.com/compose/install/).

---

### Setup Steps

1. **Clone the Repository**
  
   Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/Mohamad-bigdeli/Django-Api-Blog.git

2. **Navigate to the Project Folder**

    Move into the project directory using the cd command:

    ```bash
    cd Django-Api-Blog
    

3. **Start Docker Compose** 

    Use Docker Compose to start the project services by running the command:

    ```bash
    docker-compose up --build 

4. **Create and Apply Migrations**

    After the services are up, create and apply the database migrations using the following commands:
    ```bash 
    docker-compose exec backend sh -c "python manage.py makemigrations"

    docker-compose exec backend sh -c "python manage.py migrate"

5. **Create a Superuser**

    Create a superuser to access the Django admin panel by running the command:

    ```bash
    docker-compose exec backend sh -c "python manage.py createsuperuser"

6. **Collect Static Files**

    Collect static files for the project using the command:

    ```bash
    docker-compose exec backend sh -c "python manage.py collectstatic --noinput"
    
7. **View the Project**

    Your project is now running on port 8000. Open your browser and navigate to:

   ```bash
    http://localhost:8000.

8. **Access the Admin Panel**

    To access the Django admin panel, go to the following URL and log in with your superuser credentials:

    ```bash
    http://localhost:8000/admin

**Additional Notes**

    If you make changes to the code and need to restart the services, use the docker-compose restart command.
    To stop the services, use the docker-compose down command.

<h3>By following these steps, your project will be fully set up and ready to use. 🎉</h3>
