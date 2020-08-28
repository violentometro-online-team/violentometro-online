import emoji
import es_core_news_sm
import re
import pandas as pd
import string

nlp = es_core_news_sm.load()


def clean_text(text):
    """Make text lowercase, remove punctuation and remove words containing numbers."""
    text = text.lower()
    text = re.sub(".*?¿", "", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("\w*\d\w*", "", text)
    text = re.sub("\n", "", text)
    re.sub("[0-9]+", "", text)
    return text


def delete_stop_words(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop]
    return " ".join(token for token in tokens)


def lemmatize(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc]
    return " ".join(token for token in tokens)


def delete_emoji(text):
    return emoji.get_emoji_regexp().sub(u"", text)


def add_features(text):
    words = text.split()
    text_len = len(text)
    text_words_count = len(words)
    unique_words_count = len(set(words))

    return text_len, text_words_count, unique_words_count


def predict(text, model, count_vectorizer):
    text_cleaned = clean_text(text)
    without_stop_words = delete_stop_words(text_cleaned)
    lemmatized = lemmatize(without_stop_words)
    without_emojis = delete_emoji(lemmatized)
    text_len, text_words_count, unique_words_count = add_features(without_emojis)

    X_vec = count_vectorizer.transform([without_emojis])
    vocab = count_vectorizer.get_feature_names()
    X = pd.DataFrame(X_vec.toarray(), columns=vocab)
    X["Longitud_Text"] = text_len
    X["Numero_Palabras_Text"] = text_words_count
    X["Numero_Palabras_Unicas"] = unique_words_count

    prediction_proba = model.predict_proba(X)

    res = {
        "No discurso de Odio": prediction_proba[0][0],
        "Discurso de Odio": prediction_proba[0][1],
        "Discurso de Odio contra Mujeres": prediction_proba[0][2],
    }

    return res
