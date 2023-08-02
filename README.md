# HeraldBlogApp

Welcome to HeraldBlogApp! This is a simple web application built using Django, a high-level Python web framework, to showcase various features and functionalities.

## Features

- User Registration and Authentication: The app includes a user registration system with custom fields like 'name', 'email', and 'password' for a personalized experience.

- Blog App: We have implemented a simple blog application with CRUD functionalities that allow users to create, read, update, and delete blog posts.

## Getting Started

To run the app locally on your machine, follow these steps:

1. Clone the repository to your local machine:
```
git clone https://github.com/sabin-lohani/Herald-Django.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Apply database migrations:
```
python manage.py migrate
```

4. Create a superuser (admin) account:
```
python manage.py createsuperuser
```

5. Start the development server:
```
python manage.py runserver
```

6. Access the app in your web browser at `http://localhost:8000/`

## Environment Variables

Before running the app, make sure to set up the following environment variables:

- EMAIL_BACKEND: The email backend for sending notifications.
- EMAIL_HOST: The hostname of the email server.
- EMAIL_HOST_USER: The email address for sender authentication.
- EMAIL_HOST_PASSWORD: The password for the email account used for sender authentication.
- EMAIL_PORT: The port number for the email server.
- EMAIL_USE_TLS: Set this to True if using TLS encrypted connection.
- DEFAULT_FROM_EMAIL: The default "From" email address used in the application for sending emails.

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript

## Contributing

We welcome contributions to improve and add new features to this app. Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

We extend our gratitude to Mr. Rukesh Shrestha, our tutor, for his valuable guidance during the development of this app.

Enjoy exploring My Django App! If you have any questions or feedback, please don't hesitate to reach out.

Thank you! 😊
