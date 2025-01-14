
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*bzwzl9d&aq)rg2z9(@twit_)=5fp77et3i&l4-xp1h$r)^+gp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


ROOT_URLCONF = 'vnpay_python.urls'


WSGI_APPLICATION = 'vnpay_python.wsgi.application'





LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Saigon'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)
STATIC_URL = '/static/'
# VNPAY CONFIG
VNPAY_RETURN_URL = 'http://localhost:8000/payments/payment_return'  # get from config
VNPAY_PAYMENT_URL = 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html'  # get from config
VNPAY_API_URL = 'https://sandbox.vnpayment.vn/merchant_webapi/api/transaction'
VNPAY_TMN_CODE = 'TXOOZNX4'  # Website ID in VNPAY System, get from config
VNPAY_HASH_SECRET_KEY = 'HUQHTRVXVRGJJWHMBFCAUBAXOSAJBIND'  # Secret key for create checksum,get from config
