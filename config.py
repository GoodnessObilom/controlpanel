#db variables
HOST="localhost"
USER="pterodactyl" # Replace with your database user
PASSWORD="1" # Replace with your database user's password
DATABASE="panel" # Replace with your database name (you might need to create this)

PTERODACTYL_URL="https://television.goodnesstechhost.xyz/" # Your Pterodactyl URL
PTERODACTYL_ADMIN_KEY = "ptlc_aoqYkiwOZy58c7dAfrhz1lwVZZwE9bL7lkBl801uLRD" # Your Pterodactyl Admin API Key
PTERODACTYL_CLIENT_KEY = "ptlc_aoqYkiwOZy58c7dAfrhz1lwVZZwE9bL7lkBl801uLRD" # Often not needed for this type of integration, but provide if you have one
STRIPE_API_KEY = "" # Your Stripe API Key if using Stripe
STRIPE_SECRET_KEY = "" # Your Stripe Secret Key if using Stripe
URL = "https://control.goodnesstechhost.xyz/" # Your control panel's URL (change for production)
YOUR_SUCCESS_URL = f'{URL}store/success'
YOUR_CANCEL_URL = f'{URL}store/cancel'
HOSTED_URL = URL
SECRET_KEY = "" # GENERATE A UNIQUE ONE!
MAIL_SERVER="smtp.gmail.com" # Your mail server
MAIL_PORT = 587 # Common SMTP port (587 for TLS, 465 for SSL)
MAIL_USERNAME = "obilomgoodness9@gmail.com"
MAIL_PASSWORD = "ezih atbo fppu sdcu"
MAIL_DEFAULT_SENDER = ""
RECAPTCHA_SITE_KEY = "0x4AAAAAABnzxiChs7lGEMMi"
RECAPTCHA_SECRET_KEY = "0x4AAAAAABnzxgbISzL_20CdKuqsLrHA-A4"
WEBHOOK_URL = "https://discord.com/api/webhooks/1399111793556717588/1qxJmlZkmWLAVTkV1DCuI809Lm_qfxmjh99dv7bv8hc3_Uto0yumkbwb9pYJHV9T5esh"
TICKET_WEBHOOK_URL=WEBHOOK_URL
#DISCORD BOT
ENABLE_BOT = False # Set to True if you want to enable the Discord bot
TOKEN = "" # Your Discord bot token if ENABLE_BOT is True
DEBUG_FRONTEND_MODE = False # Set to False for production
AUTODEPLOY_NEST_ID: int = 5 # Your Pterodactyl Nest ID for auto-deployment
#DISCORD INVITE
DISCORD_INVITE = "https://discord.gg/Y7fWp9sB" # Your Discord invite link