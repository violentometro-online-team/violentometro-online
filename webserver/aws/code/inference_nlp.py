import json
import logging
import os
import torch
import emoji

from model import BERTGRUSentiment
from transformers import BertTokenizer, BertModel


logger = logging.getLogger(__name__)

tokenizer = BertTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-uncased")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

max_input_length = 512
init_token_idx = tokenizer.cls_token_id
eos_token_idx = tokenizer.sep_token_id


def model_fn(model_dir):
    bert = BertModel.from_pretrained("dccuchile/bert-base-spanish-wwm-uncased")
    logger.info("Loading the model.")

    HIDDEN_DIM = 256
    OUTPUT_DIM = 1
    N_LAYERS = 2
    BIDIRECTIONAL = True
    DROPOUT = 0.25

    model = BERTGRUSentiment(
        bert, HIDDEN_DIM, OUTPUT_DIM, N_LAYERS, BIDIRECTIONAL, DROPOUT
    )

    with open(os.path.join(model_dir, "tut6-model.pt"), "rb") as f:
        model.load_state_dict(torch.load(f, map_location=device))

    model.to(device).eval()
    logger.info("Done loading model")
    return model


def input_fn(request_body, content_type="application/json"):
    logger.info("Deserializing the input data.")
    if content_type == "application/json":
        input_data = json.loads(request_body)
        sentence = input_data["sentence"]
        logger.info(f"Sentence received: {sentence}")

        sentence = emoji.demojize(sentence, language="es")
        tokens = tokenizer.tokenize(sentence)
        tokens = tokens[: max_input_length - 2]
        indexed = (
            [init_token_idx] + tokenizer.convert_tokens_to_ids(tokens) + [eos_token_idx]
        )
        tensor = torch.LongTensor(indexed).to(device)
        tensor = tensor.unsqueeze(0)

        return tensor
    raise Exception(
        f"Requested unsupported ContentType in content_type: {content_type}"
    )


def output_fn(prediction_output, accept="application/json"):
    logger.info("Serializing the generated output.")

    if accept == "application/json":
        return json.dumps({"prediction": prediction_output})
    raise Exception(f"Requested unsupported ContentType in Accept: {accept}")


def predict_fn(input_data, model):
    logger.info("Generating prediction based on input parameters.")

    with torch.no_grad():
        model.eval()
        out = model(input_data)
        ps = torch.sigmoid(out)

    return ps.item()
