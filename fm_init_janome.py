from typing import Callable
from janome.tokenizer import Tokenizer

JANOME_TOKENIZER = Tokenizer()

def janome_tokenizer_provided_via_user_files_init(txt: str) -> list[str]:

    token_list = list(token for token in JANOME_TOKENIZER.tokenize(txt, wakati=True) if isinstance(token, str))
    return token_list


def janome_tokenizers_provider() -> list[tuple[str, Callable]]:

    return [("ja", janome_tokenizer_provided_via_user_files_init)]


