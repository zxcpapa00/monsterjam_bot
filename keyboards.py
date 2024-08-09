from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.db import get_sources, get_all_signatures, get_parser_info, get_signature

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📰 Источники"),
        ],
        [
            KeyboardButton(text="🤖 Данные юзербота"),
        ]
    ],
    resize_keyboard=True
)

settings_user = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="📝 Добавить данные", callback_data="settings_data"),
        ],
        [
            InlineKeyboardButton(text="⛔ Закрыть", callback_data="delete_settings"),
        ]
    ]
)

settings_user_already = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="📝 Изменить данные", callback_data="settings_data"),
        ],
        [
            InlineKeyboardButton(text="🔁 Перезапустить клиент", callback_data="restart_client"),
        ],
        [
            InlineKeyboardButton(text="⛔ Закрыть", callback_data="delete_settings"),
        ]
    ]
)

settings_parser_kb = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="➕ Добавить", callback_data="add_source"),
            InlineKeyboardButton(text="➖ Удалить", callback_data="del_source"),
        ],
        [
            InlineKeyboardButton(text="✔️ Запустить", callback_data="start_parser"),
        ],
        [
            InlineKeyboardButton(text="❌ Остановить", callback_data="stop_parser"),
        ],
        [
            InlineKeyboardButton(text="⛔ Закрыть", callback_data="delete_settings"),
        ]
    ]
)

back_settings_user = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="⏪ Назад", callback_data="back_settings_data"),
        ],
    ]
)

back_add_sources = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="⏪ Назад", callback_data="back_add_sources"),
        ],
    ]
)


def get_main_post_kb():
    post_kb = InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(text="💎 Пост в телеграмм", callback_data=f"telegram_kb"),
            ],
            [
                InlineKeyboardButton(text="📭 Пост в вконтакте", callback_data=f"vkontakte_kb"),
            ],
            [
                InlineKeyboardButton(text="📃 Добавить описание", callback_data=f"add_desc"),
            ],
            [
                InlineKeyboardButton(text="✍️ Изменить", callback_data=f"edit_kb"),
                InlineKeyboardButton(text="❌ Удалить", callback_data=f"post_delete"),
            ],
        ]
    )
    return post_kb


restore_post_kb = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="📝 Изменить текст", callback_data="edit_text"),
        ],
        [
            InlineKeyboardButton(text="🖼️ Изменить медиа", callback_data="edit_media"),
        ],
        [
            InlineKeyboardButton(text="📑 Изменить описание", callback_data="edit_desc"),
            InlineKeyboardButton(text="⏪ Назад", callback_data="back_to_main"),
        ]
    ]
)

publish_telegram_kb = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="✅ Отправить сейчас", callback_data="publish_now_tg"),
        ],
        [
            InlineKeyboardButton(text="⏳ Отправка по времени", callback_data="set_publish_time_tg"),
        ],
        [
            InlineKeyboardButton(text="⏪ Назад", callback_data="back_to_main"),
        ]
    ]
)

back_edit_kb = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="⏪ Назад", callback_data="back_to_edit"),
        ]
    ]
)

back_main_kb = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="⏪ Назад", callback_data="back_to_main"),
        ]
    ]
)

back_sign_kb = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="⏪ Назад", callback_data="back_to_sign_kb"),
        ]
    ]
)

back_sign_edit_kb = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="⏪ Назад", callback_data="back_to_signatures"),
        ]
    ]
)


def get_sources_for_del(user_id):
    builder = InlineKeyboardBuilder()
    sources = get_sources(user_id)
    for _id, user_id, title in sources:
        builder.row(InlineKeyboardButton(text=f"🚫 {title}", callback_data=f"source_del_{_id}"))
    builder.row(InlineKeyboardButton(text="⏪ Назад", callback_data=f"back_add_sources"))
    return builder.as_markup()


def get_edit_signature_kb(signature_id):
    builder = InlineKeyboardBuilder()
    sign_id, title, url = get_signature(signature_id)
    builder.row(InlineKeyboardButton(text=title, url=url))
    builder.row(InlineKeyboardButton(text="Изменить текст", callback_data=f"signature_text_edit_{signature_id}"))
    builder.row(InlineKeyboardButton(text="Изменить ссылку", callback_data=f"url_edit_signature_{signature_id}"))
    builder.row(InlineKeyboardButton(text="⏪ Назад", callback_data=f"back_to_signatures"))
    return builder.as_markup()


def get_signatures(user_id):
    builder = InlineKeyboardBuilder()
    signatures = get_all_signatures(user_id)
    for _id, title in signatures:
        builder.row(InlineKeyboardButton(text=f"✅ {title}", callback_data=f"edit_signature_{_id}"))
    builder.row(InlineKeyboardButton(text="➕ Добавить", callback_data=f"add_signature"),
                InlineKeyboardButton(text="➖ Удалить", callback_data=f"delete_signatures"))
    builder.row(InlineKeyboardButton(text="⏪ Назад", callback_data=f"back_to_edit"))
    return builder.as_markup()


def get_signatures_for_del(user_id):
    builder = InlineKeyboardBuilder()
    signatures = get_all_signatures(user_id)
    for _id, title in signatures:
        builder.row(InlineKeyboardButton(text=f"🚫 {title}", callback_data=f"signature_del_{_id}"))
    builder.row(InlineKeyboardButton(text="⏪ Назад", callback_data=f"back_to_sign_kb"))
    return builder.as_markup()


def get_started_kb(user_id, _type):
    builder = InlineKeyboardBuilder()
    parsers = get_sources(user_id)
    for _id, user_id, title in parsers:
        if get_parser_info(user_id, title):
            builder.row(InlineKeyboardButton(text=f"✅ {title}", callback_data=f"{_type}_source_{title}"))
        else:
            builder.row(InlineKeyboardButton(text=f"❌ {title}", callback_data=f"{_type}_source_{title}"))
    if _type == "start":
        builder.row(InlineKeyboardButton(text="✅ Запустить все ✅", callback_data=f"start_all_parser"))
    else:
        builder.row(InlineKeyboardButton(text="❌ Остановить все ❌", callback_data=f"stop_all_parser"))
    builder.row(InlineKeyboardButton(text="⏪ Назад", callback_data=f"back_add_sources"))
    return builder.as_markup()


def set_signature_for_post_kb(user_id, message_id):
    builder = InlineKeyboardBuilder()
    signatures = get_all_signatures(user_id)
    for _id, title in signatures:
        builder.row(InlineKeyboardButton(text=f"  {title}  ", callback_data=f"add_sign_{_id}|{message_id}"))
    builder.row(InlineKeyboardButton(text="⏪ Назад", callback_data=f"back_to_main"))
    return builder.as_markup()
