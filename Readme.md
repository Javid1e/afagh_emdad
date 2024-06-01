# Afagh Emdad Full Django Next Docker

Afagh Emdad is a full-stack web application built with Django REST Framework and Next.js, utilizing Next UI, Tailwind CSS, Axios, Docker, and NGINX. This application aims to provide road assistance services to users. Below is a comprehensive guide to set up, configure, and run the application.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Technologies Used](#technologies-used)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

To install and run Afagh Emdad locally, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone <repository-url>
    ```

2. Navigate into the project directory:

    ```bash
    cd afagh_emdad_full_django_next_docker
    ```

3. Install dependencies for both Django and Next.js:

    ```bash
    cd apps/web
    poetry install
    cd ../www
    pnpm install
    ```

## Usage

Before running the application, ensure you have set up the required environment variables. Refer to the `.env.example` files in both the `apps/web` and `apps/www` directories.

To start the Django server, run the following command in the `apps/web` directory:

    ```bash
    poetry run python manage.py runserver
    ```

To start the Next.js development server, run the following command in the `apps/www` directory:

    ```bash
    pnpm dev
    ```

Access the application in your web browser at `http://localhost:3000`.

### Using Docker

To run the application using Docker, follow these steps:

1. Navigate to the `apps/docker` directory:

    ```bash
    cd apps/docker
    ```

2. Build and start the Docker containers:

    ```bash
    docker-compose up --build
    ```

This will start all the necessary services, including Django, Next.js, NGINX, and MariaDB.

Access the application in your web browser at `http://localhost`.

## Project Structure

```
$PROJECT_ROOT
├── apps/web                  # Django Backend
├── apps/docker               # Docker files for web, www, nginx
├── apps/www                  # Next.js App
├── apps/web/requirements     # Python Requirements
├── apps/web/manage.py        # Run Django Commands
├── apps/www/package.json     # npm commands.
```

## Getting Started

### Clone Repo

```bash
mkdir dockerize-django-with-nextjs
cd dockerize-django-with-nextjs
git clone <repository-url> .
```

### Using Docker

```bash
docker-compose up --build
```

Open Django Server at: [http://0.0.0.0:8000](http://0.0.0.0:8000)

Open Django Admin at: [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin)

Open Next.js Server at: [http://0.0.0.0](http://0.0.0.0)

### Manual Way

#### For Django

Create Virtual Environment for Python

```bash
pip install poetry
poetry install
```

Activate Virtual Environment

```bash
poetry shell
```

Install Dependencies

```bash
poetry install
```

Make Migrations

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

#### For Frontend

Install Dependencies

```bash
pnpm install --prefix apps/www
```

Run Dev Server

```bash
pnpm dev --prefix apps/www
```

Now for Bundling Your Frontend

```bash
pnpm build --prefix apps/www
```

## Technologies Used

- Django REST Framework
- Next.js
- Nextui Library
- Tailwind CSS Framework
- Axios
- Docker
- NGINX
- MariaDB
- React
- Python
- JavaScript
- HTML
- CSS

## Contributing

Contributions are welcome! If you'd like to contribute to Afagh Emdad, please fork the repository and create a pull request with your changes. Ensure to follow the existing code style and conventions.

## License

This project is licensed under the [MIT License](LICENSE).