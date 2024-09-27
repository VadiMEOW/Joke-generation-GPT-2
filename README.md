\documentclass{article} 
\usepackage[utf8]{inputenc} 
\usepackage{hyperref}

\title{Генератор анекдотов с GPT-2} 
\author{} 
\date{}

\begin{document}

\maketitle

\section{Введение}

\textbf{Постановка проблемы}: 
В современном мире потребность в развлекательном контенте, включая анекдоты, постоянно растёт. Анекдоты играют важную роль в общении, помогают улучшить настроение и укрепить социальные связи. Автоматическая генерация анекдотов актуальна, поскольку позволяет создавать новый юмористический контент и исследовать возможности искусственного интеллекта в понимании и воспроизведении человеческого юмора.

Целью проекта является создание модели для генерации анекдотов на русском языке с использованием модели GPT-2, а также разработка интерфейса в виде Telegram-бота для взаимодействия с моделью.

\section{Обзор проекта}

\begin{itemize}
    \item \textbf{Модель}: Дообученная модель GPT-2 генерирует окончания для русских анекдотов на основе заданных фраз.
    \item \textbf{Интерфейс}: Пользователи взаимодействуют с ботом через Telegram, отправляя запросы с анекдотами и получая сгенерированные ответы.
    \item \textbf{Технологии}:
    \begin{itemize}
        \item Python
        \item Библиотека \texttt{transformers} от Hugging Face
        \item PyTorch
        \item Docker (для контейнеризации и упрощения развёртывания)
        \item Telegram API
        \item Pandas (для обработки данных)
    \end{itemize}
\end{itemize}

\section{Особенности}

\begin{itemize}
    \item Генерация анекдотов: Бот генерирует анекдоты на основе русскоязычного датасета, используя текстовые подсказки.
    \item Интеграция с Telegram: Пользователи могут взаимодействовать с ботом, отправляя запросы через Telegram и получая ответы в реальном времени.
    \item Дообучение модели: GPT-2 была дообучена на специальном датасете анекдотов для генерации связных и осмысленных текстов на русском языке.
\end{itemize}

\section{Как запустить проект}

\subsection{1. Настройка окружения}

Клонируйте репозиторий:

\begin{verbatim}
git clone https://github.com/VadiMEOW/Joke-generation-GPT-2.git
cd joke-generator-bot
\end{verbatim}

Создайте виртуальное окружение и активируйте его:

\begin{verbatim}
python3 -m venv venv
source venv/bin/activate
\end{verbatim}

Установите зависимости:

\begin{verbatim}
pip install -r requirements.txt
\end{verbatim}

\subsection{2. Запуск бота}

Добавьте токен Telegram-бота в файл \texttt{.env} (создайте файл, если его нет):

\begin{verbatim}
TELEGRAM_TOKEN=your-telegram-bot-token
\end{verbatim}

Запустите бота:

\begin{verbatim}
python bot.py
\end{verbatim}

\subsection{3. Использование Docker}

Соберите образ Docker:

\begin{verbatim}
docker build -t joke-bot .
\end{verbatim}

Запустите контейнер:

\begin{verbatim}
docker run -d --env-file=.env joke-bot
\end{verbatim}

\subsection{4. Взаимодействие с ботом}

Найдите бота в Telegram, используя ваш токен. Начните разговор и отправьте запрос с началом анекдота, например: \texttt{"Начало анекдота..."}. Бот ответит сгенерированным окончанием анекдота.

\section{Датасет}

Модель была дообучена на датасете \texttt{jokes.csv}, содержащем 129 383 русских анекдота с платформы Kaggle.

Ссылка на датасет: \href{https://www.kaggle.com/datasets/taivop/joke-dataset}{Kaggle - Russian Jokes Dataset}

\section{Перспективы улучшения}

\begin{itemize}
    \item Улучшение качества и релевантности анекдотов.
    \item Эксперименты с более продвинутыми моделями, такими как GPT-3 или GPT-Neo.
    \item Добавление фильтров для модерации контента.
    \item Поддержка нескольких языков.
\end{itemize}

\end{document}
