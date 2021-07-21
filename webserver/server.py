import emoji
import torch

from flask import Flask, jsonify, request
from model import BERTGRUSentiment
from transformers import BertTokenizer, BertModel


tokenizer = BertTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-uncased")
bert = BertModel.from_pretrained("dccuchile/bert-base-spanish-wwm-uncased")
app = Flask(__name__)
device = torch.device("cpu")

HIDDEN_DIM = 256
OUTPUT_DIM = 1
N_LAYERS = 2
BIDIRECTIONAL = True
DROPOUT = 0.25

model = BERTGRUSentiment(bert, HIDDEN_DIM, OUTPUT_DIM, N_LAYERS, BIDIRECTIONAL, DROPOUT)

model.load_state_dict(torch.load("tut6-model.pt", map_location=device))
model.eval()

max_input_length = 512
init_token_idx = tokenizer.cls_token_id
eos_token_idx = tokenizer.sep_token_id


def predict_sentiment(sentence):
    sentence = emoji.demojize(sentence, language="es")
    tokens = tokenizer.tokenize(sentence)
    tokens = tokens[: max_input_length - 2]
    indexed = (
        [init_token_idx] + tokenizer.convert_tokens_to_ids(tokens) + [eos_token_idx]
    )
    tensor = torch.LongTensor(indexed).to(device)
    tensor = tensor.unsqueeze(0)
    prediction = torch.sigmoid(model(tensor))
    return prediction.item()


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        sentence = request.json["sentence"]
        pred = predict_sentiment(sentence)
        return jsonify({"prediction": pred})


if __name__ == "__main__":
    app.run()
