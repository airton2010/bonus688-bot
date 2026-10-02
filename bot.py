import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

CANAL = "https://t.me/+GpYL1MDGLhUzOTMx"
SITE = "https://688v888.com/?a=snyfnjxn"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    botoes = [
        [InlineKeyboardButton("📢 Entrar no Canal", url=CANAL)],
        [InlineKeyboardButton("🌐 Acessar o Site", url=SITE)]
    ]

    teclado = InlineKeyboardMarkup(botoes)

    await update.message.reply_text(
        "Olá! Escolha uma opção:",
        reply_markup=teclado
    )

def main():
    token = os.environ["BOT_TOKEN"]

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
