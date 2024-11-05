from pathlib import Path
import os

# Para desenvolvimento local, descomente as opções abaixo se for necessário implementar SSL
# SECURE_SSL_REDIRECT = False  

# SESSION_COOKIE_SECURE = False  # Para desenvolvimento local, evite cookies seguros
# CSRF_COOKIE_SECURE = False

# Para produção, você pode usar HSTS, mas desative em ambiente local
# SECURE_HSTS_SECONDS = 31536000  # 1 ano
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# Desative filtros de segurança que são usados apenas em produção
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-lzc)l!c$ew3kylcssvcvdr^5^ww9=wp$ivt@&$o6pei+!0$oug'

DEBUG = True  # Para ambiente de desenvolvimento, deve ser True

ALLOWED_HOSTS = ['54.233.92.107', 'localhost', '127.0.0.1']  # Adicione aqui todos os hosts permitidos

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',  # Seu app customizado
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'websys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'websys.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [ 
    BASE_DIR / 'static', 
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'  
LOGIN_REDIRECT_URL = 'area_do_candidato'  
LOGOUT_REDIRECT_URL = 'pagina_inicial'

AUTH_USER_MODEL = 'website.Usuario'  # Use seu modelo de usuário customizado

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  
]

# Configurações de email para envio via Gmail (segurança recomendada: ocultar senhas sensíveis)
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'shelton.oliveira.barbosa@gmail.com'
EMAIL_HOST_PASSWORD = '@Drik16091985'

SITE_ATUALIZACAO = False  # Variável personalizada
