# Localization

First of all, extract translatable strings from the source code by using `generate_messages_pot.sh`.

Then, `generate_new_locale.sh <locale_id>` will create a new locale folder for the given locale.
From there, you may edit `messages.pot` for that locale, e. g.: `./translations/<locale_id>/LC_MESSAGES/messages.pot`.

When you are done, compile the locale to a `.mo` format that Flask understands with `compile_translations.sh`.

If you add new strings for translation in the source code, you will need to update the `messages.pot` file (`update_translations.sh`). If you are lucky, it won't screw up your existing translation files.
Remember that you'll have to wrap the strings in `_()` to make them translatable (or `{% trans %}...{% endtrans %}` in Jinja templates).

This directory can be put in a sub-repo as well, if you have a private project for the source code, but want to still accept community translations.

Flask-Babel documentation: [https://flask-babel.tkte.ch](https://flask-babel.tkte.ch/)
