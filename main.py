import logging
from replit import db

#del db["apa"]
#del db["alur"]
#del db["tujuan"]
#del db["cp"]
#del db["form"]

# database

db["apa"] = """Aspirasi secara garis besar memiliki makna tujuan dan harapan yang membangun untuk masa yang akan datang. Aspirasi memiliki peran penting untuk menyalurkan ide, masukan, dan juga harapan dari seluruh mahasiswa dalam rangka meningkatkan kualitas agar terwujudnya cita-cita serta tujuan yang diinginkan"""
# print(db["apa"])

# database

db["alur"] = """Terima kasih sudah memberikan aspirasi kepada kami. Aspirasi kamu akan kami olah dan filter terlebih dahulu lalu kemudian akan kami salurkan kepada pihak terkait. Setiap progress yang kami lakukan akan ter-update pada official instagram kami. Silahkan cek secara berkala."""
# print(db["alur"])


db["tujuan"] = "Tujuan Aspirasi merupakan tujuan/sasaran dari aspirasi kamu disalurkan seperti Badan Semi Otonom HMTT, BP HMTT, DPA HMTT, Layanan dan Civitas, dan Lainnya yang bisa kamu jabarkan sesuai tujuanmu."
# print(db["tujuan"])


db["form"] = """Terima kasih sudah mau memberikan aspirasi kepada kami! Kamu bisa memasukkan aspirasi kamu pada link berikut ini :  https://bit.ly/AspirationDays2022."""
# print(db["form"])


db["cp"] = """Kamu masi bingung tentang aspirasi? Atau ada hal lain yang ingin ditanyakan mengenai aspirasi silahkan hubungan CP berikut ini yaa ^^ Thalita : 087825578991"""
# print(db["cp"])



from telegram import __version__ as TG_VER

try:

  from telegram import __version_info__

except ImportError:

  __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):

  raise RuntimeError(
    f"This example is not compatible with your current PTB version {TG_VER}. To view the "
    f"{TG_VER} version of this example, "
    f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html")

from telegram import ForceReply, Update

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging

logging.basicConfig(
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO)

logger = logging.getLogger(__name__)

#if "apa" in db:
#    print("ada")

# Define a few command handlers. These usually take the two arguments update and

# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /start is issued."""

  user = update.effective_user

  await update.message.reply_html(
    rf"Halo {user.mention_html()}, Selamat Datang di Aspirasi Bot",
    reply_markup=ForceReply(selective=True),
  )

  await update.message.reply_text("""
    Ketik perintah dibawah ini untuk mengetahui tentang kami :
    /ApaItuAspirasi 
    /AlurAspirasi
    /TujuanAspirasi
    /FormAspirasi
    /CP -> Contact Person 
    /help -> Untuk Bantuan
    """)


async def help_command(update: Update,
                       context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /help is issued."""

  await update.message.reply_text("""
    Ketik perintah dibawah ini untuk mengetahui tentang kami :
    /ApaItuAspirasi 
    /AlurAspirasi
    /TujuanAspirasi
    /FormAspirasi
    /CP -> Contact Person 
    /help -> Untuk Bantuan
    """)


async def ApaItuAspirasi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /apa is issued."""

  await update.message.reply_text(db["apa"])


async def AlurAspirasi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /apa is issued."""
  
  await update.message.reply_text(db["alur"])

async def TujuanAspirasi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /apa is issued."""

  await update.message.reply_text(db["tujuan"])

async def FormAspirasi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /apa is issued."""

  await update.message.reply_text(db["form"])

async def CP(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /apa is issued."""

  await update.message.reply_text(db["cp"])
  
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Echo the user message."""

  await update.message.reply_text("""Maaf keyword tidak dikenal.Ketik perintah dibawah ini untuk mengetahui tentang kami :
    /ApaItuAspirasi 
    /AlurAspirasi
    /TujuanAspirasi
    /FormAspirasi
    /CP -> Contact Person 
    /help -> Untuk Bantuan
    """)


def main() -> None:
  """Start the bot."""

  # Create the Application and pass it your bot's token.

  application = Application.builder().token(
    "5724601279:AAEiwWaZghotRazLh2bO_Nq9JYTes9cmCO0").build()

  # on different commands - answer in Telegram

  application.add_handler(CommandHandler("start", start))

  application.add_handler(CommandHandler("help", help_command))

  application.add_handler(CommandHandler("ApaItuAspirasi", ApaItuAspirasi))
  application.add_handler(CommandHandler("AlurAspirasi", AlurAspirasi))
  application.add_handler(CommandHandler("TujuanAspirasi", TujuanAspirasi))
  application.add_handler(CommandHandler("FormAspirasi", FormAspirasi))
  application.add_handler(CommandHandler("CP", CP))
  # on non command i.e message - echo the message on Telegram

  application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,
                                         echo))

  # Run the bot until the user presses Ctrl-C

  application.run_polling()


if __name__ == "__main__":

  main()
