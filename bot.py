#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nest_asyncio
nest_asyncio.apply()

import os
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)
import logging
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
import torch

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Загрузка переменных окружения из файла .env
load_dotenv()

# Загрузка дообученной модели из сохранённой директории
model_path = './models/trained_model'  # Путь к вашей сохранённой модели
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)
# Получение токена из переменных окружения
TOKEN = os.getenv('TELEGRAM_TOKEN')

# Создание пайплайна генерации
device = 0 if torch.cuda.is_available() else -1
generator = pipeline('text-generation', model=model, tokenizer=tokenizer, device=device)

# Функции-обработчики команд
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Привет! Я бот, который генерирует концовки анекдотов.\n'
        'Напиши мне начало анекдота, и я его продолжу.'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Просто отправьте мне начало анекдота, и я постараюсь его продолжить!')

async def generate_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text
    
    # Генерация текста в отдельном потоке
    loop = asyncio.get_event_loop()
    try:
        generated = await loop.run_in_executor(
            None,
            lambda: generator(
                prompt,
                max_length=250,
                #max_new_tokens=150,
                truncation=True,
                num_return_sequences=1,
                no_repeat_ngram_size=3,
                repetition_penalty=1.2,
                top_p=0.8,
                temperature=0.6,
                do_sample=True,
                top_k=40,
                eos_token_id=tokenizer.eos_token_id,
            )
        )
        joke = generated[0]['generated_text']
        joke = joke.split('<|endoftext|>')[0].strip()
        await update.message.reply_text(joke)
    except Exception as e:
        await update.message.reply_text('Произошла ошибка при генерации анекдота.')
        logging.error(f"Ошибка генерации: {e}")

# Создание приложения
application = ApplicationBuilder().token(TOKEN).build()

# Добавление обработчиков
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_joke))

# Запуск бота
application.run_polling()


# In[ ]:




