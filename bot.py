# Ligne corrigée (exemple) :
label = f'{s["name"]} - {s["price"]}€'
# Devient :
label = f'{s["name"]} - {s["price"]}€'
markup.add(telebot.types.InlineKeyboardButton(label, callback_data=f"BUY_{s['id']}"))
